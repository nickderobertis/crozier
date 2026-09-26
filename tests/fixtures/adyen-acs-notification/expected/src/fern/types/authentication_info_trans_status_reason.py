

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoTransStatusReason(enum.StrEnum):
    """
    Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values).
    """

    ONE = "01"
    TWO = "02"
    THREE = "03"
    FOUR = "04"
    FIVE = "05"
    SIX = "06"
    SEVEN = "07"
    EIGHT = "08"
    NINE = "09"
    TEN = "10"
    ELEVEN = "11"
    TWELVE = "12"
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SIXTEEN = "16"
    SEVENTEEN = "17"
    EIGHTEEN = "18"
    NINETEEN = "19"
    TWENTY = "20"
    TWENTY_ONE = "21"
    TWENTY_TWO = "22"
    TWENTY_THREE = "23"
    TWENTY_FOUR = "24"
    TWENTY_FIVE = "25"
    TWENTY_SIX = "26"
    EIGHTY = "80"
    EIGHTY_ONE = "81"
    EIGHTY_TWO = "82"
    EIGHTY_THREE = "83"
    EIGHTY_FOUR = "84"
    EIGHTY_FIVE = "85"
    EIGHTY_SIX = "86"
    EIGHTY_SEVEN = "87"
    EIGHTY_EIGHT = "88"

    def visit(
        self,
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
        four: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        six: typing.Callable[[], T_Result],
        seven: typing.Callable[[], T_Result],
        eight: typing.Callable[[], T_Result],
        nine: typing.Callable[[], T_Result],
        ten: typing.Callable[[], T_Result],
        eleven: typing.Callable[[], T_Result],
        twelve: typing.Callable[[], T_Result],
        thirteen: typing.Callable[[], T_Result],
        fourteen: typing.Callable[[], T_Result],
        fifteen: typing.Callable[[], T_Result],
        sixteen: typing.Callable[[], T_Result],
        seventeen: typing.Callable[[], T_Result],
        eighteen: typing.Callable[[], T_Result],
        nineteen: typing.Callable[[], T_Result],
        twenty: typing.Callable[[], T_Result],
        twenty_one: typing.Callable[[], T_Result],
        twenty_two: typing.Callable[[], T_Result],
        twenty_three: typing.Callable[[], T_Result],
        twenty_four: typing.Callable[[], T_Result],
        twenty_five: typing.Callable[[], T_Result],
        twenty_six: typing.Callable[[], T_Result],
        eighty: typing.Callable[[], T_Result],
        eighty_one: typing.Callable[[], T_Result],
        eighty_two: typing.Callable[[], T_Result],
        eighty_three: typing.Callable[[], T_Result],
        eighty_four: typing.Callable[[], T_Result],
        eighty_five: typing.Callable[[], T_Result],
        eighty_six: typing.Callable[[], T_Result],
        eighty_seven: typing.Callable[[], T_Result],
        eighty_eight: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationInfoTransStatusReason.ONE:
            return one()
        if self is AuthenticationInfoTransStatusReason.TWO:
            return two()
        if self is AuthenticationInfoTransStatusReason.THREE:
            return three()
        if self is AuthenticationInfoTransStatusReason.FOUR:
            return four()
        if self is AuthenticationInfoTransStatusReason.FIVE:
            return five()
        if self is AuthenticationInfoTransStatusReason.SIX:
            return six()
        if self is AuthenticationInfoTransStatusReason.SEVEN:
            return seven()
        if self is AuthenticationInfoTransStatusReason.EIGHT:
            return eight()
        if self is AuthenticationInfoTransStatusReason.NINE:
            return nine()
        if self is AuthenticationInfoTransStatusReason.TEN:
            return ten()
        if self is AuthenticationInfoTransStatusReason.ELEVEN:
            return eleven()
        if self is AuthenticationInfoTransStatusReason.TWELVE:
            return twelve()
        if self is AuthenticationInfoTransStatusReason.THIRTEEN:
            return thirteen()
        if self is AuthenticationInfoTransStatusReason.FOURTEEN:
            return fourteen()
        if self is AuthenticationInfoTransStatusReason.FIFTEEN:
            return fifteen()
        if self is AuthenticationInfoTransStatusReason.SIXTEEN:
            return sixteen()
        if self is AuthenticationInfoTransStatusReason.SEVENTEEN:
            return seventeen()
        if self is AuthenticationInfoTransStatusReason.EIGHTEEN:
            return eighteen()
        if self is AuthenticationInfoTransStatusReason.NINETEEN:
            return nineteen()
        if self is AuthenticationInfoTransStatusReason.TWENTY:
            return twenty()
        if self is AuthenticationInfoTransStatusReason.TWENTY_ONE:
            return twenty_one()
        if self is AuthenticationInfoTransStatusReason.TWENTY_TWO:
            return twenty_two()
        if self is AuthenticationInfoTransStatusReason.TWENTY_THREE:
            return twenty_three()
        if self is AuthenticationInfoTransStatusReason.TWENTY_FOUR:
            return twenty_four()
        if self is AuthenticationInfoTransStatusReason.TWENTY_FIVE:
            return twenty_five()
        if self is AuthenticationInfoTransStatusReason.TWENTY_SIX:
            return twenty_six()
        if self is AuthenticationInfoTransStatusReason.EIGHTY:
            return eighty()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_ONE:
            return eighty_one()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_TWO:
            return eighty_two()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_THREE:
            return eighty_three()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_FOUR:
            return eighty_four()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_FIVE:
            return eighty_five()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_SIX:
            return eighty_six()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_SEVEN:
            return eighty_seven()
        if self is AuthenticationInfoTransStatusReason.EIGHTY_EIGHT:
            return eighty_eight()
