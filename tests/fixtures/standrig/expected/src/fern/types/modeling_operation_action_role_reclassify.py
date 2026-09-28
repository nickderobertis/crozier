

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_role_reclassify_expected_role import ModelingOperationActionRoleReclassifyExpectedRole
from .modeling_operation_action_role_reclassify_role import ModelingOperationActionRoleReclassifyRole


class ModelingOperationActionRoleReclassify(UniversalBaseModel):
    expected_role: typing_extensions.Annotated[
        ModelingOperationActionRoleReclassifyExpectedRole,
        FieldMetadata(alias="expectedRole"),
        pydantic.Field(alias="expectedRole"),
    ]
    role: ModelingOperationActionRoleReclassifyRole
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
