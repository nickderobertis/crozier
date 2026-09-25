

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .favourites_section_path import FavouritesSectionPath


class FavouritesResponseDataDescription(UniversalBaseModel):
    id: float
    name: str
    description: typing.Optional[str] = None
    folder_id: typing_extensions.Annotated[float, FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    fixture_price: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="fixturePrice"), pydantic.Field(alias="fixturePrice")
    ] = None
    total_item_cost: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalItemCost"), pydantic.Field(alias="totalItemCost")
    ]
    total_item_price: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalItemPrice"), pydantic.Field(alias="totalItemPrice")
    ]
    path: FavouritesSectionPath

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
