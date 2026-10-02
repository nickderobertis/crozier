

import typing

SiteMembershipMethod = typing.Union[
    typing.Literal["sso", "invite", "scim", "dashboard", "admin", "access_request"], typing.Any
]
