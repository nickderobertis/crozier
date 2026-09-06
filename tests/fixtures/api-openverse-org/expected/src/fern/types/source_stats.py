

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceStats(UniversalBaseModel):
    source_name: typing.Optional[str] = None
    display_name: typing.Optional[str] = None
    source_url: typing.Optional[str] = None
    logo_url: typing.Optional[str] = None
    media_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
