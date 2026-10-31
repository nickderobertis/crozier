

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .complex_types_search_response_result_data_results_item import ComplexTypesSearchResponseResultDataResultsItem


class ComplexTypesSearchResponseResultData(UniversalBaseModel):
    results: typing.List[ComplexTypesSearchResponseResultDataResultsItem]
    total: float
    has_more: typing_extensions.Annotated[bool, FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
