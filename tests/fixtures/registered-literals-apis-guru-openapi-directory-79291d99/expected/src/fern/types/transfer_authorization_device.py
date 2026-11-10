

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferAuthorizationDevice(UniversalBaseModel):
    """
    Information about the device being used to initiate the authorization.
    """

    ip_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the device being used to initiate the authorization. Required for Guarantee.
    """

    user_agent: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user agent of the device being used to initiate the authorization. Required for Guarantee.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
