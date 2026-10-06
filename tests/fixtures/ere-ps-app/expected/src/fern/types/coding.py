

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .boolean_type import BooleanType
from .code_type import CodeType


class Coding(UniversalBaseModel):
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
    user_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="userData"), pydantic.Field(alias="userData")
    ] = None
    primitive: typing.Optional[bool] = None
    boolean_primitive: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="booleanPrimitive"), pydantic.Field(alias="booleanPrimitive")
    ] = None
    date_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dateTime"), pydantic.Field(alias="dateTime")
    ] = None
    metadata_based: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="metadataBased"), pydantic.Field(alias="metadataBased")
    ] = None
    resource: typing.Optional[bool] = None
    xhtml: typing.Optional["XhtmlNode"] = None
    id: typing.Optional["StringType"] = None
    extension: typing.Optional[typing.List["Extension"]] = None
    disallow_extensions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="disallowExtensions"), pydantic.Field(alias="disallowExtensions")
    ] = None
    id_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="idElement"), pydantic.Field(alias="idElement")
    ] = None
    extension_first_rep: typing_extensions.Annotated[
        typing.Optional["Extension"],
        FieldMetadata(alias="extensionFirstRep"),
        pydantic.Field(alias="extensionFirstRep"),
    ] = None
    id_base: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idBase"), pydantic.Field(alias="idBase")
    ] = None
    system: typing.Optional["UriType"] = None
    version: typing.Optional["StringType"] = None
    code: typing.Optional[CodeType] = None
    display: typing.Optional["StringType"] = None
    user_selected: typing_extensions.Annotated[
        typing.Optional[BooleanType], FieldMetadata(alias="userSelected"), pydantic.Field(alias="userSelected")
    ] = None
    system_element: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="systemElement"), pydantic.Field(alias="systemElement")
    ] = None
    version_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="versionElement"), pydantic.Field(alias="versionElement")
    ] = None
    code_element: typing_extensions.Annotated[
        typing.Optional[CodeType], FieldMetadata(alias="codeElement"), pydantic.Field(alias="codeElement")
    ] = None
    display_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="displayElement"), pydantic.Field(alias="displayElement")
    ] = None
    user_selected_element: typing_extensions.Annotated[
        typing.Optional[BooleanType],
        FieldMetadata(alias="userSelectedElement"),
        pydantic.Field(alias="userSelectedElement"),
    ] = None
    empty: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .xhtml_node import XhtmlNode
from .xhtml_node_list import XhtmlNodeList
from .extension import Extension
from .string_type import StringType
from .type import Type
from .uri_type import UriType

update_forward_refs(
    Coding,
    Extension=Extension,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
