

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .externalized_function_config_dto import ExternalizedFunctionConfigDto
from .query_condition_dto import QueryConditionDto


class ExternalizedFunctionDto(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the function that returns boolean
    """

    config: typing.Optional[ExternalizedFunctionConfigDto] = None
    criterion: typing.Optional[QueryConditionDto] = pydantic.Field(default=None)
    """
    Optional criterion to check before calling an expensive function, used when the result can be confidently determined from entity data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
