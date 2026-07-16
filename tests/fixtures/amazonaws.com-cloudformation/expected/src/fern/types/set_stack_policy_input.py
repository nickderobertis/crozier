

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SetStackPolicyInput(UniversalBaseModel):
    """
    The input for the <a>SetStackPolicy</a> action.
    """

    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName", description="The name or unique stack ID that you want to associate a policy with."
        ),
    ]
    """
    The name or unique stack ID that you want to associate a policy with.
    """

    stack_policy_body: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackPolicyBody"),
        pydantic.Field(
            alias="StackPolicyBody",
            description='Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent updates to stack resources</a> in the CloudFormation User Guide. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.',
        ),
    ] = None
    """
    Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent updates to stack resources</a> in the CloudFormation User Guide. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    """

    stack_policy_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackPolicyURL"),
        pydantic.Field(
            alias="StackPolicyURL",
            description="Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.",
        ),
    ] = None
    """
    Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
