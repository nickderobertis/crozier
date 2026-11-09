

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatchJobRequests(UniversalBaseModel):
    """
    Operations to apply to a device
    """

    comment: typing.Optional[str] = None
    connectivity_assurance_disable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Disable connectivity assurance for the device
    """

    connectivity_assurance_enable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable connectivity assurance for the device
    """

    disable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Disable the device
    """

    enable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable the device
    """

    fleets_to_default: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fleet UIDs to assign to the device if it has no fleets
    """

    fleets_to_join: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fleet UIDs to add the device to
    """

    fleets_to_leave: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fleet UIDs to remove the device from
    """

    provision_product: typing.Optional[str] = pydantic.Field(default=None)
    """
    Product UID to provision the device with if not already provisioned
    """

    sn_to_default: typing.Optional[str] = pydantic.Field(default=None)
    """
    Set the device serial number only if not already set
    """

    sn_to_set: typing.Optional[str] = pydantic.Field(default=None)
    """
    Set the device serial number ("-" to clear)
    """

    vars_to_default: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Environment variables to set only if not already set
    """

    vars_to_set: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Environment variables to set (use "-" as value to clear)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
