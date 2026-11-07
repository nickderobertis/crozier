

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ccdl import Ccdl
from .query_result import QueryResult


class Query(UniversalBaseModel):
    id: int
    content: Ccdl
    label: typing.Optional[str] = None
    results: typing.Optional[QueryResult] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
