

import typing

IpAddressRoleValue = typing.Union[
    typing.Literal["loopback", "secondary", "anycast", "vip", "vrrp", "hsrp", "glbp", "carp"], typing.Any
]
