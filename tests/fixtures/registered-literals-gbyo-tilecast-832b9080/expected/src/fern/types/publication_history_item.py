

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .publication_history_item_method import PublicationHistoryItemMethod


class PublicationHistoryItem(UniversalBaseModel):
    id: str
    revision: int
    native_revision_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nativeRevisionId"), pydantic.Field(alias="nativeRevisionId")
    ] = None
    submission_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submissionId"), pydantic.Field(alias="submissionId")
    ] = None
    campaign_release_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="campaignReleaseId"), pydantic.Field(alias="campaignReleaseId")
    ] = None
    published_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publishedBy"), pydantic.Field(alias="publishedBy")
    ] = None
    publisher_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publisherName"), pydantic.Field(alias="publisherName")
    ] = None
    published_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ]
    supersedes_publication_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supersedesPublicationId"),
        pydantic.Field(alias="supersedesPublicationId"),
    ] = None
    method: PublicationHistoryItemMethod
    affected_screen_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="affectedScreenCount"), pydantic.Field(alias="affectedScreenCount")
    ]
    snapshot_sha256: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="snapshotSha256"), pydantic.Field(alias="snapshotSha256")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
