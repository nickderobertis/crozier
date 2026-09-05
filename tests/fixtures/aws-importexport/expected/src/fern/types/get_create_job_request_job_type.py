

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCreateJobRequestJobType(enum.StrEnum):
    """
    Specifies whether the job to initiate is an import or export job.
    """

    IMPORT = "Import"
    EXPORT = "Export"

    def visit(self, import_: typing.Callable[[], T_Result], export: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCreateJobRequestJobType.IMPORT:
            return import_()
        if self is GetCreateJobRequestJobType.EXPORT:
            return export()
