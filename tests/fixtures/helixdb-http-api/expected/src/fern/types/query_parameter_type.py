

from __future__ import annotations

import typing

from .query_parameter_type_zero import QueryParameterTypeZero

if typing.TYPE_CHECKING:
    from .query_parameter_type_array import QueryParameterTypeArray
QueryParameterType = typing.Union[QueryParameterTypeZero, "QueryParameterTypeArray"]
