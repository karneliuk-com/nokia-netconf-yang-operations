"""
Sample admin operation via NETCONF
"""
# Modules
import os
import yaml
from pprint import pprint
import xmltodict
from ncclient import manager
from ncclient.xml_ import to_ele


# Statics
PATH_INVENTORY = "./inventory.yaml"
KIND_CREDS = "env"


# Functions
def get_inventory(path: str) -> list:
    """
    High-level function to get inventory
    """
    with open(file=path, mode="rt", encoding="utf-8") as filename:
        return yaml.load(stream=filename.read(), Loader=yaml.FullLoader)


def get_credentials(kind: str) -> tuple:
    """
    High-level function to get credentials
    """
    creds_fun_dict = {
        "env": _get_env_credentials,
    }

    return creds_fun_dict[kind]()


def _get_env_credentials() -> tuple:
    """
    Private function to get credentials from variables
    """
    return os.getenv(key="AUTOMATION_USER"), os.getenv(key="AUTOMATION_PASS")


def _print_result(nested_data, indent: int = 0) -> None:
    """
    Private function to print result
    """
    indent += 2
    for key, value in nested_data.items():
        if isinstance(value, str):
            print(" " * indent + key.split(":")[-1] + ": " + value)

        else:
            print(" " * indent + key.split(":")[-1] + ":")
            _print_result(indent=indent, nested_data=value)

# Body
if __name__ == "__main__":
    # Get inventory
    inventory = get_inventory(path=PATH_INVENTORY)

    # Get credentails
    creds = get_credentials(kind="env")

    # Perform ping
    for host in inventory:
        with manager.connect(
            host=host["hostname"],
            username=creds[0],
            password=creds[1],
            device_params={"name": "sros"},
        ) as nco:
            # Check if device supports ping
            match_ping_module = False
            for netconf_module in nco.server_capabilities:
                if netconf_module.find("oper-global") >= 0:
                    match_ping_module = True

            if match_ping_module:
                print(f"Device {host['hostname']} supports ping via NETCONF")

                # Prepare ping body
                message_dict = {
                    "action": {
                        "@xmlns": "urn:ietf:params:xml:ns:yang:1",
                        "global-operations": {
                            "@xmlns": "urn:nokia.com:sros:ns:yang:sr:oper-global",
                            "ping": {"destination": "10.0.255.22", "count": 3},
                        },
                    }
                }

                message_xml = xmltodict.unparse(input_dict=message_dict)
                message_xml = message_xml.split("\n")[-1]

                ping_result = nco.dispatch(to_ele(message_xml))

                parsed_result = xmltodict.parse(xml_input=str(ping_result))

            if parsed_result:
                terminal_length = os.get_terminal_size().columns

                print("=" * terminal_length)
                print(f"Reachability to {host['hostname']}")
                print("=" * terminal_length)

                _print_result(nested_data=parsed_result["rpc-reply"]["nokiaoper:results"]["nokiaoper:summary"])


            else:
                print(f"Device {host['hostname']} DOES NOT support ping via NETCONF")
                exit("1")
