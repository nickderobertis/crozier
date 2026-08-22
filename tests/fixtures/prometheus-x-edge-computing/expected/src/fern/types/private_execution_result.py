

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_id import DataId
from .function_id import FunctionId
from .private_execution_result_metrics import PrivateExecutionResultMetrics


class PrivateExecutionResult(UniversalBaseModel):
    """
    The result of the function execution on data
    """

    uuid_: typing_extensions.Annotated[
        str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="Unique operation identifier")
    ]
    """
    Unique operation identifier
    """

    function: FunctionId
    private_data: DataId
    metrics: typing.Optional[PrivateExecutionResultMetrics] = pydantic.Field(default=None)
    """
    Collected execution metrics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
