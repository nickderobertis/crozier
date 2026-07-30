

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_source import JobSource
from .job_status import JobStatus


class Job(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique job identifier
    """

    source: JobSource = pydantic.Field()
    """
    Job source type
    """

    project: str = pydantic.Field()
    """
    Project name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Build description
    """

    platform: str = pydantic.Field()
    """
    Target platform (e.g., windows, linux, macos)
    """

    status: JobStatus = pydantic.Field()
    """
    Current job status
    """

    build_step: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="buildStep"),
        pydantic.Field(alias="buildStep", description="Current build processing step"),
    ]
    """
    Current build processing step
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 timestamp when job was created"),
    ]
    """
    ISO 8601 timestamp when job was created
    """

    ingest_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ingestPath"),
        pydantic.Field(alias="ingestPath", description="Relative path to build files within /builds directory"),
    ]
    """
    Relative path to build files within /builds directory
    """

    steam_channel_labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Steam channels to upload to
    """

    cdn_channel_labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    CDN channels to upload to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
