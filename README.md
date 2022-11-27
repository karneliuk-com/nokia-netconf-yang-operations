# Demo of Operational modules for NETCONF/YANG in Nokia SR OS
This repository contains the demo Python code to perform operational activities on Nokia SR OS network routers and switches via NETCONF.

## Usage
1. Modify the `app/inventory.yaml` file to match your needs:
```yaml
---
- hostname: 192.168.101.11
```

2. Install the dependencies:
```bash
$ pip install -r requirements.txt
```

3. Setup environment variables with credentails:
```bash
$ export AUTOMATION_USER="admin"
$ export AUTOMATION_PASS="admin"
```

4. Launch the app:
```bash
$ cd app
$ python main.py 
Device 192.168.101.11 supports ping via NETCONF
==================================================================================================================================
Reachability to 192.168.101.11
==================================================================================================================================
  statistics:
    packets:
      sent: 3
      received: 3
      loss: 0.0
    round-trip-time:
      minimum: 1445
      average: 2360
      maximum: 3879
      standard-deviation: 1081
```

# Want to Know Network Automation
[Enroll to out training programs](http://bit.ly/2mP3SJy)

(c) 2022, Karneliuk.com