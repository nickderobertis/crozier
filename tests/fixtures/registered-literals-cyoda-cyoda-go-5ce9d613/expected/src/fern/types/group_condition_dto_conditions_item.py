

from __future__ import annotations

import typing

from .array_condition_dto import ArrayConditionDto
from .lifecycle_condition_dto import LifecycleConditionDto
from .simple_condition_dto import SimpleConditionDto

if typing.TYPE_CHECKING:
    from .group_condition_dto import GroupConditionDto
GroupConditionDtoConditionsItem = typing.Union[
    ArrayConditionDto, "GroupConditionDto", LifecycleConditionDto, SimpleConditionDto
]
