

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAllScrapeMetricsResponseItemHeaterErrorCountItem(UniversalBaseModel):
    id: float = pydantic.Field()
    """
    Channel number or pin number
    """

    count: float = pydantic.Field()
    """
    Number of errors for this channel/pin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
