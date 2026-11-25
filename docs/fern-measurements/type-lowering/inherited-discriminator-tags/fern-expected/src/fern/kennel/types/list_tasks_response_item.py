

import typing

from ...types.grooming_task import GroomingTask
from ...types.walking_task import WalkingTask

ListTasksResponseItem = typing.Union[GroomingTask, WalkingTask]
