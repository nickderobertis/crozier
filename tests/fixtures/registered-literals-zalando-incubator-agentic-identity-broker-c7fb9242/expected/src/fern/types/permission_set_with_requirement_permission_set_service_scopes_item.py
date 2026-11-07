

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permission_set_with_requirement_permission_set_service_scopes_item_requirement_type import (
    PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType,
)


class PermissionSetWithRequirementPermissionSetServiceScopesItem(UniversalBaseModel):
    service_id: str = pydantic.Field()
    """
    OAuth2 service identifier
    """

    requirement_type: PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType = pydantic.Field()
    """
    Whether this service is mandatory or optional within the permission set. Raw scopes are intentionally omitted; the frontend uses this field to determine lock status (FR-007).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
