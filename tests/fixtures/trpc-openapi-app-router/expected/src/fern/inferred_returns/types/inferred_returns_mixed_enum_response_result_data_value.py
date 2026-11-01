

import typing

from .inferred_returns_mixed_enum_response_result_data_value_two import (
    InferredReturnsMixedEnumResponseResultDataValueTwo,
)
from .inferred_returns_mixed_enum_response_result_data_value_zero import (
    InferredReturnsMixedEnumResponseResultDataValueZero,
)

InferredReturnsMixedEnumResponseResultDataValue = typing.Union[
    InferredReturnsMixedEnumResponseResultDataValueZero, float, InferredReturnsMixedEnumResponseResultDataValueTwo
]
