

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .circuit_circuit_termination import CircuitCircuitTermination
from .circuit_status import CircuitStatus
from .nested_circuit_type import NestedCircuitType
from .nested_provider import NestedProvider
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class Circuit(UniversalBaseModel):
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
    provider: NestedProvider
    status: typing.Optional[CircuitStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    termination_a: typing.Optional[CircuitCircuitTermination] = None
    termination_date: typing.Optional[dt.date] = None
    termination_z: typing.Optional[CircuitCircuitTermination] = None
    type: NestedCircuitType
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
