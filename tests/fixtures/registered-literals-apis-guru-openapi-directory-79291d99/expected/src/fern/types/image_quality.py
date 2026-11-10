

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageQuality(enum.StrEnum):
    """
    A high level description of the quality of the image the user submitted.

    For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.

    Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we attribute the failure to low image quality.
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageQuality.HIGH:
            return high()
        if self is ImageQuality.MEDIUM:
            return medium()
        if self is ImageQuality.LOW:
            return low()
