

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_stack_set_operation_output_stack_set_operation import DescribeStackSetOperationOutputStackSetOperation


class DescribeStackSetOperationOutput(UniversalBaseModel):
    stack_set_operation: typing_extensions.Annotated[
        typing.Optional[DescribeStackSetOperationOutputStackSetOperation], FieldMetadata(alias="StackSetOperation")
    ] = pydantic.Field(default=None)
    """
    The specified stack set operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
