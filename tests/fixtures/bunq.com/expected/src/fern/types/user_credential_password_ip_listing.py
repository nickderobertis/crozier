

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permitted_device import PermittedDevice


class UserCredentialPasswordIpListing(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the credential object's creation.
    """

    expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the status is PENDING_FIRST_USE: when the credential expires.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the credential.
    """

    permitted_device: typing.Optional[PermittedDevice] = pydantic.Field(default=None)
    """
    When the status is ACTIVE: the details of the device that may use the credential.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the credential.
    """

    token_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the status is PENDING_FIRST_USE: the value of the token.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the credential object's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
