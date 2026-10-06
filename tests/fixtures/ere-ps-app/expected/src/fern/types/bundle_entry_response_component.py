

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .i_base_extension_object_object import IBaseExtensionObjectObject
from .instant_type import InstantType
from .resource import Resource


class BundleEntryResponseComponent(UniversalBaseModel):
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
    extension: typing.Optional[typing.List[IBaseExtensionObjectObject]] = None
    modifier_extension: typing_extensions.Annotated[
        typing.Optional[typing.List[IBaseExtensionObjectObject]],
        FieldMetadata(alias="modifierExtension"),
        pydantic.Field(alias="modifierExtension"),
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
    modifier_extension_first_rep: typing_extensions.Annotated[
        typing.Optional["Extension"],
        FieldMetadata(alias="modifierExtensionFirstRep"),
        pydantic.Field(alias="modifierExtensionFirstRep"),
    ] = None
    status: typing.Optional["StringType"] = None
    location: typing.Optional["UriType"] = None
    etag: typing.Optional["StringType"] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[InstantType], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    outcome: typing.Optional[Resource] = None
    status_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="statusElement"), pydantic.Field(alias="statusElement")
    ] = None
    location_element: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="locationElement"), pydantic.Field(alias="locationElement")
    ] = None
    etag_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="etagElement"), pydantic.Field(alias="etagElement")
    ] = None
    last_modified_element: typing_extensions.Annotated[
        typing.Optional[InstantType],
        FieldMetadata(alias="lastModifiedElement"),
        pydantic.Field(alias="lastModifiedElement"),
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
    BundleEntryResponseComponent,
    Extension=Extension,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
