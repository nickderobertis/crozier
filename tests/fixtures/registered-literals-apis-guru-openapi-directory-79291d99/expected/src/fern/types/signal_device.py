

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SignalDevice(UniversalBaseModel):
    """
    Details about the end user's device
    """

    ip_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the device that initiated the transaction
    """

    user_agent: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user agent of the device that initiated the transaction (e.g. "Mozilla/5.0")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
