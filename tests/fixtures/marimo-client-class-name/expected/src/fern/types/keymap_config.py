

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .keymap_config_preset import KeymapConfigPreset


class KeymapConfig(UniversalBaseModel):
    """
    Configuration for keymaps.

        **Keys.**

        - `preset`: one of `"default"` or `"vim"`
        - `overrides`: a dict of keymap actions to their keymap override
        - `vimrc`: path to a vimrc file to load keymaps from
        - `destructive_delete`: if `True`, allows deleting cells with content.
    """

    destructive_delete: typing.Optional[bool] = None
    overrides: typing.Optional[typing.Dict[str, str]] = None
    preset: KeymapConfigPreset
    vimrc: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
