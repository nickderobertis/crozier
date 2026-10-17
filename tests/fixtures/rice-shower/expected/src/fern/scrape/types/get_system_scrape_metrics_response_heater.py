

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_system_scrape_metrics_response_heater_error_count_item import (
    GetSystemScrapeMetricsResponseHeaterErrorCountItem,
)


class GetSystemScrapeMetricsResponseHeater(UniversalBaseModel):
    """
    Scraping metrics for heater data
    """

    last_error: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastError"),
        pydantic.Field(
            alias="lastError", description="Timestamp of the last error, or null if no errors have occurred"
        ),
    ] = None
    """
    Timestamp of the last error, or null if no errors have occurred
    """

    error_count: typing_extensions.Annotated[
        typing.List[GetSystemScrapeMetricsResponseHeaterErrorCountItem],
        FieldMetadata(alias="errorCount"),
        pydantic.Field(alias="errorCount"),
    ]
    success_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="successCount"),
        pydantic.Field(alias="successCount", description="Total number of successful scrapes"),
    ]
    """
    Total number of successful scrapes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
