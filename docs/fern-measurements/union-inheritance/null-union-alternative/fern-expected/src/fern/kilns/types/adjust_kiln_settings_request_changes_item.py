

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .adjust_kiln_settings_request_changes_item_reading import AdjustKilnSettingsRequestChangesItemReading


class AdjustKilnSettingsRequestChangesItem(UniversalBaseModel):
    setting: str
    reading: typing.Optional[AdjustKilnSettingsRequestChangesItemReading] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
