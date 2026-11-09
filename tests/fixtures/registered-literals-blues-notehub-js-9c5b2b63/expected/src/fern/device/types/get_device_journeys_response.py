

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_device_journeys_response_journeys_item import GetDeviceJourneysResponseJourneysItem


class GetDeviceJourneysResponse(UniversalBaseModel):
    has_more: bool
    journeys: typing.List[GetDeviceJourneysResponseJourneysItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
