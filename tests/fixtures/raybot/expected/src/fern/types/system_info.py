

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SystemInfo(UniversalBaseModel):
    local_ip: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="localIp"),
        pydantic.Field(alias="localIp", description="The local IP address of the system"),
    ]
    """
    The local IP address of the system
    """

    cpu_usage: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="cpuUsage"),
        pydantic.Field(alias="cpuUsage", description="The CPU usage of the system in percentage"),
    ]
    """
    The CPU usage of the system in percentage
    """

    memory_usage: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="memoryUsage"),
        pydantic.Field(alias="memoryUsage", description="The memory usage of the system in percentage"),
    ]
    """
    The memory usage of the system in percentage
    """

    total_memory: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalMemory"),
        pydantic.Field(alias="totalMemory", description="The total memory of the system in MB"),
    ]
    """
    The total memory of the system in MB
    """

    uptime: float = pydantic.Field()
    """
    The uptime of the system in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
