

import typing

from .query_parameter_type import QueryParameterType

QueryParameterTypes = typing.Dict[str, QueryParameterType]
"""
When present, keys must exactly match parameters. Typed and untyped parameters cannot be mixed. The HTTP contract deliberately omits f32 and f64 declarations because JSON Schema cannot express the lexical distinction required by exact typed decoding; send floating-point JSON numbers without parameter_types.
"""
