

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .health import Health
from .status1 import Status1


class ContainerState(UniversalBaseModel):
    """
    ContainerState stores container's running state. It's part of ContainerJSONBase
    and will be returned by the "inspect" command.
    """

    status: typing_extensions.Annotated[
        typing.Optional[Status1],
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description='String representation of the container state. Can be one of "created",\n"running", "paused", "restarting", "removing", "exited", or "dead".',
        ),
    ] = None
    """
    String representation of the container state. Can be one of "created",
    "running", "paused", "restarting", "removing", "exited", or "dead".
    """

    running: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Running"),
        pydantic.Field(
            alias="Running",
            description='Whether this container is running.\n\nNote that a running container can be _paused_. The `Running` and `Paused`\nbooleans are not mutually exclusive:\n\nWhen pausing a container (on Linux), the freezer cgroup is used to suspend\nall processes in the container. Freezing the process requires the process to\nbe running. As a result, paused containers are both `Running` _and_ `Paused`.\n\nUse the `Status` field instead to determine if a container\'s state is "running".',
        ),
    ] = None
    """
    Whether this container is running.
    
    Note that a running container can be _paused_. The `Running` and `Paused`
    booleans are not mutually exclusive:
    
    When pausing a container (on Linux), the freezer cgroup is used to suspend
    all processes in the container. Freezing the process requires the process to
    be running. As a result, paused containers are both `Running` _and_ `Paused`.
    
    Use the `Status` field instead to determine if a container's state is "running".
    """

    paused: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Paused"),
        pydantic.Field(alias="Paused", description="Whether this container is paused."),
    ] = None
    """
    Whether this container is paused.
    """

    restarting: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Restarting"),
        pydantic.Field(alias="Restarting", description="Whether this container is restarting."),
    ] = None
    """
    Whether this container is restarting.
    """

    oom_killed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="OOMKilled"),
        pydantic.Field(
            alias="OOMKilled",
            description="Whether a process within this container has been killed because it ran\nout of memory since the container was last started.",
        ),
    ] = None
    """
    Whether a process within this container has been killed because it ran
    out of memory since the container was last started.
    """

    dead: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="Dead"), pydantic.Field(alias="Dead")
    ] = None
    pid: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Pid"),
        pydantic.Field(alias="Pid", description="The process ID of this container"),
    ] = None
    """
    The process ID of this container
    """

    exit_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ExitCode"),
        pydantic.Field(alias="ExitCode", description="The last exit code of this container"),
    ] = None
    """
    The last exit code of this container
    """

    error: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Error"), pydantic.Field(alias="Error")
    ] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StartedAt"),
        pydantic.Field(alias="StartedAt", description="The time when this container was last started."),
    ] = None
    """
    The time when this container was last started.
    """

    finished_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FinishedAt"),
        pydantic.Field(alias="FinishedAt", description="The time when this container last exited."),
    ] = None
    """
    The time when this container last exited.
    """

    health: typing_extensions.Annotated[
        typing.Optional[Health], FieldMetadata(alias="Health"), pydantic.Field(alias="Health")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
