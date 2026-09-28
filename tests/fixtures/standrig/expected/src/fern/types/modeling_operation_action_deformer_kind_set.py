

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_kind_set_kind import ModelingOperationActionDeformerKindSetKind
from .modeling_operation_action_deformer_kind_set_warp import ModelingOperationActionDeformerKindSetWarp


class ModelingOperationActionDeformerKindSet(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    kind: ModelingOperationActionDeformerKindSetKind
    warp: typing.Optional[ModelingOperationActionDeformerKindSetWarp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
