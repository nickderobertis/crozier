

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderEventObjectType(enum.StrEnum):
    USER = "user"
    FOLDER = "folder"
    GROUP = "group"
    ADMIN = "admin"
    API_KEY = "api_key"
    SHARE = "share"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"
    ROLE = "role"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        api_key: typing.Callable[[], T_Result],
        share: typing.Callable[[], T_Result],
        event_action: typing.Callable[[], T_Result],
        event_rule: typing.Callable[[], T_Result],
        role: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderEventObjectType.USER:
            return user()
        if self is ProviderEventObjectType.FOLDER:
            return folder()
        if self is ProviderEventObjectType.GROUP:
            return group()
        if self is ProviderEventObjectType.ADMIN:
            return admin()
        if self is ProviderEventObjectType.API_KEY:
            return api_key()
        if self is ProviderEventObjectType.SHARE:
            return share()
        if self is ProviderEventObjectType.EVENT_ACTION:
            return event_action()
        if self is ProviderEventObjectType.EVENT_RULE:
            return event_rule()
        if self is ProviderEventObjectType.ROLE:
            return role()
