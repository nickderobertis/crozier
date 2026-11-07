

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permission_set_with_requirement_permission_set import PermissionSetWithRequirementPermissionSet
from .permission_set_with_requirement_requirement_type import PermissionSetWithRequirementRequirementType


class PermissionSetWithRequirement(UniversalBaseModel):
    permission_set: PermissionSetWithRequirementPermissionSet
    requirement_type: PermissionSetWithRequirementRequirementType = pydantic.Field()
    """
    Whether this permission set is mandatory or optional for the agent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
