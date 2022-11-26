## Tree of Operational Module
Built using `pyang`:
```
module: nokia-oper-global
  +--ro global-operations
     +---x md-cli-raw-command
     |  +---w input
     |  |  +---w md-cli-input-line    string
     |  +--ro output
     |     +--ro operation-id?      types-operation:operation-id
     |     +--ro start-time?        types-operation:operation-timestamp
     |     +--ro results-path?      types-operation:operation-path
     |     +--ro results
     |     |  +--ro md-cli-output-block?   string
     |     +--ro status?            types-operation:operation-status
     |     +--ro error-message*     types-operation:operation-message
     |     +--ro warning-message*   types-operation:operation-message
     |     +--ro info-message*      types-operation:operation-message
     |     +--ro end-time?          types-operation:operation-timestamp
     +---x md-compare
     |  +---w input
     |  |  +---w path
     |  |  |  +---w (path-type)?
     |  |  |     +--:(subtree-path)
     |  |  |        +---w subtree-path?   <anyxml>
     |  |  +---w configuration-region?   types-sros:configuration-region
     |  |  +---w source
     |  |  |  +---w (destination-type)?
     |  |  |     +--:(candidate)
     |  |  |     |  +---w candidate?   empty
     |  |  |     +--:(baseline)
     |  |  |     |  +---w baseline?    empty
     |  |  |     +--:(url)
     |  |  |     |  +---w url?         string
     |  |  |     +--:(running)
     |  |  |     |  +---w running?     empty
     |  |  |     +--:(startup)
     |  |  |     |  +---w startup?     empty
     |  |  |     +--:(booted)
     |  |  |     |  +---w booted?      empty
     |  |  |     +--:(rollback)
     |  |  |        +---w rollback
     |  |  |           +---w checkpoint-id?   uint32
     |  |  +---w destination
     |  |  |  +---w (destination-type)?
     |  |  |     +--:(candidate)
     |  |  |     |  +---w candidate?   empty
     |  |  |     +--:(baseline)
     |  |  |     |  +---w baseline?    empty
     |  |  |     +--:(url)
     |  |  |     |  +---w url?         string
     |  |  |     +--:(running)
     |  |  |     |  +---w running?     empty
     |  |  |     +--:(startup)
     |  |  |     |  +---w startup?     empty
     |  |  |     +--:(booted)
     |  |  |     |  +---w booted?      empty
     |  |  |     +--:(rollback)
     |  |  |        +---w rollback
     |  |  |           +---w checkpoint-id?   uint32
     |  |  +---w format?                 enumeration
     |  +--ro output
     |     +--ro operation-id?      types-operation:operation-id
     |     +--ro start-time?        types-operation:operation-timestamp
     |     +--ro results-path?      types-operation:operation-path
     |     +--ro results
     |     |  +--ro md-compare-output?   string
     |     +--ro status?            types-operation:operation-status
     |     +--ro error-message*     types-operation:operation-message
     |     +--ro warning-message*   types-operation:operation-message
     |     +--ro info-message*      types-operation:operation-message
     |     +--ro end-time?          types-operation:operation-timestamp
     +--ro oam
     |  +--ro eth-cfm
     |  |  +---x linktrace
     |  |  |  +---w input
     |  |  |  |  +---w asynchronous?        types-operation:operation-asynchronous
     |  |  |  |  +---w retention-timeout?   types-operation:operation-timeout
     |  |  |  |  +---w destination          union
     |  |  |  |  +---w md-admin-name        -> /state:state/eth-cfm/domain/md-admin-name
     |  |  |  |  +---w ma-admin-name        -> /state:state/eth-cfm/domain[state:md-admin-name=current()/../md-admin-name]/association/ma-admin-name
     |  |  |  |  +---w mep-id               types-eth-cfm:mep-id-type
     |  |  |  |  +---w ttl?                 uint32
     |  |  |  +--ro output
     |  |  |     +--ro operation-id?      types-operation:operation-id
     |  |  |     +--ro start-time?        types-operation:operation-timestamp
     |  |  |     +--ro results-path?      types-operation:operation-path
     |  |  |     +--ro status?            types-operation:operation-status
     |  |  |     +--ro error-message*     types-operation:operation-message
     |  |  |     +--ro warning-message*   types-operation:operation-message
     |  |  |     +--ro info-message*      types-operation:operation-message
     |  |  |     +--ro end-time?          types-operation:operation-timestamp
     |  |  +---x loopback
     |  |     +---w input
     |  |     |  +---w asynchronous?        types-operation:operation-asynchronous
     |  |     |  +---w execution-timeout?   types-operation:operation-timeout
     |  |     |  +---w retention-timeout?   types-operation:operation-timeout
     |  |     |  +---w destination          union
     |  |     |  +---w md-admin-name        -> /state:state/eth-cfm/domain/md-admin-name
     |  |     |  +---w ma-admin-name        -> /state:state/eth-cfm/domain[state:md-admin-name=current()/../md-admin-name]/association/ma-admin-name
     |  |     |  +---w mep-id               types-eth-cfm:mep-id-type
     |  |     |  +---w send-count?          int32
     |  |     |  +---w size?                uint32
     |  |     |  +---w priority?            int32
     |  |     |  +---w lbm-padding?         uint32
     |  |     |  +---w timeout?             uint32
     |  |     |  +---w interval?            uint32
     |  |     +--ro output
     |  |        +--ro operation-id?      types-operation:operation-id
     |  |        +--ro start-time?        types-operation:operation-timestamp
     |  |        +--ro results-path?      types-operation:operation-path
     |  |        +--ro status?            types-operation:operation-status
     |  |        +--ro error-message*     types-operation:operation-message
     |  |        +--ro warning-message*   types-operation:operation-message
     |  |        +--ro info-message*      types-operation:operation-message
     |  |        +--ro end-time?          types-operation:operation-timestamp
     |  +--ro saa
     |  |  +--ro owner* [owner-name test]
     |  |     +--ro owner-name    -> /state:state/saa/owner[state:test=current()/../../owner/test]/owner-name
     |  |     +--ro test          -> /state:state/saa/owner[state:owner-name=current()/../../owner/owner-name]/test
     |  |     +---x start
     |  |     |  +---w input
     |  |     |  |  +---w accounting?   boolean
     |  |     |  +--ro output
     |  |     |     +--ro operation-id?      types-operation:operation-id
     |  |     |     +--ro start-time?        types-operation:operation-timestamp
     |  |     |     +--ro results-path?      types-operation:operation-path
     |  |     |     +--ro status?            types-operation:operation-status
     |  |     |     +--ro error-message*     types-operation:operation-message
     |  |     |     +--ro warning-message*   types-operation:operation-message
     |  |     |     +--ro info-message*      types-operation:operation-message
     |  |     |     +--ro end-time?          types-operation:operation-timestamp
     |  |     +---x stop
     |  |        +---w input
     |  |        |  +---w accounting?   boolean
     |  |        +--ro output
     |  |           +--ro operation-id?      types-operation:operation-id
     |  |           +--ro start-time?        types-operation:operation-timestamp
     |  |           +--ro results-path?      types-operation:operation-path
     |  |           +--ro status?            types-operation:operation-status
     |  |           +--ro error-message*     types-operation:operation-message
     |  |           +--ro warning-message*   types-operation:operation-message
     |  |           +--ro info-message*      types-operation:operation-message
     |  |           +--ro end-time?          types-operation:operation-timestamp
     |  +--ro service-activation-testhead
     |     +--ro service-test* [service-test-name]
     |        +--ro service-test-name    -> /state:state/test-oam/service-activation-testhead/service-test/test-name
     |        +---x start
     |        |  +--ro output
     |        |     +--ro operation-id?      types-operation:operation-id
     |        |     +--ro start-time?        types-operation:operation-timestamp
     |        |     +--ro results-path?      types-operation:operation-path
     |        |     +--ro status?            types-operation:operation-status
     |        |     +--ro error-message*     types-operation:operation-message
     |        |     +--ro warning-message*   types-operation:operation-message
     |        |     +--ro info-message*      types-operation:operation-message
     |        |     +--ro end-time?          types-operation:operation-timestamp
     |        +---x stop
     |           +--ro output
     |              +--ro operation-id?      types-operation:operation-id
     |              +--ro start-time?        types-operation:operation-timestamp
     |              +--ro results-path?      types-operation:operation-path
     |              +--ro status?            types-operation:operation-status
     |              +--ro error-message*     types-operation:operation-message
     |              +--ro warning-message*   types-operation:operation-message
     |              +--ro info-message*      types-operation:operation-message
     |              +--ro end-time?          types-operation:operation-timestamp
     +---x ping
     |  +---w input
     |  |  +---w destination               union
     |  |  +---w (routing-options)?
     |  |  |  +--:(case-bypass-routing)
     |  |  |  |  +---w bypass-routing?     empty
     |  |  |  +--:(case-interface)
     |  |  |  |  +---w interface?          types-sros:interface-name
     |  |  |  +--:(case-next-hop)
     |  |  |  |  +---w next-hop-address?   types-sros:ip-address
     |  |  |  +--:(case-subscriber)
     |  |  |     +---w subscriber?         types-submgt:subscriber-id
     |  |  +---w count?                    uint32
     |  |  +---w output-format?            enumeration
     |  |  +---w do-not-fragment?          empty
     |  |  +---w fc?                       types-sros:fc-name
     |  |  +---w interval?                 union
     |  |  +---w pattern?                  union
     |  |  +---w router-instance?          string
     |  |  +---w size?                     uint32
     |  |  +---w source-address?           types-sros:ip-address
     |  |  +---w timeout?                  uint32
     |  |  +---w tos?                      uint32
     |  |  +---w ttl?                      uint32
     |  +--ro output
     |     +--ro operation-id?      types-operation:operation-id
     |     +--ro start-time?        types-operation:operation-timestamp
     |     +--ro results-path?      types-operation:operation-path
     |     +--ro results
     |     |  +--ro test-parameters
     |     |  |  +--ro destination?              union
     |     |  |  +--ro (routing-options)?
     |     |  |  |  +--:(case-bypass-routing)
     |     |  |  |  |  +--ro bypass-routing?     boolean
     |     |  |  |  +--:(case-interface)
     |     |  |  |  |  +--ro interface?          types-sros:interface-name
     |     |  |  |  +--:(case-next-hop)
     |     |  |  |  |  +--ro next-hop-address?   types-sros:ip-address
     |     |  |  |  +--:(case-subscriber)
     |     |  |  |     +--ro subscriber?         types-submgt:subscriber-id
     |     |  |  +--ro count?                    uint32
     |     |  |  +--ro output-format?            enumeration
     |     |  |  +--ro do-not-fragment?          boolean
     |     |  |  +--ro fc?                       types-sros:fc-name
     |     |  |  +--ro interval?                 union
     |     |  |  +--ro pattern?                  union
     |     |  |  +--ro router-instance?          types-sros:router-instance-base-management-vprn-loose
     |     |  |  +--ro size?                     uint32
     |     |  |  +--ro source-address?           types-sros:ip-address
     |     |  |  +--ro timeout?                  uint32
     |     |  |  +--ro tos?                      uint32
     |     |  |  +--ro ttl?                      uint32
     |     |  +--ro probe* [probe-index]
     |     |  |  +--ro probe-index        uint32
     |     |  |  +--ro status?            types-oam:response-status
     |     |  |  +--ro round-trip-time?   uint32
     |     |  |  +--ro response-packet
     |     |  |     +--ro size?                   uint32
     |     |  |     +--ro source-address?         types-sros:ip-address-with-zone
     |     |  |     +--ro icmp-sequence-number?   uint32
     |     |  |     +--ro ttl?                    uint32
     |     |  +--ro summary
     |     |     +--ro statistics
     |     |        +--ro packets
     |     |        |  +--ro sent?       uint32
     |     |        |  +--ro received?   uint32
     |     |        |  +--ro loss?       decimal64
     |     |        +--ro round-trip-time
     |     |           +--ro minimum?              uint32
     |     |           +--ro average?              uint32
     |     |           +--ro maximum?              uint32
     |     |           +--ro standard-deviation?   uint32
     |     +--ro status?            types-operation:operation-status
     |     +--ro error-message*     types-operation:operation-message
     |     +--ro warning-message*   types-operation:operation-message
     |     +--ro info-message*      types-operation:operation-message
     |     +--ro end-time?          types-operation:operation-timestamp
     +---x traceroute
        +---w input
        |  +---w destination            union
        |  +---w decode?                enumeration
        |  +---w dest-port?             uint32
        |  +---w dest-port-udp-fixed?   empty
        |  +---w detail?                empty
        |  +---w min-ttl?               uint32
        |  +---w ttl?                   uint32
        |  +---w numeric?               empty
        |  +---w probe-count?           uint32
        |  +---w protocol?              enumeration
        |  +---w router-instance?       string
        |  +---w size?                  uint32
        |  +---w source-address?        types-sros:ip-address
        |  +---w tos?                   uint32
        |  +---w wait?                  uint32
        +--ro output
           +--ro operation-id?      types-operation:operation-id
           +--ro start-time?        types-operation:operation-timestamp
           +--ro results-path?      types-operation:operation-path
           +--ro results
           |  +--ro test-parameters
           |  |  +--ro destination?           union
           |  |  +--ro decode?                enumeration
           |  |  +--ro dest-port?             uint32
           |  |  +--ro dest-port-udp-fixed?   boolean
           |  |  +--ro detail?                boolean
           |  |  +--ro min-ttl?               uint32
           |  |  +--ro ttl?                   uint32
           |  |  +--ro numeric?               boolean
           |  |  +--ro probe-count?           uint32
           |  |  +--ro protocol?              enumeration
           |  |  +--ro router-instance?       types-sros:router-instance-base-management-vprn-loose
           |  |  +--ro size?                  uint32
           |  |  +--ro source-address?        types-sros:ip-address
           |  |  +--ro tos?                   uint32
           |  |  +--ro wait?                  uint32
           |  +--ro hop* [hop-index]
           |     +--ro hop-index    uint32
           |     +--ro probe* [probe-index]
           |        +--ro probe-index        uint32
           |        +--ro status?            types-oam:response-status
           |        +--ro round-trip-time?   uint32
           |        +--ro size?              uint32
           |        +--ro response-packet
           |           +--ro icmp-type?                uint32
           |           +--ro icmp-code?                uint32
           |           +--ro mtu-exceeded?             uint32
           |           +--ro source-address?           types-sros:ip-address
           |           +--ro source-host-name?         string
           |           +--ro tcp-port-status?          enumeration
           |           +--ro mpls-label-stack-entry* [index]
           |           |  +--ro index              uint32
           |           |  +--ro label?             types-sros:mpls-label-full-range
           |           |  +--ro traffic-class?     uint32
           |           |  +--ro bottom-of-stack?   uint32
           |           |  +--ro ttl?               uint32
           |           +--ro original-datagram
           |              +--ro header* [header-index]
           |                 +--ro header-index         uint32
           |                 +--ro (header-type-choice)?
           |                    +--:(ipv6-case)
           |                    |  +--ro ipv6-header
           |                    |     +--ro destination-address?   types-sros:ip-address
           |                    |     +--ro dscp?                  types-sros:named-item-or-empty
           |                    |     +--ro hop-limit?             uint32
           |                    |     +--ro source-address?        types-sros:ip-address
           |                    +--:(srv6-case)
           |                       +--ro srv6-header
           |                          +--ro segments-left?   uint32
           |                          +--ro segment-list* [segment-index]
           |                             +--ro segment-index      uint32
           |                             +--ro segment-address?   types-sros:ip-address
           +--ro status?            types-operation:operation-status
           +--ro error-message*     types-operation:operation-message
           +--ro warning-message*   types-operation:operation-message
           +--ro info-message*      types-operation:operation-message
           +--ro end-time?          types-operation:operation-timestamp
```