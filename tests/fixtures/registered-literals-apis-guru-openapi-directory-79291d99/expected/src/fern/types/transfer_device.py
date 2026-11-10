

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferDevice(UniversalBaseModel):
    """
    Information about the device being used to initiate the authorization.
    """

    ip_address: str = pydantic.Field()
    """
    The IP address of the device being used to initiate the authorization.
    """

    user_agent: str = pydantic.Field()
    """
    The user agent of the device being used to initiate the authorization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
