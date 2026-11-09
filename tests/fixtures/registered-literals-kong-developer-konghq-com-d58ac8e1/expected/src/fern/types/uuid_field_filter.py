

import typing

from .string_field_equals_filter import StringFieldEqualsFilter
from .string_field_neq_filter import StringFieldNeqFilter
from .string_field_oeq_filter import StringFieldOeqFilter

UuidFieldFilter = typing.Union[StringFieldEqualsFilter, StringFieldOeqFilter, StringFieldNeqFilter]
