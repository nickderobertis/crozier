

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .next_page import NextPage
from .previous_page import PreviousPage


class Paging(UniversalBaseModel):
    next: typing.Optional[NextPage] = None
    prev: typing.Optional[PreviousPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
