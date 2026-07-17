

import typing

from .header_dto import HeaderDto

OperationHeaders = typing.Dict[str, typing.List[HeaderDto]]
"""
Specification of additional headers for a Service/API operations. Keys are operation name or "globals" (if header applies to all), values are Header objects DTO.
"""
