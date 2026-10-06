

import typing

from .cycle_error import CycleError
from .import_star_error import ImportStarError
from .marimo_ancestor_prevented_error import MarimoAncestorPreventedError
from .marimo_ancestor_stopped_error import MarimoAncestorStoppedError
from .marimo_exception_raised_error import MarimoExceptionRaisedError
from .marimo_internal_error import MarimoInternalError
from .marimo_interruption_error import MarimoInterruptionError
from .marimo_sql_error import MarimoSqlError
from .marimo_strict_execution_error import MarimoStrictExecutionError
from .marimo_syntax_error import MarimoSyntaxError
from .multiple_definition_error import MultipleDefinitionError
from .setup_root_error import SetupRootError
from .unknown_error import UnknownError

CellOutputDataOneItem = typing.Union[
    SetupRootError,
    CycleError,
    MultipleDefinitionError,
    ImportStarError,
    MarimoAncestorStoppedError,
    MarimoAncestorPreventedError,
    MarimoExceptionRaisedError,
    MarimoStrictExecutionError,
    MarimoInterruptionError,
    MarimoSyntaxError,
    MarimoInternalError,
    MarimoSqlError,
    UnknownError,
]
