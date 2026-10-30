

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BluetoothDeviceListListItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device name
    """

    ad: typing.Optional[str] = pydantic.Field(default=None)
    """
    MAC address
    """

    ct: typing.Optional[int] = pydantic.Field(default=None)
    """
    Connection type
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    Role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
