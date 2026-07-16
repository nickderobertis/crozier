

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cable_length_unit import CableLengthUnit
from .cable_status import CableStatus
from .cable_type import CableType
from .generic_object import GenericObject
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class Cable(UniversalBaseModel):
    a_terminations: typing.Optional[typing.List[GenericObject]] = None
    b_terminations: typing.Optional[typing.List[GenericObject]] = None
    color: typing.Optional[str] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = None
    last_updated: typing.Optional[dt.datetime] = None
    length: typing.Optional[float] = None
    length_unit: typing.Optional[CableLengthUnit] = None
    status: typing.Optional[CableStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    type: typing.Optional[CableType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
