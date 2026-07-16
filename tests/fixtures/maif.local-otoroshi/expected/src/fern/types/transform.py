

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transform_algo_settings import TransformAlgoSettings
from .transform_settings import TransformSettings
from .verification_settings import VerificationSettings


class Transform(UniversalBaseModel):
    """
    Strategy where signature and field values are verified, trasnformed and then token si re-signed
    """

    algo_settings: typing_extensions.Annotated[
        TransformAlgoSettings, FieldMetadata(alias="algoSettings"), pydantic.Field(alias="algoSettings")
    ]
    transform_settings: typing_extensions.Annotated[
        typing.Optional[TransformSettings],
        FieldMetadata(alias="transformSettings"),
        pydantic.Field(alias="transformSettings"),
    ] = None
    type: str = pydantic.Field()
    """
    String with value Transform
    """

    verification_settings: typing_extensions.Annotated[
        VerificationSettings, FieldMetadata(alias="verificationSettings"), pydantic.Field(alias="verificationSettings")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
