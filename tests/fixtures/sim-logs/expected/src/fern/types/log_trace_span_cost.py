

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LogTraceSpanCost(UniversalBaseModel):
    """
    Cost attributed to the span.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total span cost in USD.
    """

    input: typing.Optional[float] = pydantic.Field(default=None)
    """
    Input-token cost in USD.
    """

    output: typing.Optional[float] = pydantic.Field(default=None)
    """
    Output-token cost in USD.
    """

    tool_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="toolCost"),
        pydantic.Field(alias="toolCost", description="Tool cost in USD."),
    ] = None
    """
    Tool cost in USD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
