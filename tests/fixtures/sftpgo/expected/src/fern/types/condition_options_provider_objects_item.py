

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionOptionsProviderObjectsItem(enum.StrEnum):
    USER = "user"
    GROUP = "group"
    ADMIN = "admin"
    API_KEY = "api_key"
    SHARE = "share"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        api_key: typing.Callable[[], T_Result],
        share: typing.Callable[[], T_Result],
        event_action: typing.Callable[[], T_Result],
        event_rule: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionOptionsProviderObjectsItem.USER:
            return user()
        if self is ConditionOptionsProviderObjectsItem.GROUP:
            return group()
        if self is ConditionOptionsProviderObjectsItem.ADMIN:
            return admin()
        if self is ConditionOptionsProviderObjectsItem.API_KEY:
            return api_key()
        if self is ConditionOptionsProviderObjectsItem.SHARE:
            return share()
        if self is ConditionOptionsProviderObjectsItem.EVENT_ACTION:
            return event_action()
        if self is ConditionOptionsProviderObjectsItem.EVENT_RULE:
            return event_rule()
