

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Quantization(enum.StrEnum):
    """
    Quantization method for embeddings.
    """

    SCALAR_QUANTIZATION_I8 = "ScalarQuantizationI8"
    TURBO_QUANT_I8 = "TurboQuantI8"
    NONE = "None"

    def visit(
        self,
        scalar_quantization_i8: typing.Callable[[], T_Result],
        turbo_quant_i8: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Quantization.SCALAR_QUANTIZATION_I8:
            return scalar_quantization_i8()
        if self is Quantization.TURBO_QUANT_I8:
            return turbo_quant_i8()
        if self is Quantization.NONE:
            return none()
