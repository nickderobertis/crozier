

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_model import SearchModel


class SavedRecentSearch(UniversalBaseModel):
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    description: typing.Optional[str] = None
    id: typing.Optional[str] = None
    last_modified_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastModifiedBy"), pydantic.Field(alias="lastModifiedBy")
    ] = None
    policies: typing.Optional[typing.List[typing.Dict[str, str]]] = None
    query: typing.Optional[str] = None
    search_model: typing_extensions.Annotated[
        typing.Optional[SearchModel], FieldMetadata(alias="searchModel"), pydantic.Field(alias="searchModel")
    ] = None
    search_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="searchName"), pydantic.Field(alias="searchName")
    ] = None
    system_default: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="systemDefault"), pydantic.Field(alias="systemDefault")
    ] = None
    timestamp: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
