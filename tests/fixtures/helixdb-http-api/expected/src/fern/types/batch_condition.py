

import typing

from .batch_condition_var_empty import BatchConditionVarEmpty
from .batch_condition_var_min_size import BatchConditionVarMinSize
from .batch_condition_var_not_empty import BatchConditionVarNotEmpty
from .batch_condition_zero import BatchConditionZero

BatchCondition = typing.Union[
    BatchConditionZero, BatchConditionVarNotEmpty, BatchConditionVarEmpty, BatchConditionVarMinSize
]
