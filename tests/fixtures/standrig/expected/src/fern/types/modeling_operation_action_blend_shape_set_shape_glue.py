

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_blend_shape_set_shape_glue_curve import (
    ModelingOperationActionBlendShapeSetShapeGlueCurve,
)
from .modeling_operation_action_blend_shape_set_shape_glue_interpolation import (
    ModelingOperationActionBlendShapeSetShapeGlueInterpolation,
)


class ModelingOperationActionBlendShapeSetShapeGlue(UniversalBaseModel):
    glue_id: typing_extensions.Annotated[str, FieldMetadata(alias="glueId"), pydantic.Field(alias="glueId")]
    strength: float
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionBlendShapeSetShapeGlueInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBlendShapeSetShapeGlueCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
