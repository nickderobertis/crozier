

import typing

from .response_format_nullish_json_schema import ResponseFormatNullishJsonSchema
from .response_format_nullish_type import ResponseFormatNullishType
from .response_format_nullish_zero import ResponseFormatNullishZero

ResponseFormatNullish = typing.Union[
    ResponseFormatNullishZero, ResponseFormatNullishJsonSchema, ResponseFormatNullishType
]
