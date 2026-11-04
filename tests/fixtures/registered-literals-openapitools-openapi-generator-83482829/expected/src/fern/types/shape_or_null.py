

import typing

from .shape import Shape

ShapeOrNull = typing.Optional[Shape]
"""
A value that is either a Shape or null. OAS 3.1 expresses nullable via oneOf with a null member instead of the deprecated `nullable: true` attribute.
"""
