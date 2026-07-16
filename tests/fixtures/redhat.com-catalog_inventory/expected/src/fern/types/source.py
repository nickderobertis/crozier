

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class Source(UniversalBaseModel):
    archived_at: typing.Optional[dt.datetime] = None
    availability_message: typing.Optional[str] = None
    availability_status: typing.Optional[str] = None
    cloud_connector_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[Id] = None
    info: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    last_available_at: typing.Optional[dt.datetime] = None
    last_checked_at: typing.Optional[dt.datetime] = None
    last_refresh_message: typing.Optional[str] = None
    last_successful_refresh_at: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    previous_sha: typing.Optional[str] = None
    previous_size: typing.Optional[int] = None
    refresh_finished_at: typing.Optional[dt.datetime] = None
    refresh_started_at: typing.Optional[dt.datetime] = None
    refresh_state: typing.Optional[str] = None
    refresh_task_id: typing.Optional[str] = None
    uid: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
