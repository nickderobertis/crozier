

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConsolePortSpeedLabel(str, enum.Enum):
    ONE_THOUSAND_TWO_HUNDRED_BPS = "1200 bps"
    TWO_THOUSAND_FOUR_HUNDRED_BPS = "2400 bps"
    FOUR_THOUSAND_EIGHT_HUNDRED_BPS = "4800 bps"
    NINE_THOUSAND_SIX_HUNDRED_BPS = "9600 bps"
    NINETEEN2KBPS = "19.2 kbps"
    THIRTY_EIGHT4KBPS = "38.4 kbps"
    FIFTY_SEVEN6KBPS = "57.6 kbps"
    ONE_HUNDRED_FIFTEEN2KBPS = "115.2 kbps"

    def visit(
        self,
        one_thousand_two_hundred_bps: typing.Callable[[], T_Result],
        two_thousand_four_hundred_bps: typing.Callable[[], T_Result],
        four_thousand_eight_hundred_bps: typing.Callable[[], T_Result],
        nine_thousand_six_hundred_bps: typing.Callable[[], T_Result],
        nineteen2kbps: typing.Callable[[], T_Result],
        thirty_eight4kbps: typing.Callable[[], T_Result],
        fifty_seven6kbps: typing.Callable[[], T_Result],
        one_hundred_fifteen2kbps: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsolePortSpeedLabel.ONE_THOUSAND_TWO_HUNDRED_BPS:
            return one_thousand_two_hundred_bps()
        if self is ConsolePortSpeedLabel.TWO_THOUSAND_FOUR_HUNDRED_BPS:
            return two_thousand_four_hundred_bps()
        if self is ConsolePortSpeedLabel.FOUR_THOUSAND_EIGHT_HUNDRED_BPS:
            return four_thousand_eight_hundred_bps()
        if self is ConsolePortSpeedLabel.NINE_THOUSAND_SIX_HUNDRED_BPS:
            return nine_thousand_six_hundred_bps()
        if self is ConsolePortSpeedLabel.NINETEEN2KBPS:
            return nineteen2kbps()
        if self is ConsolePortSpeedLabel.THIRTY_EIGHT4KBPS:
            return thirty_eight4kbps()
        if self is ConsolePortSpeedLabel.FIFTY_SEVEN6KBPS:
            return fifty_seven6kbps()
        if self is ConsolePortSpeedLabel.ONE_HUNDRED_FIFTEEN2KBPS:
            return one_hundred_fifteen2kbps()
