

import typing

IpAddressRoleLabel = typing.Union[
    typing.Literal["Loopback", "Secondary", "Anycast", "VIP", "VRRP", "HSRP", "GLBP", "CARP"], typing.Any
]
