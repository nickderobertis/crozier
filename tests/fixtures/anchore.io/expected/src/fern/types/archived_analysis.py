

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archived_analysis_status import ArchivedAnalysisStatus
from .tag_entry import TagEntry


class ArchivedAnalysis(UniversalBaseModel):
    analyzed_at: typing.Optional[dt.datetime] = None
    annotations: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User provided annotations as key-value pairs
    """

    archive_size_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size, in bytes, of the analysis archive file
    """

    created_at: typing.Optional[dt.datetime] = None
    image_digest: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageDigest"),
        pydantic.Field(
            alias="imageDigest",
            description="The image digest (digest of the manifest describing the image, per docker spec)",
        ),
    ] = None
    """
    The image digest (digest of the manifest describing the image, per docker spec)
    """

    image_detail: typing.Optional[typing.List[TagEntry]] = pydantic.Field(default=None)
    """
    List of tags associated with the image digest
    """

    last_updated: typing.Optional[dt.datetime] = None
    parent_digest: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentDigest"),
        pydantic.Field(alias="parentDigest", description="The digest of a parent manifest (for manifest-list images)"),
    ] = None
    """
    The digest of a parent manifest (for manifest-list images)
    """

    status: typing.Optional[ArchivedAnalysisStatus] = pydantic.Field(default=None)
    """
    The archival status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
