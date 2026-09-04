

import typing

from .previous_turn_id_input_one import PreviousTurnIdInputOne
from .previous_turn_id_input_zero import PreviousTurnIdInputZero

PreviousTurnIdInput = typing.Union[PreviousTurnIdInputZero, PreviousTurnIdInputOne, str]
