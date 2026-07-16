

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_manufacturer import NestedManufacturer
from .nested_tag import NestedTag


class Platform(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    manufacturer: typing.Optional[NestedManufacturer] = None
    name: str
    napalm_args: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Additional arguments to pass when initiating the NAPALM driver (JSON format)
    """

    napalm_driver: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the NAPALM driver to use when interacting with devices
    """

    slug: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None
    virtualmachine_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
