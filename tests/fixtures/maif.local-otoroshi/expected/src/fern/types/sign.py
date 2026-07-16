

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sign_algo_settings import SignAlgoSettings
from .verification_settings import VerificationSettings


class Sign(UniversalBaseModel):
    """
    Strategy where signature and field values are verified, and then token si re-signed
    """

    algo_settings: typing_extensions.Annotated[SignAlgoSettings, FieldMetadata(alias="algoSettings")]
    type: str = pydantic.Field()
    """
    String with value Sign
    """

    verification_settings: typing_extensions.Annotated[
        VerificationSettings, FieldMetadata(alias="verificationSettings")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
