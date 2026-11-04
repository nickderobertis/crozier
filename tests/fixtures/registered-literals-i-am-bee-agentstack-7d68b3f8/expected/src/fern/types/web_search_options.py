

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .web_search_options_search_context_size import WebSearchOptionsSearchContextSize
from .web_search_options_user_location import WebSearchOptionsUserLocation


class WebSearchOptions(UniversalBaseModel):
    """
    This tool searches the web for relevant results to use in a response.
    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).
    """

    search_context_size: typing.Optional[WebSearchOptionsSearchContextSize] = None
    user_location: typing.Optional[WebSearchOptionsUserLocation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
