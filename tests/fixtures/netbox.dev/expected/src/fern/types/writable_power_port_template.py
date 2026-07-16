

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_power_port_template_type import WritablePowerPortTemplateType


class WritablePowerPortTemplate(UniversalBaseModel):
    allocated_draw: typing.Optional[int] = pydantic.Field(default=None)
    """
    Allocated power draw (watts)
    """

    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    device_type: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    last_updated: typing.Optional[dt.datetime] = None
    maximum_draw: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum power draw (watts)
    """

    module_type: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    type: typing.Optional[WritablePowerPortTemplateType] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
