

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device_type import NestedDeviceType
from .nested_module_type import NestedModuleType
from .nested_power_port_template import NestedPowerPortTemplate
from .power_outlet_template_feed_leg import PowerOutletTemplateFeedLeg
from .power_outlet_template_type import PowerOutletTemplateType


class PowerOutletTemplate(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    device_type: typing.Optional[NestedDeviceType] = None
    display: typing.Optional[str] = None
    feed_leg: typing.Optional[PowerOutletTemplateFeedLeg] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    module_type: typing.Optional[NestedModuleType] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    power_port: typing.Optional[NestedPowerPortTemplate] = None
    type: typing.Optional[PowerOutletTemplateType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
