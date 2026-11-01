

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preset_list_preset_list_item import PresetListPresetListItem


class PresetList(UniversalBaseModel):
    preset_num: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of presets
    """

    preset_list: typing.Optional[typing.List[PresetListPresetListItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
