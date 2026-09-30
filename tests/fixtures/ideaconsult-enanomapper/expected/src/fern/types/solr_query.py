

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SolrQuery(UniversalBaseModel):
    facet: typing.Optional[str] = None
    filter: typing.Optional[str] = None
    query: typing.Optional[str] = None
    rows: typing.Optional[int] = None
    sort: typing.Optional[bool] = None
    start: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
