

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice
from .rack_unit_face import RackUnitFace


class RackUnit(UniversalBaseModel):
    device: typing.Optional[NestedDevice] = None
    display: typing.Optional[str] = None
    face: typing.Optional[RackUnitFace] = None
    id: typing.Optional[float] = None
    name: typing.Optional[str] = None
    occupied: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
