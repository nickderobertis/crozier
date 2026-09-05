

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_about import AppAbout
from .app_legal import AppLegal


class App(UniversalBaseModel):
    about: typing.Optional[AppAbout] = None
    id: int
    legal: typing.Optional[AppLegal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
