

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountLimit(UniversalBaseModel):
    """
    <p>The AccountLimit data type.</p> <p>CloudFormation has the following limits per account:</p> <ul> <li> <p>Number of concurrent resources</p> </li> <li> <p>Number of stacks</p> </li> <li> <p>Number of stack outputs</p> </li> </ul> <p>For more information about these account limits, and other CloudFormation limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Name")] = pydantic.Field(default=None)
    """
    <p>The name of the account limit.</p> <p>Values: <code>ConcurrentResourcesLimit</code> | <code>StackLimit</code> | <code>StackOutputsLimit</code> </p>
    """

    value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="Value")] = pydantic.Field(
        default=None
    )
    """
    The value that's associated with the account limit name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
