

import typing

from .query_post_response_data_item_results_one import QueryPostResponseDataItemResultsOne
from .query_post_response_data_item_results_two import QueryPostResponseDataItemResultsTwo
from .query_post_response_data_item_results_zero_item_value import QueryPostResponseDataItemResultsZeroItemValue

QueryPostResponseDataItemResults = typing.Union[
    typing.List[typing.Dict[str, QueryPostResponseDataItemResultsZeroItemValue]],
    QueryPostResponseDataItemResultsOne,
    QueryPostResponseDataItemResultsTwo,
    typing.Optional[typing.Any],
]
