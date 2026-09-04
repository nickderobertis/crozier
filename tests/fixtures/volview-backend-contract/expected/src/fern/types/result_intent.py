

import typing

from .result_intent_id import ResultIntentId
from .result_intent_zero import ResultIntentZero

ResultIntent = typing.Union[ResultIntentZero, ResultIntentId]
