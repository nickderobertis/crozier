

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowAudioEssenceParametersUncParametersUncType(enum.StrEnum):
    """
    The uncompressed audio multi-channel representation type. If codec is `audio/x-raw-int` or `audio/x-raw-float`, unc_type must be set.
    """

    INTERLEAVED = "interleaved"
    PLANAR = "planar"
    PAIRS = "pairs"

    def visit(
        self,
        interleaved: typing.Callable[[], T_Result],
        planar: typing.Callable[[], T_Result],
        pairs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FlowAudioEssenceParametersUncParametersUncType.INTERLEAVED:
            return interleaved()
        if self is FlowAudioEssenceParametersUncParametersUncType.PLANAR:
            return planar()
        if self is FlowAudioEssenceParametersUncParametersUncType.PAIRS:
            return pairs()
