

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_list_string import MapListString


class DisplayableUser(UniversalBaseModel):
    id: str
    username: str
    is_admin: typing_extensions.Annotated[bool, FieldMetadata(alias="isAdmin"), pydantic.Field(alias="isAdmin")]
    categories: typing.Optional[typing.List[str]] = None
    category_permissions: typing_extensions.Annotated[
        MapListString, FieldMetadata(alias="categoryPermissions"), pydantic.Field(alias="categoryPermissions")
    ]
    global_permissions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="globalPermissions"),
        pydantic.Field(alias="globalPermissions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
