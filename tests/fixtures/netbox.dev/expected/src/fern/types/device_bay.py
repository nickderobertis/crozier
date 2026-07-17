

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice
from .nested_tag import NestedTag


class DeviceBay(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: NestedDevice
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    installed_device: typing.Optional[NestedDevice] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    name: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
