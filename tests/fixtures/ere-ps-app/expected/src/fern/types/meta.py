

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .canonical_type import CanonicalType
from .coding import Coding
from .id_type import IdType
from .instant_type import InstantType


class Meta(UniversalBaseModel):
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
    version_id: typing_extensions.Annotated[
        typing.Optional[IdType], FieldMetadata(alias="versionId"), pydantic.Field(alias="versionId")
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[InstantType], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    source: typing.Optional["UriType"] = None
    profile: typing.Optional[typing.List[CanonicalType]] = None
    security: typing.Optional[typing.List[Coding]] = None
    tag: typing.Optional[typing.List[Coding]] = None
    version_id_element: typing_extensions.Annotated[
        typing.Optional[IdType], FieldMetadata(alias="versionIdElement"), pydantic.Field(alias="versionIdElement")
    ] = None
    last_updated_element: typing_extensions.Annotated[
        typing.Optional[InstantType],
        FieldMetadata(alias="lastUpdatedElement"),
        pydantic.Field(alias="lastUpdatedElement"),
    ] = None
    source_element: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="sourceElement"), pydantic.Field(alias="sourceElement")
    ] = None
    security_first_rep: typing_extensions.Annotated[
        typing.Optional[Coding], FieldMetadata(alias="securityFirstRep"), pydantic.Field(alias="securityFirstRep")
    ] = None
    tag_first_rep: typing_extensions.Annotated[
        typing.Optional[Coding], FieldMetadata(alias="tagFirstRep"), pydantic.Field(alias="tagFirstRep")
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
    Meta,
    Extension=Extension,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
