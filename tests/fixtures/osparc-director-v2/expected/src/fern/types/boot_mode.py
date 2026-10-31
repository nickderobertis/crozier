

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BootMode(enum.StrEnum):
    CPU = "CPU"
    GPU = "GPU"
    MPI = "MPI"

    def visit(
        self, cpu: typing.Callable[[], T_Result], gpu: typing.Callable[[], T_Result], mpi: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BootMode.CPU:
            return cpu()
        if self is BootMode.GPU:
            return gpu()
        if self is BootMode.MPI:
            return mpi()
