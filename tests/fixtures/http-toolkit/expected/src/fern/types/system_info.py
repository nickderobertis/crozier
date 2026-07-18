

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SystemInfo(UniversalBaseModel):
    """
    System information
    """

    hostname: str
    os: str
    architecture: str
    cpu_count: typing_extensions.Annotated[int, FieldMetadata(alias="cpuCount"), pydantic.Field(alias="cpuCount")]
    memory: str
    go_version: typing_extensions.Annotated[str, FieldMetadata(alias="goVersion"), pydantic.Field(alias="goVersion")]
    client_addr: typing_extensions.Annotated[str, FieldMetadata(alias="clientAddr"), pydantic.Field(alias="clientAddr")]
    server_host: typing_extensions.Annotated[str, FieldMetadata(alias="serverHost"), pydantic.Field(alias="serverHost")]
    uptime: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
