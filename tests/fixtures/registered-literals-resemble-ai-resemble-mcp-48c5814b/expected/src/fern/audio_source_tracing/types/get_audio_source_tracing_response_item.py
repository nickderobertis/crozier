

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_audio_source_tracing_response_item_results import GetAudioSourceTracingResponseItemResults


class GetAudioSourceTracingResponseItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    results: typing.Optional[GetAudioSourceTracingResponseItemResults] = None
    created_at: typing.Optional[dt.datetime] = None
    detect_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the associated detect object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
