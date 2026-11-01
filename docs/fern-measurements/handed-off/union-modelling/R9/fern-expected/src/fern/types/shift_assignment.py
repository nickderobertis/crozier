

import typing

from .cover import Cover
from .leave import Leave
from .training import Training

ShiftAssignment = typing.Union[Cover, Training, Leave]
