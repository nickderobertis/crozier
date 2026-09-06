

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_search_match import LogSearchMatch


class LogSearchResponse(UniversalBaseModel):
    files_searched: typing.Optional[typing.List[str]] = None
    matches: typing.Optional[typing.List[LogSearchMatch]] = None
    query: typing.Optional[str] = None
    truncated: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
