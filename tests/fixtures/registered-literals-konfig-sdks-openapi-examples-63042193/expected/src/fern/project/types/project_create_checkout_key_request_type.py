

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectCreateCheckoutKeyRequestType(enum.StrEnum):
    """
    The type of checkout key to create. This may be either `deploy-key` or `user-key`.
    """

    USER_KEY = "user-key"
    DEPLOY_KEY = "deploy-key"

    def visit(self, user_key: typing.Callable[[], T_Result], deploy_key: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectCreateCheckoutKeyRequestType.USER_KEY:
            return user_key()
        if self is ProjectCreateCheckoutKeyRequestType.DEPLOY_KEY:
            return deploy_key()
