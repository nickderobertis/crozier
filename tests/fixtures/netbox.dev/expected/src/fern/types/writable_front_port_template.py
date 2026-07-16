

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_front_port_template_type import WritableFrontPortTemplateType


class WritableFrontPortTemplate(UniversalBaseModel):
    color: typing.Optional[str] = None
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
    module_type: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    rear_port: int
    rear_port_position: typing.Optional[int] = None
    type: WritableFrontPortTemplateType
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
