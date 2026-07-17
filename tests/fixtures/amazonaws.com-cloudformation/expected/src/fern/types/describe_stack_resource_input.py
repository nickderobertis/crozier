

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DescribeStackResourceInput(UniversalBaseModel):
    """
    The input for <a>DescribeStackResource</a> action.
    """

    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName",
            description="<p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>",
        ),
    ]
    """
    <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    """

    logical_resource_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogicalResourceId"),
        pydantic.Field(
            alias="LogicalResourceId",
            description="<p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>",
        ),
    ]
    """
    <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
