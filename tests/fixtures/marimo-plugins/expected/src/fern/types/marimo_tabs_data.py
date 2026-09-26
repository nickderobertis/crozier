

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_tabs_data_orientation import MarimoTabsDataOrientation


class MarimoTabsData(UniversalBaseModel):
    tabs: typing.List[str]
    label: typing.Optional[str] = None
    orientation: typing.Optional[MarimoTabsDataOrientation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
