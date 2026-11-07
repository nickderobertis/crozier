

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SimUsage(UniversalBaseModel):
    iccid: typing.Optional[str] = pydantic.Field(default=None)
    """
    ICCID of the SIM card
    """

    last_updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time this usage information was last updated
    """

    lifetime_used: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of bytes used by SIM
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Limit in bytes of the SIMs current data plan
    """

    used: typing.Optional[int] = pydantic.Field(default=None)
    """
    Bytes used on the SIMs current data plan
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
