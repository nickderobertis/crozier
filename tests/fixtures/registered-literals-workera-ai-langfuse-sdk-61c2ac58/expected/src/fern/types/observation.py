

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_value import MapValue
from .observation_level import ObservationLevel
from .usage import Usage


class Observation(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of the observation
    """

    trace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="traceId"),
        pydantic.Field(alias="traceId", description="The trace ID associated with the observation"),
    ] = None
    """
    The trace ID associated with the observation
    """

    type: str = pydantic.Field()
    """
    The type of the observation
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the observation
    """

    start_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="The start time of the observation"),
    ]
    """
    The start time of the observation
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="The end time of the observation."),
    ] = None
    """
    The end time of the observation.
    """

    completion_start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completionStartTime"),
        pydantic.Field(alias="completionStartTime", description="The completion start time of the observation"),
    ] = None
    """
    The completion start time of the observation
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model used for the observation
    """

    model_parameters: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[MapValue]]],
        FieldMetadata(alias="modelParameters"),
        pydantic.Field(alias="modelParameters", description="The parameters of the model used for the observation"),
    ] = None
    """
    The parameters of the model used for the observation
    """

    input: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The input data of the observation
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the observation
    """

    metadata: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Additional metadata of the observation
    """

    output: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The output data of the observation
    """

    usage: typing.Optional[Usage] = pydantic.Field(default=None)
    """
    (Deprecated. Use usageDetails and costDetails instead.) The usage data of the observation
    """

    level: ObservationLevel = pydantic.Field()
    """
    The level of the observation
    """

    status_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statusMessage"),
        pydantic.Field(alias="statusMessage", description="The status message of the observation"),
    ] = None
    """
    The status message of the observation
    """

    parent_observation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentObservationId"),
        pydantic.Field(alias="parentObservationId", description="The parent observation ID"),
    ] = None
    """
    The parent observation ID
    """

    prompt_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="promptId"),
        pydantic.Field(alias="promptId", description="The prompt ID associated with the observation"),
    ] = None
    """
    The prompt ID associated with the observation
    """

    usage_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[int]]],
        FieldMetadata(alias="usageDetails"),
        pydantic.Field(
            alias="usageDetails",
            description="The usage details of the observation. Key is the name of the usage metric, value is the number of units consumed. The total key is the sum of all (non-total) usage metrics or the total value ingested.",
        ),
    ] = None
    """
    The usage details of the observation. Key is the name of the usage metric, value is the number of units consumed. The total key is the sum of all (non-total) usage metrics or the total value ingested.
    """

    cost_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[float]]],
        FieldMetadata(alias="costDetails"),
        pydantic.Field(
            alias="costDetails",
            description="The cost details of the observation. Key is the name of the cost metric, value is the cost in USD. The total key is the sum of all (non-total) cost metrics or the total value ingested.",
        ),
    ] = None
    """
    The cost details of the observation. Key is the name of the cost metric, value is the cost in USD. The total key is the sum of all (non-total) cost metrics or the total value ingested.
    """

    environment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The environment from which this observation originated. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
