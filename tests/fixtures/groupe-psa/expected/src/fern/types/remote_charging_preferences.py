

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_charging_preferences_level import RemoteChargingPreferencesLevel
from .remote_charging_preferences_type import RemoteChargingPreferencesType


class RemoteChargingPreferences(UniversalBaseModel):
    """
    Set the charging preferences.
    """

    level: typing.Optional[RemoteChargingPreferencesLevel] = pydantic.Field(default=None)
    """
    Charging power level.
    """

    type: typing.Optional[RemoteChargingPreferencesType] = pydantic.Field(default=None)
    """
    Configure charging type preferences.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
