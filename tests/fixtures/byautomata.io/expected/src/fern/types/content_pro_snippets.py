

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContentProSnippets(UniversalBaseModel):
    description: typing.Optional[typing.List[str]] = None
    text: typing.Optional[typing.List[str]] = None
    title: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
