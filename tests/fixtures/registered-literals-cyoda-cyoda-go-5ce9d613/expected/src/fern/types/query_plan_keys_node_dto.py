

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_plan_keys_node_dto_type import QueryPlanKeysNodeDtoType


class QueryPlanKeysNodeDto(UniversalBaseModel):
    type: typing.Optional[QueryPlanKeysNodeDtoType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
