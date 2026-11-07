

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_preferences_form_theme import UpdatePreferencesFormTheme


class UpdatePreferencesForm(UniversalBaseModel):
    theme: UpdatePreferencesFormTheme
    timezone: str
    daily_digest: typing.Optional[bool] = None
    weekly_limit: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
