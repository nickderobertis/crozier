

import typing

from .string_field_contains_filter import StringFieldContainsFilter
from .string_field_equals_filter import StringFieldEqualsFilter
from .string_field_neq_filter import StringFieldNeqFilter
from .string_field_o_contains_filter import StringFieldOContainsFilter
from .string_field_oeq_filter import StringFieldOeqFilter

LabelsFieldFilter = typing.Union[
    StringFieldEqualsFilter,
    StringFieldContainsFilter,
    StringFieldOContainsFilter,
    StringFieldOeqFilter,
    StringFieldNeqFilter,
]
