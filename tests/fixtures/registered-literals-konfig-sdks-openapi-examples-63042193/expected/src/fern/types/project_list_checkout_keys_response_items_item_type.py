

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectListCheckoutKeysResponseItemsItemType(enum.StrEnum):
    """
    The type of checkout key. This may be either `deploy-key` or `github-user-key`.
    """

    DEPLOY_KEY = "deploy-key"
    GITHUB_USER_KEY = "github-user-key"

    def visit(
        self, deploy_key: typing.Callable[[], T_Result], github_user_key: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ProjectListCheckoutKeysResponseItemsItemType.DEPLOY_KEY:
            return deploy_key()
        if self is ProjectListCheckoutKeysResponseItemsItemType.GITHUB_USER_KEY:
            return github_user_key()
