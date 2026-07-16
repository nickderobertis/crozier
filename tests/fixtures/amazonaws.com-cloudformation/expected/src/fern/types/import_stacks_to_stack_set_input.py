

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .import_stacks_to_stack_set_input_call_as import ImportStacksToStackSetInputCallAs
from .organizational_unit_id import OrganizationalUnitId
from .stack_id import StackId
from .stack_set_operation_preferences import StackSetOperationPreferences


class ImportStacksToStackSetInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackSetName")] = pydantic.Field()
    """
    The name of the stack set. The name must be unique in the Region where you create your stack set.
    """

    stack_ids: typing_extensions.Annotated[typing.Optional[typing.List[StackId]], FieldMetadata(alias="StackIds")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The IDs of the stacks you are importing into a stack set. You import up to 10 stacks per stack set at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
    """

    stack_ids_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackIdsUrl")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
    """

    organizational_unit_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganizationalUnitId]], FieldMetadata(alias="OrganizationalUnitIds")
    ] = pydantic.Field(default=None)
    """
    The list of OU ID's to which the stacks being imported has to be mapped as deployment target.
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[StackSetOperationPreferences], FieldMetadata(alias="OperationPreferences")
    ] = None
    operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="OperationId")] = (
        pydantic.Field(default=None)
    )
    """
    A unique, user defined, identifier for the stack set operation.
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[ImportStacksToStackSetInputCallAs], FieldMetadata(alias="CallAs")
    ] = pydantic.Field(default=None)
    """
    <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed stack sets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
