

import typing

from .query_output_aggregation_three_value_value import QueryOutputAggregationThreeValueValue
from .query_output_aggregation_two_value import QueryOutputAggregationTwoValue

QueryOutputAggregation = typing.Union[
    str,
    typing.List[typing.Optional[str]],
    typing.Dict[str, typing.Optional[QueryOutputAggregationTwoValue]],
    typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[QueryOutputAggregationThreeValueValue]]]],
]
