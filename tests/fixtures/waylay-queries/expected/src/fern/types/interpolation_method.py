

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterpolationMethod(enum.StrEnum):
    """
    Interpolation algorithm specifier.
    """

    PAD = "pad"
    FIXED = "fixed"
    BACKFILL = "backfill"
    LINEAR = "linear"
    ZERO = "zero"
    SLINEAR = "slinear"
    QUADRATIC = "quadratic"
    CUBIC = "cubic"
    POLYNOMIAL = "polynomial"
    SPLINE = "spline"
    FROM_DERIVATIVES = "from_derivatives"
    PCHIP = "pchip"
    AKIMA = "akima"

    def visit(
        self,
        pad: typing.Callable[[], T_Result],
        fixed: typing.Callable[[], T_Result],
        backfill: typing.Callable[[], T_Result],
        linear: typing.Callable[[], T_Result],
        zero: typing.Callable[[], T_Result],
        slinear: typing.Callable[[], T_Result],
        quadratic: typing.Callable[[], T_Result],
        cubic: typing.Callable[[], T_Result],
        polynomial: typing.Callable[[], T_Result],
        spline: typing.Callable[[], T_Result],
        from_derivatives: typing.Callable[[], T_Result],
        pchip: typing.Callable[[], T_Result],
        akima: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterpolationMethod.PAD:
            return pad()
        if self is InterpolationMethod.FIXED:
            return fixed()
        if self is InterpolationMethod.BACKFILL:
            return backfill()
        if self is InterpolationMethod.LINEAR:
            return linear()
        if self is InterpolationMethod.ZERO:
            return zero()
        if self is InterpolationMethod.SLINEAR:
            return slinear()
        if self is InterpolationMethod.QUADRATIC:
            return quadratic()
        if self is InterpolationMethod.CUBIC:
            return cubic()
        if self is InterpolationMethod.POLYNOMIAL:
            return polynomial()
        if self is InterpolationMethod.SPLINE:
            return spline()
        if self is InterpolationMethod.FROM_DERIVATIVES:
            return from_derivatives()
        if self is InterpolationMethod.PCHIP:
            return pchip()
        if self is InterpolationMethod.AKIMA:
            return akima()
