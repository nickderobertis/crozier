

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_about_website import AppAboutWebsite


class AppAbout(UniversalBaseModel):
    description: typing.Optional[str] = None
    name: typing.Optional[str] = None
    website: typing.Optional[AppAboutWebsite] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
