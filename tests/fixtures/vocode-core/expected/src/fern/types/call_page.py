

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .normalized_call import NormalizedCall


class CallPage(UniversalBaseModel):
    items: typing.List[NormalizedCall]
    page: int
    size: int
    has_more: bool
    total: int
    total_is_estimated: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
