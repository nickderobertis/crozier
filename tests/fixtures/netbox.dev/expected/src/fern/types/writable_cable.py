

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_object import GenericObject
from .nested_tag import NestedTag
from .writable_cable_length_unit import WritableCableLengthUnit
from .writable_cable_status import WritableCableStatus
from .writable_cable_type import WritableCableType


class WritableCable(UniversalBaseModel):
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
    length_unit: typing.Optional[WritableCableLengthUnit] = None
    status: typing.Optional[WritableCableStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    type: typing.Optional[WritableCableType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
