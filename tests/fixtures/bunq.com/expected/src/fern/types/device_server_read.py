

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceServerRead(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the DeviceServer's creation.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the DeviceServer.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the DeviceServer as created on the server.
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ip address which was used to create the DeviceServer.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the DeviceServer. Can be ACTIVE, BLOCKED, NEEDS_CONFIRMATION or OBSOLETE.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the DeviceServer's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
