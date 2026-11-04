

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_submission_content_type import ContentSubmissionContentType
from .content_submission_status import ContentSubmissionStatus


class ContentSubmission(UniversalBaseModel):
    id: str
    content_type: typing_extensions.Annotated[
        ContentSubmissionContentType, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ]
    content_id: typing_extensions.Annotated[str, FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId")]
    content_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentName"), pydantic.Field(alias="contentName")
    ] = None
    working_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="workingRevision"), pydantic.Field(alias="workingRevision")
    ]
    snapshot: typing.Dict[str, typing.Any]
    snapshot_sha256: typing_extensions.Annotated[
        str, FieldMetadata(alias="snapshotSha256"), pydantic.Field(alias="snapshotSha256")
    ]
    submitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submittedBy"), pydantic.Field(alias="submittedBy")
    ] = None
    submitter_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submitterName"), pydantic.Field(alias="submitterName")
    ] = None
    submitted_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="submittedAt"), pydantic.Field(alias="submittedAt")
    ]
    based_published_revision: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="basedPublishedRevision"),
        pydantic.Field(alias="basedPublishedRevision"),
    ] = None
    based_published_revision_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="basedPublishedRevisionId"),
        pydantic.Field(alias="basedPublishedRevisionId"),
    ] = None
    status: ContentSubmissionStatus
    review_required: typing_extensions.Annotated[
        bool, FieldMetadata(alias="reviewRequired"), pydantic.Field(alias="reviewRequired")
    ]
    allow_self_approval: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowSelfApproval"), pydantic.Field(alias="allowSelfApproval")
    ]
    review_note: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reviewNote"), pydantic.Field(alias="reviewNote")
    ] = None
    reviewed_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reviewedBy"), pydantic.Field(alias="reviewedBy")
    ] = None
    reviewer_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reviewerName"), pydantic.Field(alias="reviewerName")
    ] = None
    reviewed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="reviewedAt"), pydantic.Field(alias="reviewedAt")
    ] = None
    requested_publication_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="requestedPublicationAt"),
        pydantic.Field(alias="requestedPublicationAt"),
    ] = None
    publication_failure_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publicationFailureReason"),
        pydantic.Field(alias="publicationFailureReason"),
    ] = None
    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ] = None
    newer_working_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="newerWorkingDraft"), pydantic.Field(alias="newerWorkingDraft")
    ] = None
    current_published_revision: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentPublishedRevision"),
        pydantic.Field(alias="currentPublishedRevision"),
    ] = None
    affected_screen_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="affectedScreenCount"), pydantic.Field(alias="affectedScreenCount")
    ] = None
    affected_location_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="affectedLocationCount"),
        pydantic.Field(alias="affectedLocationCount"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
