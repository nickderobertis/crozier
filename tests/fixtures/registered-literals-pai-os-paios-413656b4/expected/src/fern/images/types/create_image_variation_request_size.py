

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageVariationRequestSize(enum.StrEnum):
    """
    The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.
    """

    TWO_HUNDRED_FIFTY_SIX_X256 = "256x256"
    FIVE_HUNDRED_TWELVE_X512 = "512x512"
    ONE_THOUSAND_TWENTY_FOUR_X1024 = "1024x1024"

    def visit(
        self,
        two_hundred_fifty_six_x256: typing.Callable[[], T_Result],
        five_hundred_twelve_x512: typing.Callable[[], T_Result],
        one_thousand_twenty_four_x1024: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateImageVariationRequestSize.TWO_HUNDRED_FIFTY_SIX_X256:
            return two_hundred_fifty_six_x256()
        if self is CreateImageVariationRequestSize.FIVE_HUNDRED_TWELVE_X512:
            return five_hundred_twelve_x512()
        if self is CreateImageVariationRequestSize.ONE_THOUSAND_TWENTY_FOUR_X1024:
            return one_thousand_twenty_four_x1024()
