

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transect_kind import TransectKind
from .transect_legs_item_item import TransectLegsItemItem


class Transect(UniversalBaseModel):
    extent: typing.Optional[typing.List[typing.Any]] = None
    kind: TransectKind
    legs: typing.List[typing.List[TransectLegsItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
