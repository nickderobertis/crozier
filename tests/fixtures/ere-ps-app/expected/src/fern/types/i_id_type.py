

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IIdType(UniversalBaseModel):
    value_as_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueAsString"), pydantic.Field(alias="valueAsString")
    ] = None
    format_comments_pre: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPre"),
        pydantic.Field(alias="formatCommentsPre"),
    ] = None
    format_comments_post: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPost"),
        pydantic.Field(alias="formatCommentsPost"),
    ] = None
    base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseUrl"), pydantic.Field(alias="baseUrl")
    ] = None
    id_part: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idPart"), pydantic.Field(alias="idPart")
    ] = None
    id_part_as_long: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="idPartAsLong"), pydantic.Field(alias="idPartAsLong")
    ] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ] = None
    value: typing.Optional[str] = None
    version_id_part: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="versionIdPart"), pydantic.Field(alias="versionIdPart")
    ] = None
    version_id_part_as_long: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="versionIdPartAsLong"), pydantic.Field(alias="versionIdPartAsLong")
    ] = None
    absolute: typing.Optional[bool] = None
    empty: typing.Optional[bool] = None
    id_part_valid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="idPartValid"), pydantic.Field(alias="idPartValid")
    ] = None
    id_part_valid_long: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="idPartValidLong"), pydantic.Field(alias="idPartValidLong")
    ] = None
    local: typing.Optional[bool] = None
    version_id_part_valid_long: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="versionIdPartValidLong"),
        pydantic.Field(alias="versionIdPartValidLong"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
