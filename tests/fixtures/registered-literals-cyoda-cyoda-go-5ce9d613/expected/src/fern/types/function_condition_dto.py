

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .externalized_function_dto import ExternalizedFunctionDto
from .query_condition_dto import QueryConditionDto


class FunctionConditionDto(QueryConditionDto):
    function: ExternalizedFunctionDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
