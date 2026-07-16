

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceCode(UniversalBaseModel):
    """ """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique code that can be used to login.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    When this DeviceCode was created. Timestamp in RFC 3339 format.
    """

    device_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the device that used this code. Populated when the device is paired up.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id for this device code.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location assigned to this code.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional user-defined name for the device code.
    """

    pair_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    When this DeviceCode will expire and no longer login. Timestamp in RFC 3339 format.
    """

    paired_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    When this DeviceCode was paired. Timestamp in RFC 3339 format.
    """

    product_type: str = pydantic.Field()
    """
    The targeting product type of the device code.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pairing status of the device code.
    """

    status_changed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    When this DeviceCode's status was last changed. Timestamp in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
