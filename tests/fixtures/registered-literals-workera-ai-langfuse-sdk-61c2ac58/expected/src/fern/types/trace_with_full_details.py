

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .observations_view import ObservationsView
from .score import Score
from .trace import Trace


class TraceWithFullDetails(Trace):
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

    observations: typing.List[ObservationsView] = pydantic.Field()
    """
    List of observations
    """

    scores: typing.List[Score] = pydantic.Field()
    """
    List of scores
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
