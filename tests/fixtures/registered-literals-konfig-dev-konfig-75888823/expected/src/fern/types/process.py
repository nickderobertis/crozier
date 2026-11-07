

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .deployment_id import DeploymentId
from .exposed_port import ExposedPort
from .num_rooms_per_process import NumRoomsPerProcess
from .process_id import ProcessId
from .region import Region


class Process(UniversalBaseModel):
    """
    A process object represents a runtime instance of your game server and its metadata.
    """

    egressed_bytes: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="egressedBytes"),
        pydantic.Field(alias="egressedBytes", description="Measures network traffic leaving the process in bytes."),
    ]
    """
    Measures network traffic leaving the process in bytes.
    """

    idle_since: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="idleSince"), pydantic.Field(alias="idleSince")
    ] = None
    active_connections_updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="activeConnectionsUpdatedAt"),
        pydantic.Field(alias="activeConnectionsUpdatedAt"),
    ]
    active_connections: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="activeConnections"),
        pydantic.Field(alias="activeConnections", description="Tracks the number of active connections to a process."),
    ]
    """
    Tracks the number of active connections to a process.
    """

    rooms_allocated_updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="roomsAllocatedUpdatedAt"), pydantic.Field(alias="roomsAllocatedUpdatedAt")
    ]
    rooms_allocated: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="roomsAllocated"),
        pydantic.Field(
            alias="roomsAllocated", description="Tracks the number of rooms that have been allocated to the process."
        ),
    ]
    """
    Tracks the number of rooms that have been allocated to the process.
    """

    room_slots_available_updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="roomSlotsAvailableUpdatedAt"),
        pydantic.Field(alias="roomSlotsAvailableUpdatedAt"),
    ]
    room_slots_available: typing_extensions.Annotated[
        float, FieldMetadata(alias="roomSlotsAvailable"), pydantic.Field(alias="roomSlotsAvailable")
    ]
    draining: bool = pydantic.Field()
    """
    Process in drain will not accept any new rooms.
    """

    terminated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="terminatedAt"),
        pydantic.Field(alias="terminatedAt", description="When the process has been terminated."),
    ] = None
    """
    When the process has been terminated.
    """

    stopping_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="stoppingAt"),
        pydantic.Field(
            alias="stoppingAt",
            description="When the process is issued to stop. We use this to determine when we should stop billing.",
        ),
    ] = None
    """
    When the process is issued to stop. We use this to determine when we should stop billing.
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startedAt"),
        pydantic.Field(
            alias="startedAt",
            description="When the process bound to the specified port. We use this to determine when we should start billing.",
        ),
    ] = None
    """
    When the process bound to the specified port. We use this to determine when we should start billing.
    """

    starting_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startingAt"),
        pydantic.Field(alias="startingAt", description="When the process started being provisioned."),
    ]
    """
    When the process started being provisioned.
    """

    rooms_per_process: typing_extensions.Annotated[
        NumRoomsPerProcess, FieldMetadata(alias="roomsPerProcess"), pydantic.Field(alias="roomsPerProcess")
    ]
    additional_exposed_ports: typing_extensions.Annotated[
        typing.List[ExposedPort],
        FieldMetadata(alias="additionalExposedPorts"),
        pydantic.Field(alias="additionalExposedPorts"),
    ]
    exposed_port: typing_extensions.Annotated[
        typing.Optional[ExposedPort], FieldMetadata(alias="exposedPort"), pydantic.Field(alias="exposedPort")
    ] = None
    port: float
    host: str
    region: Region
    process_id: typing_extensions.Annotated[
        ProcessId, FieldMetadata(alias="processId"), pydantic.Field(alias="processId")
    ]
    deployment_id: typing_extensions.Annotated[
        DeploymentId, FieldMetadata(alias="deploymentId"), pydantic.Field(alias="deploymentId")
    ]
    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
