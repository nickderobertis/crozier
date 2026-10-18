

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_all_scrape_metrics_response_item_heater import GetAllScrapeMetricsResponseItemHeater
from .get_all_scrape_metrics_response_item_thermo import GetAllScrapeMetricsResponseItemThermo


class GetAllScrapeMetricsResponseItem(UniversalBaseModel):
    system_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="systemId"), pydantic.Field(alias="systemId", description="System identifier")
    ]
    """
    System identifier
    """

    thermo: GetAllScrapeMetricsResponseItemThermo = pydantic.Field()
    """
    Scraping metrics for thermometer data
    """

    heater: GetAllScrapeMetricsResponseItemHeater = pydantic.Field()
    """
    Scraping metrics for heater data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
