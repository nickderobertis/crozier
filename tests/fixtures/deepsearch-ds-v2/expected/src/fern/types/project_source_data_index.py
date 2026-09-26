

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .elastic_index_search_query_options import ElasticIndexSearchQueryOptions


class ProjectSourceDataIndex(UniversalBaseModel):
    index_key: str
    query_options: ElasticIndexSearchQueryOptions
    proj_key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
