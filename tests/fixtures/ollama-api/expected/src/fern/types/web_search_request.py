

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebSearchRequest(UniversalBaseModel):
    query: str = pydantic.Field()
    """
    Search query string
    """

    max_results: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of results to return
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
