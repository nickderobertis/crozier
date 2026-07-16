

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetStackPolicyOutput(UniversalBaseModel):
    """
    The output for the <a>GetStackPolicy</a> action.
    """

    stack_policy_body: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackPolicyBody")] = (
        pydantic.Field(default=None)
    )
    """
    Structure containing the stack policy body. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent Updates to Stack Resources</a> in the CloudFormation User Guide.)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
