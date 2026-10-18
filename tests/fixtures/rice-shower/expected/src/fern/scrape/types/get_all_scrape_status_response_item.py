

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_all_scrape_status_response_item_heater import GetAllScrapeStatusResponseItemHeater
from .get_all_scrape_status_response_item_thermo import GetAllScrapeStatusResponseItemThermo


class GetAllScrapeStatusResponseItem(UniversalBaseModel):
    system_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="systemId"), pydantic.Field(alias="systemId", description="System identifier")
    ]
    """
    System identifier
    """

    thermo: GetAllScrapeStatusResponseItemThermo
    heater: GetAllScrapeStatusResponseItemHeater
    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="UTC timestamp when this scraper was started"),
    ]
    """
    UTC timestamp when this scraper was started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
