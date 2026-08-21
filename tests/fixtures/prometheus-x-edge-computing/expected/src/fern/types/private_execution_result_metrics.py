

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PrivateExecutionResultMetrics(UniversalBaseModel):
    """
    Collected execution metrics
    """

    ret: typing.Optional[int] = pydantic.Field(default=None)
    """
    Return value of the function
    """

    elapsed_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="elapsedTime"),
        pydantic.Field(alias="elapsedTime", description="Elapsed time of the function"),
    ] = None
    """
    Elapsed time of the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
