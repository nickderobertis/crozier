

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostClientRequestRequestUserClaimsItem(enum.StrEnum):
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
        if self is PostClientRequestRequestUserClaimsItem.NAME:
            return name()
        if self is PostClientRequestRequestUserClaimsItem.GIVEN_NAME:
            return given_name()
        if self is PostClientRequestRequestUserClaimsItem.MIDDLE_NAME:
            return middle_name()
        if self is PostClientRequestRequestUserClaimsItem.PREFERRED_USERNAME:
            return preferred_username()
        if self is PostClientRequestRequestUserClaimsItem.NICKNAME:
            return nickname()
        if self is PostClientRequestRequestUserClaimsItem.GENDER:
            return gender()
        if self is PostClientRequestRequestUserClaimsItem.BIRTHDATE:
            return birthdate()
        if self is PostClientRequestRequestUserClaimsItem.EMAIL:
            return email()
        if self is PostClientRequestRequestUserClaimsItem.PHONE_NUMBER:
            return phone_number()
        if self is PostClientRequestRequestUserClaimsItem.PICTURE:
            return picture()
        if self is PostClientRequestRequestUserClaimsItem.ADDRESS:
            return address()
