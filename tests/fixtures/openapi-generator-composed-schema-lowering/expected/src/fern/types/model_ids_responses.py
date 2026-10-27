

import typing

from .model_ids_responses_one import ModelIdsResponsesOne
from .model_ids_shared import ModelIdsShared

ModelIdsResponses = typing.Union[ModelIdsShared, ModelIdsResponsesOne]
