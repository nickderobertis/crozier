

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_job_timeseries_data_response_items_item import InsightsGetJobTimeseriesDataResponseItemsItem


class InsightsGetJobTimeseriesDataResponse(UniversalBaseModel):
    """
    Project level timeseries metrics response
    """

    next_page_token: str = pydantic.Field()
    """
    A token to pass as a `page-token` query parameter to return the next page of results.
    """

    items: typing.List[InsightsGetJobTimeseriesDataResponseItemsItem] = pydantic.Field()
    """
    Aggregate metrics for a workflow at a time granularity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
