

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .favourites_folder_sections_item import FavouritesFolderSectionsItem


class FavouritesFolder(UniversalBaseModel):
    id: float
    name: str
    parent_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    children: typing.Optional[typing.List["FavouritesFolder"]] = None
    sort_order: typing_extensions.Annotated[float, FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")]
    sections: typing.Optional[typing.List[FavouritesFolderSectionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FavouritesFolder)
