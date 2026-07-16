

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeSummaryPublisherIdentity(enum.StrEnum):
    """
    <p>The service used to verify the publisher identity.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Registering your account to publish CloudFormation extensions</a> in the <i> CFN-CLI User Guide for Extension Development</i>.</p>
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
        if self is TypeSummaryPublisherIdentity.AWS_MARKETPLACE:
            return aws_marketplace()
        if self is TypeSummaryPublisherIdentity.GIT_HUB:
            return git_hub()
        if self is TypeSummaryPublisherIdentity.BITBUCKET:
            return bitbucket()
