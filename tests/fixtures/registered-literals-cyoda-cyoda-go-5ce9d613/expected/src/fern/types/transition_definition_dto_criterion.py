

import typing

from .array_condition_dto import ArrayConditionDto
from .function_condition_dto import FunctionConditionDto
from .group_condition_dto import GroupConditionDto
from .lifecycle_condition_dto import LifecycleConditionDto
from .simple_condition_dto import SimpleConditionDto

TransitionDefinitionDtoCriterion = typing.Union[
    ArrayConditionDto, FunctionConditionDto, GroupConditionDto, LifecycleConditionDto, SimpleConditionDto
]
