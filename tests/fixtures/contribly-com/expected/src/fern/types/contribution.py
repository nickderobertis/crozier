

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assignment import Assignment
from .media_usage import MediaUsage
from .moderation_history_item import ModerationHistoryItem
from .place import Place
from .via import Via


class Contribution(UniversalBaseModel):
    assignment: typing.Optional[Assignment] = None
    attribution: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public attribution for this contribution. This will be the display name of the registered user or the contributor's first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.
    """

    body: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    headline: typing.Optional[str] = None
    id: typing.Optional[str] = None
    media_usages: typing_extensions.Annotated[
        typing.Optional[typing.List[MediaUsage]],
        FieldMetadata(alias="mediaUsages"),
        pydantic.Field(alias="mediaUsages"),
    ] = None
    moderation_history: typing_extensions.Annotated[
        typing.Optional[typing.List[ModerationHistoryItem]],
        FieldMetadata(alias="moderationHistory"),
        pydantic.Field(alias="moderationHistory"),
    ] = None
    place: typing.Optional[Place] = None
    url_words: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="urlWords"), pydantic.Field(alias="urlWords")
    ] = None
    via: typing.Optional[Via] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
