

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_usage import DataUsage


class CellularPlan(UniversalBaseModel):
    activated: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp of when the SIM was activated
    """

    data_usage: typing.Optional[DataUsage] = None
    expires_at: typing.Optional[int] = None
    iccid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Integrated Circuit Card Identifier of the SIM card
    """

    imsi: typing.Optional[str] = pydantic.Field(default=None)
    """
    IMSI of the SIM card
    """

    last_updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time this plan information was last updated
    """

    lifetime_used: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total bytes used by this SIM
    """

    plan_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the SIM plan type including data allowance, region, and validity period
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
