

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthClientRequestRequestUserClaimsItem(enum.StrEnum):
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
        if self is PostOauthClientRequestRequestUserClaimsItem.NAME:
            return name()
        if self is PostOauthClientRequestRequestUserClaimsItem.GIVEN_NAME:
            return given_name()
        if self is PostOauthClientRequestRequestUserClaimsItem.MIDDLE_NAME:
            return middle_name()
        if self is PostOauthClientRequestRequestUserClaimsItem.PREFERRED_USERNAME:
            return preferred_username()
        if self is PostOauthClientRequestRequestUserClaimsItem.NICKNAME:
            return nickname()
        if self is PostOauthClientRequestRequestUserClaimsItem.GENDER:
            return gender()
        if self is PostOauthClientRequestRequestUserClaimsItem.BIRTHDATE:
            return birthdate()
        if self is PostOauthClientRequestRequestUserClaimsItem.EMAIL:
            return email()
        if self is PostOauthClientRequestRequestUserClaimsItem.PHONE_NUMBER:
            return phone_number()
        if self is PostOauthClientRequestRequestUserClaimsItem.PICTURE:
            return picture()
        if self is PostOauthClientRequestRequestUserClaimsItem.ADDRESS:
            return address()
