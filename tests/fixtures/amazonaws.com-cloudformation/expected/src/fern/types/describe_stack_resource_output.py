

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_stack_resource_output_stack_resource_detail import DescribeStackResourceOutputStackResourceDetail


class DescribeStackResourceOutput(UniversalBaseModel):
    """
    The output for a <a>DescribeStackResource</a> action.
    """

    stack_resource_detail: typing_extensions.Annotated[
        typing.Optional[DescribeStackResourceOutputStackResourceDetail], FieldMetadata(alias="StackResourceDetail")
    ] = pydantic.Field(default=None)
    """
    A <code>StackResourceDetail</code> structure containing the description of the specified resource in the specified stack.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
