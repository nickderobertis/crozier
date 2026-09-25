

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_alarm_status_activation import BaseAlarmStatusActivation


class BaseAlarmStatus(UniversalBaseModel):
    """
    Describe a vehicle alarm status.
    """

    activation: BaseAlarmStatusActivation = pydantic.Field()
    """
    Define whether the vehicle alarm is active or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
