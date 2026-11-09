

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationDtoAction(enum.StrEnum):
    POLICY_CONFIGURATION = "POLICY_CONFIGURATION"
    POLICY_VIEW = "POLICY_VIEW"
    POLICIES_PAGE = "POLICIES_PAGE"
    SCHEMAS_PAGE = "SCHEMAS_PAGE"
    TOKENS_PAGE = "TOKENS_PAGE"
    PROFILE_PAGE = "PROFILE_PAGE"

    def visit(
        self,
        policy_configuration: typing.Callable[[], T_Result],
        policy_view: typing.Callable[[], T_Result],
        policies_page: typing.Callable[[], T_Result],
        schemas_page: typing.Callable[[], T_Result],
        tokens_page: typing.Callable[[], T_Result],
        profile_page: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationDtoAction.POLICY_CONFIGURATION:
            return policy_configuration()
        if self is NotificationDtoAction.POLICY_VIEW:
            return policy_view()
        if self is NotificationDtoAction.POLICIES_PAGE:
            return policies_page()
        if self is NotificationDtoAction.SCHEMAS_PAGE:
            return schemas_page()
        if self is NotificationDtoAction.TOKENS_PAGE:
            return tokens_page()
        if self is NotificationDtoAction.PROFILE_PAGE:
            return profile_page()
