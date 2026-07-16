

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_interface_template_poe_mode import WritableInterfaceTemplatePoeMode
from .writable_interface_template_poe_type import WritableInterfaceTemplatePoeType
from .writable_interface_template_type import WritableInterfaceTemplateType


class WritableInterfaceTemplate(UniversalBaseModel):
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
    mgmt_only: typing.Optional[bool] = None
    module_type: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    
    {module} is accepted as a substitution for the module bay position when attached to a module type.
    """

    poe_mode: typing.Optional[WritableInterfaceTemplatePoeMode] = None
    poe_type: typing.Optional[WritableInterfaceTemplatePoeType] = None
    type: WritableInterfaceTemplateType
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
