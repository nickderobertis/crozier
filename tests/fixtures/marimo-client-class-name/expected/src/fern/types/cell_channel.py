

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CellChannel(enum.StrEnum):
    """
    The channel of a cell's output.
    """

    MARIMO_ERROR = "marimo-error"
    MEDIA = "media"
    OUTPUT = "output"
    PDB = "pdb"
    STDERR = "stderr"
    STDIN = "stdin"
    STDOUT = "stdout"

    def visit(
        self,
        marimo_error: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        output: typing.Callable[[], T_Result],
        pdb: typing.Callable[[], T_Result],
        stderr: typing.Callable[[], T_Result],
        stdin: typing.Callable[[], T_Result],
        stdout: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CellChannel.MARIMO_ERROR:
            return marimo_error()
        if self is CellChannel.MEDIA:
            return media()
        if self is CellChannel.OUTPUT:
            return output()
        if self is CellChannel.PDB:
            return pdb()
        if self is CellChannel.STDERR:
            return stderr()
        if self is CellChannel.STDIN:
            return stdin()
        if self is CellChannel.STDOUT:
            return stdout()
