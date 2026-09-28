

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_curve import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurve,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolation,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_points_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathPointsItem,
)


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPath(UniversalBaseModel):
    path_id: typing_extensions.Annotated[str, FieldMetadata(alias="pathId"), pydantic.Field(alias="pathId")]
    points: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathPointsItem]
    ] = None
    width: typing.Optional[float] = None
    opacity: typing.Optional[float] = None
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
