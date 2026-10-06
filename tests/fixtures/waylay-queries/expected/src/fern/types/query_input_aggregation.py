

import typing

from .query_input_aggregation_three_value_value import QueryInputAggregationThreeValueValue
from .query_input_aggregation_two_value import QueryInputAggregationTwoValue

QueryInputAggregation = typing.Union[
    str,
    typing.List[typing.Optional[str]],
    typing.Dict[str, typing.Optional[QueryInputAggregationTwoValue]],
    typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[QueryInputAggregationThreeValueValue]]]],
]
