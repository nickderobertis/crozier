

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_hook import ChangeSetHook
from .describe_change_set_hooks_output_status import DescribeChangeSetHooksOutputStatus


class DescribeChangeSetHooksOutput(UniversalBaseModel):
    change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The change set identifier (stack ID).
    """

    change_set_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetName")] = (
        pydantic.Field(default=None)
    )
    """
    The change set name.
    """

    hooks: typing_extensions.Annotated[typing.Optional[typing.List[ChangeSetHook]], FieldMetadata(alias="Hooks")] = (
        pydantic.Field(default=None)
    )
    """
    List of hook objects.
    """

    status: typing_extensions.Annotated[
        typing.Optional[DescribeChangeSetHooksOutputStatus], FieldMetadata(alias="Status")
    ] = pydantic.Field(default=None)
    """
    Provides the status of the change set hook.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    Pagination token, <code>null</code> or empty if no more results.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    The stack identifier (stack ID).
    """

    stack_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackName")] = pydantic.Field(
        default=None
    )
    """
    The stack name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
