

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_group_field_op import QueryGroupFieldOp


class QueryGroupField(UniversalBaseModel):
    module: str
    category: str
    fieldname: str
    op: QueryGroupFieldOp
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
