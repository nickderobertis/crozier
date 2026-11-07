

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_audio_source_tracings_response_items_item_results import ListAudioSourceTracingsResponseItemsItemResults


class ListAudioSourceTracingsResponseItemsItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    results: typing.Optional[ListAudioSourceTracingsResponseItemsItemResults] = None
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
