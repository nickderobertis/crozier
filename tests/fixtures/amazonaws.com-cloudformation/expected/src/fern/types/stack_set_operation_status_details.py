

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StackSetOperationStatusDetails(UniversalBaseModel):
    """
    Detailed information about the StackSet operation.
    """

    failed_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="FailedStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    The number of stack instances for which the StackSet operation failed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
