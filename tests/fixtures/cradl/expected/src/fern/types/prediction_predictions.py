

import typing

from .prediction_predictions_zero_item import PredictionPredictionsZeroItem

PredictionPredictions = typing.Union[
    typing.Optional[typing.List[PredictionPredictionsZeroItem]], typing.Optional[typing.Dict[str, typing.Any]]
]
