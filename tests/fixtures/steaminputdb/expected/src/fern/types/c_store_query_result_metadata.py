

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .c_store_query_per_result_metadata import CStoreQueryPerResultMetadata


class CStoreQueryResultMetadata(UniversalBaseModel):
    count: typing.Optional[int] = None
    per_result_metadata: typing.Optional[typing.List[CStoreQueryPerResultMetadata]] = None
    spellcheck_suggestions: typing.Optional[typing.List[str]] = None
    start: typing.Optional[int] = None
    total_matching_records: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
