

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .async_search_status_dto_search_job_status import AsyncSearchStatusDtoSearchJobStatus


class AsyncSearchStatusDto(UniversalBaseModel):
    search_job_status: typing_extensions.Annotated[
        AsyncSearchStatusDtoSearchJobStatus,
        FieldMetadata(alias="searchJobStatus"),
        pydantic.Field(alias="searchJobStatus"),
    ]
    expiration_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expirationDate"),
        pydantic.Field(
            alias="expirationDate", description="When the search job will expire and be automatically deleted"
        ),
    ]
    """
    When the search job will expire and be automatically deleted
    """

    entities_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="entitiesCount"),
        pydantic.Field(alias="entitiesCount", description="Number of entities found by the search"),
    ]
    """
    Number of entities found by the search
    """

    calculation_time_millis: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="calculationTimeMillis"),
        pydantic.Field(
            alias="calculationTimeMillis", description="Time taken to calculate the search job in milliseconds"
        ),
    ]
    """
    Time taken to calculate the search job in milliseconds
    """

    create_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="When the search job was initiated"),
    ]
    """
    When the search job was initiated
    """

    finish_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="finishTime"),
        pydantic.Field(alias="finishTime", description="When the search job completed (null if still running)"),
    ] = None
    """
    When the search job completed (null if still running)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
