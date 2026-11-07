

import typing

from ...types.response_format_json_object import ResponseFormatJsonObject
from ...types.response_format_json_schema import ResponseFormatJsonSchema
from ...types.response_format_text import ResponseFormatText

ChatCompletionRequestResponseFormat = typing.Union[
    ResponseFormatText, ResponseFormatJsonSchema, ResponseFormatJsonObject
]
