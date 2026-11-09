

import typing

from ...types.array_condition_dto import ArrayConditionDto
from ...types.function_condition_dto import FunctionConditionDto
from ...types.group_condition_dto import GroupConditionDto
from ...types.lifecycle_condition_dto import LifecycleConditionDto
from ...types.simple_condition_dto import SimpleConditionDto

SubmitAsyncSearchJobRequestBody = typing.Union[
    ArrayConditionDto, FunctionConditionDto, GroupConditionDto, LifecycleConditionDto, SimpleConditionDto
]
