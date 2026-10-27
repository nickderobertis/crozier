

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preview_config_time_stratified_selects_item_selects_item import PreviewConfigTimeStratifiedSelectsItemSelectsItem


class PreviewConfigTimeStratifiedSelectsItem(UniversalBaseModel):
    description: typing.Optional[str] = None
    label: typing.Optional[str] = None
    selects: typing.Optional[typing.List[PreviewConfigTimeStratifiedSelectsItemSelectsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
