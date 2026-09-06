

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LogSearchMatch(UniversalBaseModel):
    context_after: typing.Optional[typing.List[str]] = None
    context_before: typing.Optional[typing.List[str]] = None
    file: typing.Optional[str] = None
    line: typing.Optional[int] = None
    text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
