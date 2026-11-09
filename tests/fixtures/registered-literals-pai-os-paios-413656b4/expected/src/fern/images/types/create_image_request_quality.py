

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestQuality(enum.StrEnum):
    """
    The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.
    """

    STANDARD = "standard"
    HD = "hd"

    def visit(self, standard: typing.Callable[[], T_Result], hd: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageRequestQuality.STANDARD:
            return standard()
        if self is CreateImageRequestQuality.HD:
            return hd()
