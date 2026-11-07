

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoginStepUserInputUserInputFieldsItemType(enum.StrEnum):
    """
    The type of field.
    """

    USERNAME = "username"
    PHONE_NUMBER = "phone_number"
    EMAIL = "email"
    PASSWORD = "password"
    TWO_FA_CODE = "2fa_code"
    TOKEN = "token"
    URL = "url"
    DOMAIN = "domain"

    def visit(
        self,
        username: typing.Callable[[], T_Result],
        phone_number: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        two_fa_code: typing.Callable[[], T_Result],
        token: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        domain: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoginStepUserInputUserInputFieldsItemType.USERNAME:
            return username()
        if self is LoginStepUserInputUserInputFieldsItemType.PHONE_NUMBER:
            return phone_number()
        if self is LoginStepUserInputUserInputFieldsItemType.EMAIL:
            return email()
        if self is LoginStepUserInputUserInputFieldsItemType.PASSWORD:
            return password()
        if self is LoginStepUserInputUserInputFieldsItemType.TWO_FA_CODE:
            return two_fa_code()
        if self is LoginStepUserInputUserInputFieldsItemType.TOKEN:
            return token()
        if self is LoginStepUserInputUserInputFieldsItemType.URL:
            return url()
        if self is LoginStepUserInputUserInputFieldsItemType.DOMAIN:
            return domain()
