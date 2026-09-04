

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutClientClientIdRequestRequestUserClaimsItem(enum.StrEnum):
    NAME = "name"
    GIVEN_NAME = "given_name"
    MIDDLE_NAME = "middle_name"
    PREFERRED_USERNAME = "preferred_username"
    NICKNAME = "nickname"
    GENDER = "gender"
    BIRTHDATE = "birthdate"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    PICTURE = "picture"
    ADDRESS = "address"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        given_name: typing.Callable[[], T_Result],
        middle_name: typing.Callable[[], T_Result],
        preferred_username: typing.Callable[[], T_Result],
        nickname: typing.Callable[[], T_Result],
        gender: typing.Callable[[], T_Result],
        birthdate: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        phone_number: typing.Callable[[], T_Result],
        picture: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutClientClientIdRequestRequestUserClaimsItem.NAME:
            return name()
        if self is PutClientClientIdRequestRequestUserClaimsItem.GIVEN_NAME:
            return given_name()
        if self is PutClientClientIdRequestRequestUserClaimsItem.MIDDLE_NAME:
            return middle_name()
        if self is PutClientClientIdRequestRequestUserClaimsItem.PREFERRED_USERNAME:
            return preferred_username()
        if self is PutClientClientIdRequestRequestUserClaimsItem.NICKNAME:
            return nickname()
        if self is PutClientClientIdRequestRequestUserClaimsItem.GENDER:
            return gender()
        if self is PutClientClientIdRequestRequestUserClaimsItem.BIRTHDATE:
            return birthdate()
        if self is PutClientClientIdRequestRequestUserClaimsItem.EMAIL:
            return email()
        if self is PutClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER:
            return phone_number()
        if self is PutClientClientIdRequestRequestUserClaimsItem.PICTURE:
            return picture()
        if self is PutClientClientIdRequestRequestUserClaimsItem.ADDRESS:
            return address()
