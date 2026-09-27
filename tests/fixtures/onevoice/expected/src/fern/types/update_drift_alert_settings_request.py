

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_drift_alert_settings_request_locale import UpdateDriftAlertSettingsRequestLocale


class UpdateDriftAlertSettingsRequest(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    locale: UpdateDriftAlertSettingsRequestLocale

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
