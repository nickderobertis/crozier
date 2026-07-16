

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verification_settings import VerificationSettings


class PassThrough(UniversalBaseModel):
    """
    Strategy where only signature and field values are verified
    """

    type: str = pydantic.Field()
    """
    String with value PassThrough
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
