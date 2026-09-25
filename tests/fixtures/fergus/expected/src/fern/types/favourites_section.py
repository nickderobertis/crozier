

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .favourites_section_line_items_item import FavouritesSectionLineItemsItem
from .favourites_section_path import FavouritesSectionPath


class FavouritesSection(UniversalBaseModel):
    id: float
    name: str
    description: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    folder_id: typing_extensions.Annotated[float, FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")]
    path: FavouritesSectionPath
    line_items: typing_extensions.Annotated[
        typing.List[FavouritesSectionLineItemsItem], FieldMetadata(alias="lineItems"), pydantic.Field(alias="lineItems")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
