

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_target_roles_item import ModelingOperationTargetRolesItem


class ModelingOperationTarget(UniversalBaseModel):
    roles: typing.Optional[typing.List[ModelingOperationTargetRolesItem]] = None
    part_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="partIds"), pydantic.Field(alias="partIds")
    ] = None
    deformer_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="deformerIds"), pydantic.Field(alias="deformerIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
