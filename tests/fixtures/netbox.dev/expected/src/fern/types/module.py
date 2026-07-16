

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .module_status import ModuleStatus
from .nested_device import NestedDevice
from .nested_module_bay import NestedModuleBay
from .nested_module_type import NestedModuleType
from .nested_tag import NestedTag


class Module(UniversalBaseModel):
    asset_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique tag used to identify this device
    """

    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: NestedDevice
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    module_bay: NestedModuleBay
    module_type: typing.Optional[NestedModuleType] = None
    serial: typing.Optional[str] = None
    status: typing.Optional[ModuleStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
