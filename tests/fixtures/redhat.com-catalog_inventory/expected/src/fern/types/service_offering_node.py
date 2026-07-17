

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class ServiceOfferingNode(UniversalBaseModel):
    archived_at: typing.Optional[dt.datetime] = None
    created_at: typing.Optional[dt.datetime] = None
    extra: typing.Optional[typing.Dict[str, typing.Any]] = None
    id: typing.Optional[Id] = None
    last_seen_at: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    refresh_state_part_id: typing.Optional[Id] = None
    root_service_offering_id: typing.Optional[Id] = None
    service_inventory_id: typing.Optional[Id] = None
    service_offering_id: typing.Optional[Id] = None
    source_created_at: typing.Optional[dt.datetime] = None
    source_id: typing.Optional[Id] = None
    source_ref: typing.Optional[str] = None
    source_updated_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
