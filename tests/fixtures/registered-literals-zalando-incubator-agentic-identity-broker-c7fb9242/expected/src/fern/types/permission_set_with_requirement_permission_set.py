

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permission_set_with_requirement_permission_set_service_scopes_item import (
    PermissionSetWithRequirementPermissionSetServiceScopesItem,
)


class PermissionSetWithRequirementPermissionSet(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Permission set identifier
    """

    name: str = pydantic.Field()
    """
    Permission set display name
    """

    description: str = pydantic.Field()
    """
    Permission set description
    """

    service_scopes: typing.List[PermissionSetWithRequirementPermissionSetServiceScopesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
