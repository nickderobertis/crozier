

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DescribeChangeSetHooksInput(UniversalBaseModel):
    change_set_name: typing_extensions.Annotated[str, FieldMetadata(alias="ChangeSetName")] = pydantic.Field()
    """
    The name or Amazon Resource Name (ARN) of the change set that you want to describe.
    """

    stack_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackName")] = pydantic.Field(
        default=None
    )
    """
    If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    A string, provided by the <code>DescribeChangeSetHooks</code> response output, that identifies the next page of information that you want to retrieve.
    """

    logical_resource_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LogicalResourceId")] = (
        pydantic.Field(default=None)
    )
    """
    If specified, lists only the hooks related to the specified <code>LogicalResourceId</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
