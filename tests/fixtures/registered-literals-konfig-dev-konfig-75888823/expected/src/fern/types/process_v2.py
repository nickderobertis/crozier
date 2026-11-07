

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
from .process_status import ProcessStatus
from .region import Region


class ProcessV2(UniversalBaseModel):
    status: ProcessStatus = pydantic.Field()
    """
    Process in drain will not accept any new rooms.
    """

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

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the process started being provisioned."),
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
