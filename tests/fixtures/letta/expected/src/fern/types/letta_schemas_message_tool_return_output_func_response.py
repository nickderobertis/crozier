

import typing

from .letta_schemas_message_tool_return_output_func_response_one_item import (
    LettaSchemasMessageToolReturnOutputFuncResponseOneItem,
)

LettaSchemasMessageToolReturnOutputFuncResponse = typing.Union[
    str, typing.List[LettaSchemasMessageToolReturnOutputFuncResponseOneItem]
]
