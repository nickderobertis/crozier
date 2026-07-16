

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_power_outlet_template_feed_leg import WritablePowerOutletTemplateFeedLeg
from .writable_power_outlet_template_type import WritablePowerOutletTemplateType


class WritablePowerOutletTemplate(UniversalBaseModel):
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    device_type: typing.Optional[int] = None
    display: typing.Optional[str] = None
    feed_leg: typing.Optional[WritablePowerOutletTemplateFeedLeg] = pydantic.Field(default=None)
    """
    Phase (for three-phase feeds)
    """

    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    module_type: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    power_port: typing.Optional[int] = None
    type: typing.Optional[WritablePowerOutletTemplateType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
