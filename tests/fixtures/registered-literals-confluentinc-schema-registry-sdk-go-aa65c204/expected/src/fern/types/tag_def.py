

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_attribute_def import AtlasAttributeDef
from .tag_def_category import TagDefCategory


class TagDef(UniversalBaseModel):
    category: typing.Optional[TagDefCategory] = None
    guid: typing.Optional[str] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    create_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="createTime"), pydantic.Field(alias="createTime")
    ] = None
    update_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="updateTime"), pydantic.Field(alias="updateTime")
    ] = None
    version: typing.Optional[int] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeVersion"), pydantic.Field(alias="typeVersion")
    ] = None
    service_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="serviceType"), pydantic.Field(alias="serviceType")
    ] = None
    options: typing.Optional[typing.Dict[str, str]] = None
    attribute_defs: typing_extensions.Annotated[
        typing.Optional[typing.List[AtlasAttributeDef]],
        FieldMetadata(alias="attributeDefs"),
        pydantic.Field(alias="attributeDefs"),
    ] = None
    super_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="superTypes"), pydantic.Field(alias="superTypes")
    ] = None
    entity_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="entityTypes"), pydantic.Field(alias="entityTypes")
    ] = None
    sub_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="subTypes"), pydantic.Field(alias="subTypes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
