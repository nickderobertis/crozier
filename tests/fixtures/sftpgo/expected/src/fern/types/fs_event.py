

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_protocols import EventProtocols
from .fs_event_action import FsEventAction
from .fs_event_status import FsEventStatus
from .fs_providers import FsProviders


class FsEvent(UniversalBaseModel):
    id: typing.Optional[str] = None
    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    unix timestamp in nanoseconds
    """

    action: typing.Optional[FsEventAction] = None
    username: typing.Optional[str] = None
    fs_path: typing.Optional[str] = None
    fs_target_path: typing.Optional[str] = None
    virtual_path: typing.Optional[str] = None
    virtual_target_path: typing.Optional[str] = None
    ssh_cmd: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    elapsed: typing.Optional[int] = pydantic.Field(default=None)
    """
    elapsed time as milliseconds
    """

    status: typing.Optional[FsEventStatus] = None
    protocol: typing.Optional[EventProtocols] = None
    ip: typing.Optional[str] = None
    session_id: typing.Optional[str] = None
    fs_provider: typing.Optional[FsProviders] = None
    bucket: typing.Optional[str] = None
    endpoint: typing.Optional[str] = None
    open_flags: typing.Optional[str] = None
    role: typing.Optional[str] = None
    instance_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
