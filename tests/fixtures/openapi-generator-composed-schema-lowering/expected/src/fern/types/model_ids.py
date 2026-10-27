

import typing

from .model_ids_responses import ModelIdsResponses
from .model_ids_shared import ModelIdsShared

ModelIds = typing.Union[ModelIdsShared, ModelIdsResponses]
