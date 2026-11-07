

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .build_id import BuildId
from .container_port import ContainerPort
from .deployment_id import DeploymentId
from .deployment_v2env_item import DeploymentV2EnvItem
from .num_rooms_per_process import NumRoomsPerProcess


class DeploymentV2(UniversalBaseModel):
    idle_timeout_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="idleTimeoutEnabled"),
        pydantic.Field(
            alias="idleTimeoutEnabled",
            description="Option to shut down processes that have had no new connections or rooms\nfor five minutes.",
        ),
    ]
    """
    Option to shut down processes that have had no new connections or rooms
    for five minutes.
    """

    env: typing.List[DeploymentV2EnvItem] = pydantic.Field()
    """
    The environment variable that our process will have access to at runtime.
    """

    rooms_per_process: typing_extensions.Annotated[
        NumRoomsPerProcess, FieldMetadata(alias="roomsPerProcess"), pydantic.Field(alias="roomsPerProcess")
    ]
    additional_container_ports: typing_extensions.Annotated[
        typing.List[ContainerPort],
        FieldMetadata(alias="additionalContainerPorts"),
        pydantic.Field(alias="additionalContainerPorts", description="Additional ports your server listens on."),
    ]
    """
    Additional ports your server listens on.
    """

    default_container_port: typing_extensions.Annotated[
        ContainerPort,
        FieldMetadata(alias="defaultContainerPort"),
        pydantic.Field(alias="defaultContainerPort", description="Describes the primary port your process listens on."),
    ]
    """
    Describes the primary port your process listens on.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the deployment was created."),
    ]
    """
    When the deployment was created.
    """

    created_by: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdBy"),
        pydantic.Field(
            alias="createdBy", description="UserId or email address for the user that created the deployment."
        ),
    ]
    """
    UserId or email address for the user that created the deployment.
    """

    requested_memory_mb: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="requestedMemoryMB"),
        pydantic.Field(alias="requestedMemoryMB", description="The amount of memory allocated to your process."),
    ]
    """
    The amount of memory allocated to your process.
    """

    requested_cpu: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="requestedCPU"),
        pydantic.Field(alias="requestedCPU", description="The number of cores allocated to your process."),
    ]
    """
    The number of cores allocated to your process.
    """

    deployment_id: typing_extensions.Annotated[
        DeploymentId, FieldMetadata(alias="deploymentId"), pydantic.Field(alias="deploymentId")
    ]
    build_id: typing_extensions.Annotated[BuildId, FieldMetadata(alias="buildId"), pydantic.Field(alias="buildId")]
    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
