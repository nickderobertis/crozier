

import typing

from .records_get_predictions_response_one_item import RecordsGetPredictionsResponseOneItem

RecordsGetPredictionsResponse = typing.Union[
    typing.Dict[str, typing.Any], typing.List[RecordsGetPredictionsResponseOneItem]
]
