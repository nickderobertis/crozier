

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_part_contour_shade_shade_profile import (
    TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile,
)


class TransactionRequestOperationsOperationsItemActionPartContourShadeShade(UniversalBaseModel):
    color: str
    width: float
    strength: float
    axis_strength: typing_extensions.Annotated[
        float, FieldMetadata(alias="axisStrength"), pydantic.Field(alias="axisStrength")
    ]
    yaw_parameter: typing_extensions.Annotated[
        str, FieldMetadata(alias="yawParameter"), pydantic.Field(alias="yawParameter")
    ]
    pitch_parameter: typing_extensions.Annotated[
        str, FieldMetadata(alias="pitchParameter"), pydantic.Field(alias="pitchParameter")
    ]
    max_yaw: typing_extensions.Annotated[float, FieldMetadata(alias="maxYaw"), pydantic.Field(alias="maxYaw")]
    max_pitch: typing_extensions.Annotated[float, FieldMetadata(alias="maxPitch"), pydantic.Field(alias="maxPitch")]
    profile: typing.Optional[TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile] = None
    far_contour_fade: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="farContourFade"), pydantic.Field(alias="farContourFade")
    ] = None
    near_contour_fade: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="nearContourFade"), pydantic.Field(alias="nearContourFade")
    ] = None
    up_contour_fade: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="upContourFade"), pydantic.Field(alias="upContourFade")
    ] = None
    up_shadow_strength: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="upShadowStrength"), pydantic.Field(alias="upShadowStrength")
    ] = None
    line_width: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lineWidth"), pydantic.Field(alias="lineWidth")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
