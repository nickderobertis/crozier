

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .elastic_search_result_entry import ElasticSearchResultEntry


class ElasticSearchResult(UniversalBaseModel):
    total_hits: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalHits"), pydantic.Field(alias="totalHits")
    ] = None
    results: typing.Optional[typing.List[ElasticSearchResultEntry]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
