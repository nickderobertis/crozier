

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .async_job_status import AsyncJobStatus


class AsyncJob(UniversalBaseModel):
    """
    Model for AsyncJob
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Job creator"),
    ] = None
    """
    Job creator
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Creation timestamp"),
    ] = None
    """
    Creation timestamp
    """

    download_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadUri"),
        pydantic.Field(alias="downloadUri", description="Download URI"),
    ] = None
    """
    Download URI
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job ID
    """

    last_modified: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastModified"),
        pydantic.Field(alias="lastModified", description="Timestamp for last modified"),
    ] = None
    """
    Timestamp for last modified
    """

    record_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="recordCount"),
        pydantic.Field(alias="recordCount", description="Record Count"),
    ] = None
    """
    Record Count
    """

    status: typing.Optional[AsyncJobStatus] = pydantic.Field(default=None)
    """
    Job status
    """

    status_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statusUri"),
        pydantic.Field(alias="statusUri", description="Status URI"),
    ] = None
    """
    Status URI
    """

    time_taken: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeTaken"),
        pydantic.Field(alias="timeTaken", description="Time taken to complete the job"),
    ] = None
    """
    Time taken to complete the job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
