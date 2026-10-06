

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .bundle_entry_component import BundleEntryComponent
from .bundle_link_component import BundleLinkComponent
from .code_type import CodeType
from .enumeration_bundle_type import EnumerationBundleType
from .fhir_version_enum import FhirVersionEnum
from .i_base_meta_type import IBaseMetaType
from .i_id_type import IIdType
from .id_type import IdType
from .instant_type import InstantType
from .resource_type import ResourceType
from .signature import Signature
from .unsigned_int_type import UnsignedIntType


class Bundle(UniversalBaseModel):
    meta: typing.Optional[IBaseMetaType] = None
    id_element: typing_extensions.Annotated[
        typing.Optional[IIdType], FieldMetadata(alias="idElement"), pydantic.Field(alias="idElement")
    ] = None
    structure_fhir_version_enum: typing_extensions.Annotated[
        typing.Optional[FhirVersionEnum],
        FieldMetadata(alias="structureFhirVersionEnum"),
        pydantic.Field(alias="structureFhirVersionEnum"),
    ] = None
    deleted: typing.Optional[bool] = None
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
    xhtml: typing.Optional["XhtmlNode"] = None
    resource: typing.Optional[bool] = None
    id: typing.Optional[IdType] = None
    implicit_rules: typing_extensions.Annotated[
        typing.Optional["UriType"], FieldMetadata(alias="implicitRules"), pydantic.Field(alias="implicitRules")
    ] = None
    language: typing.Optional[CodeType] = None
    id_part: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idPart"), pydantic.Field(alias="idPart")
    ] = None
    implicit_rules_element: typing_extensions.Annotated[
        typing.Optional["UriType"],
        FieldMetadata(alias="implicitRulesElement"),
        pydantic.Field(alias="implicitRulesElement"),
    ] = None
    language_element: typing_extensions.Annotated[
        typing.Optional[CodeType], FieldMetadata(alias="languageElement"), pydantic.Field(alias="languageElement")
    ] = None
    id_base: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idBase"), pydantic.Field(alias="idBase")
    ] = None
    identifier: typing.Optional["Identifier"] = None
    type: typing.Optional[EnumerationBundleType] = None
    timestamp: typing.Optional[InstantType] = None
    total: typing.Optional[UnsignedIntType] = None
    link: typing.Optional[typing.List[BundleLinkComponent]] = None
    entry: typing.Optional[typing.List[BundleEntryComponent]] = None
    signature: typing.Optional[Signature] = None
    type_element: typing_extensions.Annotated[
        typing.Optional[EnumerationBundleType], FieldMetadata(alias="typeElement"), pydantic.Field(alias="typeElement")
    ] = None
    timestamp_element: typing_extensions.Annotated[
        typing.Optional[InstantType], FieldMetadata(alias="timestampElement"), pydantic.Field(alias="timestampElement")
    ] = None
    total_element: typing_extensions.Annotated[
        typing.Optional[UnsignedIntType], FieldMetadata(alias="totalElement"), pydantic.Field(alias="totalElement")
    ] = None
    link_first_rep: typing_extensions.Annotated[
        typing.Optional[BundleLinkComponent], FieldMetadata(alias="linkFirstRep"), pydantic.Field(alias="linkFirstRep")
    ] = None
    entry_first_rep: typing_extensions.Annotated[
        typing.Optional[BundleEntryComponent],
        FieldMetadata(alias="entryFirstRep"),
        pydantic.Field(alias="entryFirstRep"),
    ] = None
    empty: typing.Optional[bool] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[ResourceType], FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ] = None

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
    Bundle,
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
