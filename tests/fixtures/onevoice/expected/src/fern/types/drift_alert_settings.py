

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .drift_alert_settings_locale import DriftAlertSettingsLocale


class DriftAlertSettings(UniversalBaseModel):
    enabled: bool = pydantic.Field()
    """
    Whether private drift notifications are enabled. Defaults to false.
    """

    locale: DriftAlertSettingsLocale

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
