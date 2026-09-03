

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IdentificationDataBiometricData(UniversalBaseModel):
    """
    Biometrische Daten (wenn verfügbar)
    """

    face_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="faceImage"),
        pydantic.Field(alias="faceImage", description="Gesichtsbild (Base64)"),
    ] = None
    """
    Gesichtsbild (Base64)
    """

    liveness_score: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="livenessScore"),
        pydantic.Field(alias="livenessScore", description="Liveness-Check Score (0-1)"),
    ] = None
    """
    Liveness-Check Score (0-1)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
