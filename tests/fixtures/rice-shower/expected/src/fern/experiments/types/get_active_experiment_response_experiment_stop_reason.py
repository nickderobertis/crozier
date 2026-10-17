

import typing

from .get_active_experiment_response_experiment_stop_reason_one import (
    GetActiveExperimentResponseExperimentStopReasonOne,
)
from .get_active_experiment_response_experiment_stop_reason_three import (
    GetActiveExperimentResponseExperimentStopReasonThree,
)
from .get_active_experiment_response_experiment_stop_reason_two import (
    GetActiveExperimentResponseExperimentStopReasonTwo,
)
from .get_active_experiment_response_experiment_stop_reason_zero import (
    GetActiveExperimentResponseExperimentStopReasonZero,
)

GetActiveExperimentResponseExperimentStopReason = typing.Union[
    GetActiveExperimentResponseExperimentStopReasonZero,
    GetActiveExperimentResponseExperimentStopReasonOne,
    GetActiveExperimentResponseExperimentStopReasonTwo,
    GetActiveExperimentResponseExperimentStopReasonThree,
]
