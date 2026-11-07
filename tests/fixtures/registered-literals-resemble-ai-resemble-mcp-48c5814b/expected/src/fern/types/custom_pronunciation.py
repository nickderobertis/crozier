

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .custom_pronunciation_status import CustomPronunciationStatus


class CustomPronunciation(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="Unique identifier for the pronunciation"),
    ] = None
    """
    Unique identifier for the pronunciation
    """

    word: typing.Optional[str] = pydantic.Field(default=None)
    """
    The word or phrase this pronunciation applies to
    """

    status: typing.Optional[CustomPronunciationStatus] = pydantic.Field(default=None)
    """
    Processing status. Only "ready" pronunciations are applied during synthesis.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this pronunciation is active and will be applied during synthesis
    """

    audio_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the uploaded reference audio
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
