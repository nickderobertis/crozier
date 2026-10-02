

import typing

L2VpnTypeLabel = typing.Union[
    typing.Literal[
        "VPWS",
        "VPLS",
        "VXLAN",
        "VXLAN-EVPN",
        "MPLS EVPN",
        "PBB EVPN",
        "EPL",
        "EVPL",
        "Ethernet Private LAN",
        "Ethernet Virtual Private LAN",
        "Ethernet Private Tree",
        "Ethernet Virtual Private Tree",
    ],
    typing.Any,
]
