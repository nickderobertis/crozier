

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1role_scopes_item import V1RoleScopesItem


class V1Role(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the role
    """

    name: str = pydantic.Field()
    """
    Internal role name (admin, manager, employee, team_lead)
    """

    display_name: str = pydantic.Field()
    """
    Human-readable role name
    """

    description: str = pydantic.Field()
    """
    Description of the role permissions and capabilities
    """

    scopes: typing.List[V1RoleScopesItem] = pydantic.Field()
    """
    Configurable permission scopes for this role
    """

    default: bool = pydantic.Field()
    """
    Whether this is the default role for new users
    """

    allowed_to_invite: bool = pydantic.Field()
    """
    Whether users with this role can invite new members
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
