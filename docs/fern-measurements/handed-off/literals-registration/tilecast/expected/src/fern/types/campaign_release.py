

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_release_status import CampaignReleaseStatus
from .campaign_snapshot import CampaignSnapshot


class CampaignRelease(UniversalBaseModel):
    id: str
    campaign_id: typing_extensions.Annotated[str, FieldMetadata(alias="campaignId"), pydantic.Field(alias="campaignId")]
    release_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="releaseNumber"), pydantic.Field(alias="releaseNumber")
    ]
    submission_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="submissionId"), pydantic.Field(alias="submissionId")
    ] = None
    snapshot: CampaignSnapshot
    snapshot_sha256: typing_extensions.Annotated[
        str, FieldMetadata(alias="snapshotSha256"), pydantic.Field(alias="snapshotSha256")
    ]
    status: CampaignReleaseStatus
    based_release_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="basedReleaseId"), pydantic.Field(alias="basedReleaseId")
    ] = None
    published_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publishedBy"), pydantic.Field(alias="publishedBy")
    ] = None
    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ] = None
    requested_publication_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="requestedPublicationAt"),
        pydantic.Field(alias="requestedPublicationAt"),
    ] = None
    failure_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="failureReason"), pydantic.Field(alias="failureReason")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
