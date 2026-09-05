

import typing

from .function_id_code import FunctionIdCode
from .function_id_function_id import FunctionIdFunctionId
from .function_id_global_function import FunctionIdGlobalFunction
from .function_id_inline_function import FunctionIdInlineFunction
from .function_id_name import FunctionIdName
from .function_id_project_name import FunctionIdProjectName
from .function_id_prompt_session_function_id import FunctionIdPromptSessionFunctionId

FunctionId = typing.Union[
    FunctionIdFunctionId,
    FunctionIdProjectName,
    FunctionIdGlobalFunction,
    FunctionIdPromptSessionFunctionId,
    FunctionIdCode,
    FunctionIdInlineFunction,
    FunctionIdName,
]
