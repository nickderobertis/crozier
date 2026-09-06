

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_screenshots_screenshot import StoreItemScreenshotsScreenshot


class StoreItemScreenshots(UniversalBaseModel):
    all_ages_screenshots: typing.Optional[typing.List[StoreItemScreenshotsScreenshot]] = None
    mature_content_screenshots: typing.Optional[typing.List[StoreItemScreenshotsScreenshot]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
