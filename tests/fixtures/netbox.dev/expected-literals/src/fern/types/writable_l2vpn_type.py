

import typing

WritableL2VpnType = typing.Union[
    typing.Literal[
        "vpws",
        "vpls",
        "vxlan",
        "vxlan-evpn",
        "mpls-evpn",
        "pbb-evpn",
        "epl",
        "evpl",
        "ep-lan",
        "evp-lan",
        "ep-tree",
        "evp-tree",
    ],
    typing.Any,
]
