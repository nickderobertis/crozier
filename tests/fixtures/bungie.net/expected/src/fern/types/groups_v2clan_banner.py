

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GroupsV2ClanBanner(UniversalBaseModel):
    decal_background_color_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="decalBackgroundColorId")
    ] = None
    decal_color_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="decalColorId")] = None
    decal_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="decalId")] = None
    gonfalon_color_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="gonfalonColorId")] = None
    gonfalon_detail_color_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="gonfalonDetailColorId")
    ] = None
    gonfalon_detail_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="gonfalonDetailId")] = (
        None
    )
    gonfalon_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="gonfalonId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
