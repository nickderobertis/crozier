

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_entry import DisplayEntry


class ProfileDisplayEntry(UniversalBaseModel):
    display: typing.Optional[DisplayEntry] = None
    description: typing.Optional[DisplayEntry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
