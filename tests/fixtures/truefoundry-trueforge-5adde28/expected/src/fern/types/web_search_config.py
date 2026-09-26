

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebSearchConfig(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable built-in web search and fetch tools. Default: false (host must configure a provider).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
