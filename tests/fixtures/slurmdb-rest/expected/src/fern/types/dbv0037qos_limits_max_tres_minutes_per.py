

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_tres_minutes_per_account_item import Dbv0037QosLimitsMaxTresMinutesPerAccountItem
from .dbv0037qos_limits_max_tres_minutes_per_job_item import Dbv0037QosLimitsMaxTresMinutesPerJobItem
from .dbv0037qos_limits_max_tres_minutes_per_user_item import Dbv0037QosLimitsMaxTresMinutesPerUserItem


class Dbv0037QosLimitsMaxTresMinutesPer(UniversalBaseModel):
    """
    Max TRES minutes per settings
    """

    job: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresMinutesPerJobItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    account: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresMinutesPerAccountItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    user: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresMinutesPerUserItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
