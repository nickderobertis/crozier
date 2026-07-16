

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_comment_summary import ContentCommentSummary
from .content_content_representation import ContentContentRepresentation
from .user_general_user import UserGeneralUser


class ContentContentItemPublicContract(UniversalBaseModel):
    allow_comments: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowComments"), pydantic.Field(alias="allowComments")
    ] = None
    author: typing.Optional[UserGeneralUser] = None
    auto_english_property_fallback: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoEnglishPropertyFallback"),
        pydantic.Field(alias="autoEnglishPropertyFallback"),
    ] = None
    c_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cType"), pydantic.Field(alias="cType")
    ] = None
    cms_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cmsPath"), pydantic.Field(alias="cmsPath")
    ] = None
    comment_summary: typing_extensions.Annotated[
        typing.Optional[ContentCommentSummary],
        FieldMetadata(alias="commentSummary"),
        pydantic.Field(alias="commentSummary"),
    ] = None
    content_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId")
    ] = None
    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="creationDate"), pydantic.Field(alias="creationDate")
    ] = None
    has_age_gate: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasAgeGate"), pydantic.Field(alias="hasAgeGate")
    ] = None
    minimum_age: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minimumAge"), pydantic.Field(alias="minimumAge")
    ] = None
    modify_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modifyDate"), pydantic.Field(alias="modifyDate")
    ] = None
    properties: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.
    As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.
    """

    rating_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ratingImagePath"), pydantic.Field(alias="ratingImagePath")
    ] = None
    representations: typing.Optional[typing.List[ContentContentRepresentation]] = None
    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    NOTE: Tags will always be lower case.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
