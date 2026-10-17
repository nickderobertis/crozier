

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .start_experiment_response_status import StartExperimentResponseStatus
from .start_experiment_response_stop_reason import StartExperimentResponseStopReason


class StartExperimentResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Experiment id
    """

    name: str = pydantic.Field()
    """
    User-supplied experiment name
    """

    system_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="systemId"), pydantic.Field(alias="systemId", description="System id")
    ]
    """
    System id
    """

    channel: float = pydantic.Field()
    """
    Heater channel number
    """

    status: StartExperimentResponseStatus
    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="When the experiment (and PID) started"),
    ]
    """
    When the experiment (and PID) started
    """

    ended_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endedAt"),
        pydantic.Field(alias="endedAt", description="When the experiment ended; null while running"),
    ] = None
    """
    When the experiment ended; null while running
    """

    start_setpoint: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startSetpoint"),
        pydantic.Field(alias="startSetpoint", description="Target temp °C captured at start"),
    ] = None
    """
    Target temp °C captured at start
    """

    start_kp: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startKp"),
        pydantic.Field(alias="startKp", description="Kp captured at start"),
    ] = None
    """
    Kp captured at start
    """

    start_ki: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startKi"),
        pydantic.Field(alias="startKi", description="Ki captured at start"),
    ] = None
    """
    Ki captured at start
    """

    start_kd: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startKd"),
        pydantic.Field(alias="startKd", description="Kd captured at start"),
    ] = None
    """
    Kd captured at start
    """

    stop_reason: typing_extensions.Annotated[
        typing.Optional[StartExperimentResponseStopReason],
        FieldMetadata(alias="stopReason"),
        pydantic.Field(alias="stopReason"),
    ] = None
    stop_detail: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stopDetail"), pydantic.Field(alias="stopDetail")
    ] = None
    notes: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
