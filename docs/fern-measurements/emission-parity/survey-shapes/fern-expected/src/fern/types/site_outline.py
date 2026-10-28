

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marker_at import MarkerAt
from .quadrats_cells_item_item_item import QuadratsCellsItemItemItem
from .transect_legs_item_item import TransectLegsItemItem


class SiteOutline_Marker(UniversalBaseModel):
    kind: typing.Literal["Marker"] = "Marker"
    extent: typing.Optional[typing.List[typing.Any]] = None
    at: MarkerAt

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SiteOutline_Transect(UniversalBaseModel):
    kind: typing.Literal["Transect"] = "Transect"
    extent: typing.Optional[typing.List[typing.Any]] = None
    legs: typing.List[typing.List[TransectLegsItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SiteOutline_Quadrats(UniversalBaseModel):
    kind: typing.Literal["Quadrats"] = "Quadrats"
    extent: typing.Optional[typing.List[typing.Any]] = None
    cells: typing.List[typing.List[typing.List[QuadratsCellsItemItemItem]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SiteOutline = typing_extensions.Annotated[
    typing.Union[SiteOutline_Marker, SiteOutline_Transect, SiteOutline_Quadrats], pydantic.Field(discriminator="kind")
]
