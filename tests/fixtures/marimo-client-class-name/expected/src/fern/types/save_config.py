

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .save_config_autosave import SaveConfigAutosave


class SaveConfig(UniversalBaseModel):
    """
    Configuration for saving.

        **Keys.**

        - `autosave`: one of `"off"` or `"after_delay"`
        - `delay`: number of milliseconds to wait before autosaving
        - `format_on_save`: if `True`, format the code on save
    """

    autosave: SaveConfigAutosave
    autosave_delay: int
    format_on_save: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
