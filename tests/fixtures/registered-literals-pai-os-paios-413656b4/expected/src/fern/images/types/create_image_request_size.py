

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestSize(enum.StrEnum):
    """
    The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.
    """

    TWO_HUNDRED_FIFTY_SIX_X256 = "256x256"
    FIVE_HUNDRED_TWELVE_X512 = "512x512"
    ONE_THOUSAND_TWENTY_FOUR_X1024 = "1024x1024"
    ONE_THOUSAND_SEVEN_HUNDRED_NINETY_TWO_X1024 = "1792x1024"
    ONE_THOUSAND_TWENTY_FOUR_X1792 = "1024x1792"

    def visit(
        self,
        two_hundred_fifty_six_x256: typing.Callable[[], T_Result],
        five_hundred_twelve_x512: typing.Callable[[], T_Result],
        one_thousand_twenty_four_x1024: typing.Callable[[], T_Result],
        one_thousand_seven_hundred_ninety_two_x1024: typing.Callable[[], T_Result],
        one_thousand_twenty_four_x1792: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateImageRequestSize.TWO_HUNDRED_FIFTY_SIX_X256:
            return two_hundred_fifty_six_x256()
        if self is CreateImageRequestSize.FIVE_HUNDRED_TWELVE_X512:
            return five_hundred_twelve_x512()
        if self is CreateImageRequestSize.ONE_THOUSAND_TWENTY_FOUR_X1024:
            return one_thousand_twenty_four_x1024()
        if self is CreateImageRequestSize.ONE_THOUSAND_SEVEN_HUNDRED_NINETY_TWO_X1024:
            return one_thousand_seven_hundred_ninety_two_x1024()
        if self is CreateImageRequestSize.ONE_THOUSAND_TWENTY_FOUR_X1792:
            return one_thousand_twenty_four_x1792()
