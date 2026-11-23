

import typing

from .manual_paddle import ManualPaddle
from .powered_paddle import PoweredPaddle

LockPaddle = typing.Union[ManualPaddle, PoweredPaddle]
