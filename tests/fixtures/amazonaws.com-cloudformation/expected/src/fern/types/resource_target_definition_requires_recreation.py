

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceTargetDefinitionRequiresRecreation(enum.StrEnum):
    """
    If the <code>Attribute</code> value is <code>Properties</code>, indicates whether a change to this property causes the resource to be recreated. The value can be <code>Never</code>, <code>Always</code>, or <code>Conditionally</code>. To determine the conditions for a <code>Conditionally</code> recreation, see the update behavior for that <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">property</a> in the CloudFormation User Guide.
    """

    NEVER = "Never"
    CONDITIONALLY = "Conditionally"
    ALWAYS = "Always"

    def visit(
        self,
        never: typing.Callable[[], T_Result],
        conditionally: typing.Callable[[], T_Result],
        always: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceTargetDefinitionRequiresRecreation.NEVER:
            return never()
        if self is ResourceTargetDefinitionRequiresRecreation.CONDITIONALLY:
            return conditionally()
        if self is ResourceTargetDefinitionRequiresRecreation.ALWAYS:
            return always()
