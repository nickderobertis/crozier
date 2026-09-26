

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokensIssueRequestDoc(UniversalBaseModel):
    sub: str
    doc_id: typing_extensions.Annotated[str, FieldMetadata(alias="docId"), pydantic.Field(alias="docId")]
    layer_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="layerName"), pydantic.Field(alias="layerName")
    ] = None
    scope: typing.List[str]
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    groups: typing.Optional[typing.List[str]] = None
    origins: typing.Optional[typing.List[str]] = None
    expires_in: typing_extensions.Annotated[int, FieldMetadata(alias="expiresIn"), pydantic.Field(alias="expiresIn")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
