

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestStyle(enum.StrEnum):
    """
    The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.
    """

    VIVID = "vivid"
    NATURAL = "natural"

    def visit(self, vivid: typing.Callable[[], T_Result], natural: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageRequestStyle.VIVID:
            return vivid()
        if self is CreateImageRequestStyle.NATURAL:
            return natural()
