

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .double_nested_list_schema import DoubleNestedListSchema
from .double_nested_map_schema import DoubleNestedMapSchema
from .double_nested_set_schema import DoubleNestedSetSchema
from .triple_nested_map_schema import TripleNestedMapSchema


class GetNestedCollectionsResponse(UniversalBaseModel):
    double_nested_list: typing.Optional[DoubleNestedListSchema] = None
    double_nested_set: typing.Optional[DoubleNestedSetSchema] = None
    double_nested_map: typing.Optional[DoubleNestedMapSchema] = None
    triple_nested_map: typing.Optional[TripleNestedMapSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
