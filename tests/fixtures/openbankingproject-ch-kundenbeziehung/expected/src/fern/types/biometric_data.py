

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BiometricData(UniversalBaseModel):
    face_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="faceImage"),
        pydantic.Field(alias="faceImage", description="Base64-kodiertes Gesichtsbild"),
    ] = None
    """
    Base64-kodiertes Gesichtsbild
    """

    liveness_video: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="livenessVideo"),
        pydantic.Field(alias="livenessVideo", description="Liveness-Check Video"),
    ] = None
    """
    Liveness-Check Video
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
