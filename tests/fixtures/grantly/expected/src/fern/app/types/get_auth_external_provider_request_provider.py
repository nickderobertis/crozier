

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthExternalProviderRequestProvider(enum.StrEnum):
    GOOGLE = "google"
    GITHUB = "github"

    def visit(self, google: typing.Callable[[], T_Result], github: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAuthExternalProviderRequestProvider.GOOGLE:
            return google()
        if self is GetAuthExternalProviderRequestProvider.GITHUB:
            return github()
