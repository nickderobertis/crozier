

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .base64binary_type import Base64BinaryType
from .code_type import CodeType
from .coding import Coding
from .instant_type import InstantType
from .resource import Resource


class Signature(UniversalBaseModel):
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
    type: typing.Optional[typing.List[Coding]] = None
    when: typing.Optional[InstantType] = None
    who: typing.Optional["Reference"] = None
    who_target: typing_extensions.Annotated[
        typing.Optional[Resource], FieldMetadata(alias="whoTarget"), pydantic.Field(alias="whoTarget")
    ] = None
    on_behalf_of: typing_extensions.Annotated[
        typing.Optional["Reference"], FieldMetadata(alias="onBehalfOf"), pydantic.Field(alias="onBehalfOf")
    ] = None
    on_behalf_of_target: typing_extensions.Annotated[
        typing.Optional[Resource], FieldMetadata(alias="onBehalfOfTarget"), pydantic.Field(alias="onBehalfOfTarget")
    ] = None
    target_format: typing_extensions.Annotated[
        typing.Optional[CodeType], FieldMetadata(alias="targetFormat"), pydantic.Field(alias="targetFormat")
    ] = None
    sig_format: typing_extensions.Annotated[
        typing.Optional[CodeType], FieldMetadata(alias="sigFormat"), pydantic.Field(alias="sigFormat")
    ] = None
    data: typing.Optional[Base64BinaryType] = None
    type_first_rep: typing_extensions.Annotated[
        typing.Optional[Coding], FieldMetadata(alias="typeFirstRep"), pydantic.Field(alias="typeFirstRep")
    ] = None
    when_element: typing_extensions.Annotated[
        typing.Optional[InstantType], FieldMetadata(alias="whenElement"), pydantic.Field(alias="whenElement")
    ] = None
    target_format_element: typing_extensions.Annotated[
        typing.Optional[CodeType],
        FieldMetadata(alias="targetFormatElement"),
        pydantic.Field(alias="targetFormatElement"),
    ] = None
    sig_format_element: typing_extensions.Annotated[
        typing.Optional[CodeType], FieldMetadata(alias="sigFormatElement"), pydantic.Field(alias="sigFormatElement")
    ] = None
    data_element: typing_extensions.Annotated[
        typing.Optional[Base64BinaryType], FieldMetadata(alias="dataElement"), pydantic.Field(alias="dataElement")
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
from .endpoint import Endpoint
from .identifier import Identifier
from .organization import Organization
from .reference import Reference

update_forward_refs(
    Signature,
    Endpoint=Endpoint,
    Extension=Extension,
    Identifier=Identifier,
    Organization=Organization,
    Reference=Reference,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
