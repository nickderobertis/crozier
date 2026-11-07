

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .web_search_options_user_location_approximate import WebSearchOptionsUserLocationApproximate
from .web_search_options_user_location_type import WebSearchOptionsUserLocationType


class WebSearchOptionsUserLocation(UniversalBaseModel):
    """
    Approximate location parameters for the search.
    """

    approximate: WebSearchOptionsUserLocationApproximate
    type: WebSearchOptionsUserLocationType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
