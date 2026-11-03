

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_operator import AlertOperator
from .vent_alert_one_target import VentAlertOneTarget


class VentAlertOne(UniversalBaseModel):
    operator: AlertOperator
    target: VentAlertOneTarget

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
