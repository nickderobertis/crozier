

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityProvider(enum.StrEnum):
    AWS_MARKETPLACE = "AWS_Marketplace"
    GIT_HUB = "GitHub"
    BITBUCKET = "Bitbucket"

    def visit(
        self,
        aws_marketplace: typing.Callable[[], T_Result],
        git_hub: typing.Callable[[], T_Result],
        bitbucket: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityProvider.AWS_MARKETPLACE:
            return aws_marketplace()
        if self is IdentityProvider.GIT_HUB:
            return git_hub()
        if self is IdentityProvider.BITBUCKET:
            return bitbucket()
