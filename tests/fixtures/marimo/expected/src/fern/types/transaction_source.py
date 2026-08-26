

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionSource(enum.StrEnum):
    CELL_MANAGER = "cell-manager"
    CODE_MODE = "code-mode"
    FILE_WATCH = "file-watch"
    FRONTEND = "frontend"
    KERNEL = "kernel"

    def visit(
        self,
        cell_manager: typing.Callable[[], T_Result],
        code_mode: typing.Callable[[], T_Result],
        file_watch: typing.Callable[[], T_Result],
        frontend: typing.Callable[[], T_Result],
        kernel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionSource.CELL_MANAGER:
            return cell_manager()
        if self is TransactionSource.CODE_MODE:
            return code_mode()
        if self is TransactionSource.FILE_WATCH:
            return file_watch()
        if self is TransactionSource.FRONTEND:
            return frontend()
        if self is TransactionSource.KERNEL:
            return kernel()
