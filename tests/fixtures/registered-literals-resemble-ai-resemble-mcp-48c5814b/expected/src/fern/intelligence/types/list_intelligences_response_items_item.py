

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_intelligences_response_items_item_media_type import ListIntelligencesResponseItemsItemMediaType


class ListIntelligencesResponseItemsItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The AI-generated intelligence analysis
    """

    created_at: typing.Optional[dt.datetime] = None
    detect_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the associated detect object
    """

    media_type: typing.Optional[ListIntelligencesResponseItemsItemMediaType] = pydantic.Field(default=None)
    """
    Type of media analyzed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
