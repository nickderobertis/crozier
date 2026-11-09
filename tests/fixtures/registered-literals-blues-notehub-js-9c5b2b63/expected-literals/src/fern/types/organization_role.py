

import typing

OrganizationRole = typing.Union[
    typing.Literal["org_admin", "billing_manager", "project_creator", "org_member"], typing.Any
]
