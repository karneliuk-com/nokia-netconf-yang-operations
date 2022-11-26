## RPC request:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <action xmlns="urn:ietf:params:xml:ns:yang:1">
        <global-operations xmlns="urn:nokia.com:sros:ns:yang:sr:oper-global">
            <ping>
                <destination>10.0.0.1</destination>
                <count>3</count>
            </ping>
        </global-operations>
    </action>
</rpc>
]]>]]>
```

## RPC response:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nokiaoper="urn:nokia.com:sros:ns:yang:sr:oper-global">
    <nokiaoper:operation-id>13</nokiaoper:operation-id>
    <nokiaoper:start-time>2022-11-20T21:21:15.0Z</nokiaoper:start-time>
    <nokiaoper:results>
        <nokiaoper:test-parameters>
            <nokiaoper:destination>10.0.0.1</nokiaoper:destination>
            <nokiaoper:count>3</nokiaoper:count>
            <nokiaoper:output-format>detail</nokiaoper:output-format>
            <nokiaoper:do-not-fragment>false</nokiaoper:do-not-fragment>
            <nokiaoper:fc>nc</nokiaoper:fc>
            <nokiaoper:interval>1</nokiaoper:interval>
            <nokiaoper:pattern>sequential</nokiaoper:pattern>
            <nokiaoper:router-instance>Base</nokiaoper:router-instance>
            <nokiaoper:size>56</nokiaoper:size>
            <nokiaoper:timeout>5</nokiaoper:timeout>
            <nokiaoper:tos>0</nokiaoper:tos>
            <nokiaoper:ttl>64</nokiaoper:ttl>
        </nokiaoper:test-parameters>
        <nokiaoper:probe>
            <nokiaoper:probe-index>1</nokiaoper:probe-index>
            <nokiaoper:status>response-received</nokiaoper:status>
            <nokiaoper:round-trip-time>3534</nokiaoper:round-trip-time>
            <nokiaoper:response-packet>
                <nokiaoper:size>64</nokiaoper:size>
                <nokiaoper:source-address>10.0.0.1</nokiaoper:source-address>
                <nokiaoper:icmp-sequence-number>1</nokiaoper:icmp-sequence-number>
                <nokiaoper:ttl>255</nokiaoper:ttl>
            </nokiaoper:response-packet>
        </nokiaoper:probe>
        <nokiaoper:probe>
            <nokiaoper:probe-index>2</nokiaoper:probe-index>
            <nokiaoper:status>response-received</nokiaoper:status>
            <nokiaoper:round-trip-time>1209</nokiaoper:round-trip-time>
            <nokiaoper:response-packet>
                <nokiaoper:size>64</nokiaoper:size>
                <nokiaoper:source-address>10.0.0.1</nokiaoper:source-address>
                <nokiaoper:icmp-sequence-number>2</nokiaoper:icmp-sequence-number>
                <nokiaoper:ttl>255</nokiaoper:ttl>
            </nokiaoper:response-packet>
        </nokiaoper:probe>
        <nokiaoper:probe>
            <nokiaoper:probe-index>3</nokiaoper:probe-index>
            <nokiaoper:status>response-received</nokiaoper:status>
            <nokiaoper:round-trip-time>2004</nokiaoper:round-trip-time>
            <nokiaoper:response-packet>
                <nokiaoper:size>64</nokiaoper:size>
                <nokiaoper:source-address>10.0.0.1</nokiaoper:source-address>
                <nokiaoper:icmp-sequence-number>3</nokiaoper:icmp-sequence-number>
                <nokiaoper:ttl>255</nokiaoper:ttl>
            </nokiaoper:response-packet>
        </nokiaoper:probe>
        <nokiaoper:summary>
            <nokiaoper:statistics>
                <nokiaoper:packets>
                    <nokiaoper:sent>3</nokiaoper:sent>
                    <nokiaoper:received>3</nokiaoper:received>
                    <nokiaoper:loss>0.0</nokiaoper:loss>
                </nokiaoper:packets>
                <nokiaoper:round-trip-time>
                    <nokiaoper:minimum>1209</nokiaoper:minimum>
                    <nokiaoper:average>2249</nokiaoper:average>
                    <nokiaoper:maximum>3534</nokiaoper:maximum>
                    <nokiaoper:standard-deviation>964</nokiaoper:standard-deviation>
                </nokiaoper:round-trip-time>
            </nokiaoper:statistics>
        </nokiaoper:summary>
    </nokiaoper:results>
    <nokiaoper:status>completed</nokiaoper:status>
    <nokiaoper:end-time>2022-11-20T21:21:17.2Z</nokiaoper:end-time>
</rpc-reply>
```