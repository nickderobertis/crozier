

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KeywordTriggerMetadata(UniversalBaseModel):
    keyword_filter: typing.Optional[typing.List[str]] = None
    regex_patterns: typing.Optional[typing.List[str]] = None
    allow_list: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
