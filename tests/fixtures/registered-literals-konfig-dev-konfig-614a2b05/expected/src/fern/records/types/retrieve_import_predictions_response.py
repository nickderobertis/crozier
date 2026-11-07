

import typing

from .retrieve_import_predictions_response_one_item import RetrieveImportPredictionsResponseOneItem

RetrieveImportPredictionsResponse = typing.Union[
    typing.Dict[str, typing.Any], typing.List[RetrieveImportPredictionsResponseOneItem]
]
