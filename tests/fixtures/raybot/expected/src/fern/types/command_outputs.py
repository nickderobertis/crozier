

import typing

from .cargo_check_qr_outputs import CargoCheckQrOutputs
from .cargo_close_outputs import CargoCloseOutputs
from .cargo_lift_outputs import CargoLiftOutputs
from .cargo_lower_outputs import CargoLowerOutputs
from .cargo_open_outputs import CargoOpenOutputs
from .move_backward_outputs import MoveBackwardOutputs
from .move_forward_outputs import MoveForwardOutputs
from .move_to_outputs import MoveToOutputs
from .scan_location_outputs import ScanLocationOutputs
from .stop_outputs import StopOutputs
from .wait_outputs import WaitOutputs

CommandOutputs = typing.Union[
    StopOutputs,
    MoveForwardOutputs,
    MoveBackwardOutputs,
    MoveToOutputs,
    CargoOpenOutputs,
    CargoCloseOutputs,
    CargoLiftOutputs,
    CargoLowerOutputs,
    CargoCheckQrOutputs,
    ScanLocationOutputs,
    WaitOutputs,
]
