

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItemMessageMode(
    enum.StrEnum
):
    ALL = "all"
    APP_MENTIONS_ONLY = "app_mentions_only"

    def visit(self, all_: typing.Callable[[], T_Result], app_mentions_only: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItemMessageMode.ALL
        ):
            return all_()
        if (
            self
            is PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItemMessageMode.APP_MENTIONS_ONLY
        ):
            return app_mentions_only()
