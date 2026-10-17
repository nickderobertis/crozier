

import typing

from .collect_field import CollectField
from .undefined import Undefined

PromptUpdateParamsCollectFields = typing.Union[typing.List[CollectField], Undefined]
