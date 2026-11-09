

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .trace import Trace


class TraceWithDetails(Trace):
    html_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="htmlPath"),
        pydantic.Field(alias="htmlPath", description="Path of trace in Langfuse UI"),
    ]
    """
    Path of trace in Langfuse UI
    """

    latency: float = pydantic.Field()
    """
    Latency of trace in seconds
    """

    total_cost: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalCost"), pydantic.Field(alias="totalCost", description="Cost of trace in USD")
    ]
    """
    Cost of trace in USD
    """

    observations: typing.List[str] = pydantic.Field()
    """
    List of observation ids
    """

    scores: typing.List[str] = pydantic.Field()
    """
    List of score ids
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
