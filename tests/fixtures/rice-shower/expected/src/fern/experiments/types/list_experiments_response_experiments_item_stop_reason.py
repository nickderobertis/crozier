

import typing

from .list_experiments_response_experiments_item_stop_reason_one import (
    ListExperimentsResponseExperimentsItemStopReasonOne,
)
from .list_experiments_response_experiments_item_stop_reason_three import (
    ListExperimentsResponseExperimentsItemStopReasonThree,
)
from .list_experiments_response_experiments_item_stop_reason_two import (
    ListExperimentsResponseExperimentsItemStopReasonTwo,
)
from .list_experiments_response_experiments_item_stop_reason_zero import (
    ListExperimentsResponseExperimentsItemStopReasonZero,
)

ListExperimentsResponseExperimentsItemStopReason = typing.Union[
    ListExperimentsResponseExperimentsItemStopReasonZero,
    ListExperimentsResponseExperimentsItemStopReasonOne,
    ListExperimentsResponseExperimentsItemStopReasonTwo,
    ListExperimentsResponseExperimentsItemStopReasonThree,
]
