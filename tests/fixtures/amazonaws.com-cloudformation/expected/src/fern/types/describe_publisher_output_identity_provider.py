

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribePublisherOutputIdentityProvider(enum.StrEnum):
    """
    The type of account used as the identity provider when registering this publisher with CloudFormation.
    """

    AWS_MARKETPLACE = "AWS_Marketplace"
    GIT_HUB = "GitHub"
    BITBUCKET = "Bitbucket"

    def visit(
        self,
        aws_marketplace: typing.Callable[[], T_Result],
        git_hub: typing.Callable[[], T_Result],
        bitbucket: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribePublisherOutputIdentityProvider.AWS_MARKETPLACE:
            return aws_marketplace()
        if self is DescribePublisherOutputIdentityProvider.GIT_HUB:
            return git_hub()
        if self is DescribePublisherOutputIdentityProvider.BITBUCKET:
            return bitbucket()
