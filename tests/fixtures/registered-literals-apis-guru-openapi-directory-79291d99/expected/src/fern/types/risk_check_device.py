

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proxy_type import ProxyType
from .utc_offset import UtcOffset


class RiskCheckDevice(UniversalBaseModel):
    """
    Result summary object specifying values for `device` attributes of risk check.
    """

    ip_proxy_type: typing.Optional[ProxyType] = None
    ip_spam_list_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of spam lists the IP address is associated with if known.
    """

    ip_timezone_offset: typing.Optional[UtcOffset] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
