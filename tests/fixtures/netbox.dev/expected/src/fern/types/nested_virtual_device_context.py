

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice


class NestedVirtualDeviceContext(UniversalBaseModel):
    device: NestedDevice
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    identifier: typing.Optional[int] = pydantic.Field(default=None)
    """
    Numeric identifier unique to the parent device
    """

    name: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
