

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id


class ServiceOfferingIcon(UniversalBaseModel):
    archived_at: typing.Optional[dt.datetime] = None
    created_at: typing.Optional[dt.datetime] = None
    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    Raw icon data
    """

    id: typing.Optional[Id] = None
    last_seen_at: typing.Optional[dt.datetime] = None
    refresh_state_part_id: typing.Optional[Id] = None
    source_id: typing.Optional[Id] = None
    source_ref: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
