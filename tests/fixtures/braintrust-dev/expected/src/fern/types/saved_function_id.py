

import typing

from .saved_function_id_function_type import SavedFunctionIdFunctionType
from .saved_function_id_id import SavedFunctionIdId

SavedFunctionId = typing.Union[SavedFunctionIdId, SavedFunctionIdFunctionType]
