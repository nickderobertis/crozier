

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_circuit_status import WritableCircuitStatus


class WritableCircuit(UniversalBaseModel):
    cid: str
    comments: typing.Optional[str] = None
    commit_rate: typing.Optional[int] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    install_date: typing.Optional[dt.date] = None
    last_updated: typing.Optional[dt.datetime] = None
    provider: int
    status: typing.Optional[WritableCircuitStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    termination_a: typing.Optional[int] = None
    termination_date: typing.Optional[dt.date] = None
    termination_z: typing.Optional[int] = None
    type: int
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
