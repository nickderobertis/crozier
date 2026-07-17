

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExecuteChangeSetInput(UniversalBaseModel):
    """
    The input for the <a>ExecuteChangeSet</a> action.
    """

    change_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ChangeSetName"),
        pydantic.Field(
            alias="ChangeSetName",
            description="The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.",
        ),
    ]
    """
    The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.
    """

    stack_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName",
            description="If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.",
        ),
    ] = None
    """
    If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientRequestToken"),
        pydantic.Field(
            alias="ClientRequestToken",
            description="A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.",
        ),
    ] = None
    """
    A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.
    """

    disable_rollback: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="DisableRollback"),
        pydantic.Field(
            alias="DisableRollback",
            description="<p>Preserves the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>True</code> </p>",
        ),
    ] = None
    """
    <p>Preserves the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>True</code> </p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
