

import typing

from .cargo_check_qr_inputs import CargoCheckQrInputs
from .cargo_close_inputs import CargoCloseInputs
from .cargo_lift_inputs import CargoLiftInputs
from .cargo_lower_inputs import CargoLowerInputs
from .cargo_open_inputs import CargoOpenInputs
from .move_backward_inputs import MoveBackwardInputs
from .move_forward_inputs import MoveForwardInputs
from .move_to_inputs import MoveToInputs
from .scan_location_inputs import ScanLocationInputs
from .stop_inputs import StopInputs
from .wait_inputs import WaitInputs

CommandInputs = typing.Union[
    StopInputs,
    MoveForwardInputs,
    MoveBackwardInputs,
    MoveToInputs,
    CargoOpenInputs,
    CargoCloseInputs,
    CargoLiftInputs,
    CargoLowerInputs,
    CargoCheckQrInputs,
    ScanLocationInputs,
    WaitInputs,
]
