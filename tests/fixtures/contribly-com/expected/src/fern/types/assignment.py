

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .media_usage import MediaUsage
from .tag import Tag


class Assignment(UniversalBaseModel):
    allows_anonymous_contributions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowsAnonymousContributions"),
        pydantic.Field(alias="allowsAnonymousContributions"),
    ] = None
    call_to_action: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="callToAction"),
        pydantic.Field(
            alias="callToAction",
            description="An optional call to action specific to this assignment. ie. Submit your snow pictures.",
        ),
    ] = None
    """
    An optional call to action specific to this assignment. ie. Submit your snow pictures.
    """

    cover: typing.Optional[MediaUsage] = None
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    embargo: typing.Optional[dt.datetime] = None
    ends: typing.Optional[dt.datetime] = None
    featured: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    media_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="mediaRequired"), pydantic.Field(alias="mediaRequired")
    ] = None
    moderator: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional credential id of the moderator who owns this particular assignment.
    """

    name: typing.Optional[str] = None
    open: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Helper value. Is this assignment currently open? Based on the value of the ends field.
    """

    receipt_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="receiptMessage"),
        pydantic.Field(
            alias="receiptMessage",
            description="An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.",
        ),
    ] = None
    """
    An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.
    """

    starts: typing.Optional[dt.datetime] = None
    tags: typing.Optional[typing.List[Tag]] = None
    url_words: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="urlWords"), pydantic.Field(alias="urlWords")
    ] = None
    web_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webUrl"), pydantic.Field(alias="webUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
