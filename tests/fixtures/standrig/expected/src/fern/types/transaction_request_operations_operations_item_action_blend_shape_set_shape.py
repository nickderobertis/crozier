

from __future__ import annotations

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
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_pins_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_shared_points_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_transform import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_warp import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_curve import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurve,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolation,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_curve import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurve,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolation,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_transform import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform,
)


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part(UniversalBaseModel):
    kind: typing.Literal["part"] = "part"
    transform: TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Deformer(UniversalBaseModel):
    kind: typing.Literal["deformer"] = "deformer"
    transform: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform] = (
        None
    )
    warp: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp] = None
    pins: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem]
    ] = None
    shared_points: typing_extensions.Annotated[
        typing.Optional[
            typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem]
        ],
        FieldMetadata(alias="sharedPoints"),
        pydantic.Field(alias="sharedPoints"),
    ] = None
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_ArtPath(UniversalBaseModel):
    kind: typing.Literal["art-path"] = "art-path"
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


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Glue(UniversalBaseModel):
    kind: typing.Literal["glue"] = "glue"
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
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransactionRequestOperationsOperationsItemActionBlendShapeSetShape = typing_extensions.Annotated[
    typing.Union[
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Deformer,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_ArtPath,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Glue,
    ],
    pydantic.Field(discriminator="kind"),
]
