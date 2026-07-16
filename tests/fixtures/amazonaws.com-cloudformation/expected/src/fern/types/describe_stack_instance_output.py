

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_stack_instance_output_stack_instance import DescribeStackInstanceOutputStackInstance


class DescribeStackInstanceOutput(UniversalBaseModel):
    stack_instance: typing_extensions.Annotated[
        typing.Optional[DescribeStackInstanceOutputStackInstance], FieldMetadata(alias="StackInstance")
    ] = pydantic.Field(default=None)
    """
    The stack instance that matches the specified request parameters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
