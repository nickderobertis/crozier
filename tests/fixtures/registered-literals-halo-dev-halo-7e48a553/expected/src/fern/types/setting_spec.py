

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .setting_form import SettingForm


class SettingSpec(UniversalBaseModel):
    """
    Collection of form groups that make up this setting definition.
    """

    forms: typing.List[SettingForm] = pydantic.Field()
    """
    Form groups rendered for this setting definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
