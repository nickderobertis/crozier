

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ToolsToolNamePostResponseData(UniversalBaseModel):
    result: typing.Any
    tool: str = pydantic.Field()
    """
    Name of the executed tool
    """

    execution_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="executionTime"),
        pydantic.Field(alias="executionTime", description="Execution time in milliseconds"),
    ] = None
    """
    Execution time in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
