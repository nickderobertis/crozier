

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .bundle_entry_request_component import BundleEntryRequestComponent
from .bundle_entry_response_component import BundleEntryResponseComponent
from .bundle_entry_search_component import BundleEntrySearchComponent
from .bundle_link_component import BundleLinkComponent
from .i_base_extension_object_object import IBaseExtensionObjectObject
from .resource import Resource


class BundleEntryComponent(UniversalBaseModel):
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
    link: typing.Optional[typing.List[BundleLinkComponent]] = None
    full_url: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="fullUrl"), pydantic.Field(alias="fullUrl")
    ] = None
    resource: typing.Optional[Resource] = None
    search: typing.Optional[BundleEntrySearchComponent] = None
    request: typing.Optional[BundleEntryRequestComponent] = None
    response: typing.Optional[BundleEntryResponseComponent] = None
    link_first_rep: typing_extensions.Annotated[
        typing.Optional[BundleLinkComponent], FieldMetadata(alias="linkFirstRep"), pydantic.Field(alias="linkFirstRep")
    ] = None
    full_url_element: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="fullUrlElement"), pydantic.Field(alias="fullUrlElement")
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
    BundleEntryComponent,
    Extension=Extension,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
