

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .code_type import CodeType
from .codeable_concept import CodeableConcept
from .coding import Coding
from .contact_point import ContactPoint
from .enumeration_endpoint_status import EnumerationEndpointStatus
from .fhir_version_enum import FhirVersionEnum
from .i_base_meta_type import IBaseMetaType
from .i_id_type import IIdType
from .i_primitive_type_string import IPrimitiveTypeString
from .narrative import Narrative
from .period import Period
from .resource import Resource
from .resource_type import ResourceType
from .url_type import UrlType


class Endpoint(UniversalBaseModel):
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
    id: typing.Optional[str] = None
    id_element: typing_extensions.Annotated[
        typing.Optional[IIdType], FieldMetadata(alias="idElement"), pydantic.Field(alias="idElement")
    ] = None
    language_element: typing_extensions.Annotated[
        typing.Optional[IPrimitiveTypeString],
        FieldMetadata(alias="languageElement"),
        pydantic.Field(alias="languageElement"),
    ] = None
    meta: typing.Optional[IBaseMetaType] = None
    structure_fhir_version_enum: typing_extensions.Annotated[
        typing.Optional[FhirVersionEnum],
        FieldMetadata(alias="structureFhirVersionEnum"),
        pydantic.Field(alias="structureFhirVersionEnum"),
    ] = None
    deleted: typing.Optional[bool] = None
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
    id_base: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="idBase"), pydantic.Field(alias="idBase")
    ] = None
    text: typing.Optional[Narrative] = None
    contained: typing.Optional[typing.List[Resource]] = None
    extension: typing.Optional[typing.List["Extension"]] = None
    modifier_extension: typing_extensions.Annotated[
        typing.Optional[typing.List["Extension"]],
        FieldMetadata(alias="modifierExtension"),
        pydantic.Field(alias="modifierExtension"),
    ] = None
    identifier: typing.Optional[typing.List["Identifier"]] = None
    status: typing.Optional[EnumerationEndpointStatus] = None
    connection_type: typing_extensions.Annotated[
        typing.Optional[Coding], FieldMetadata(alias="connectionType"), pydantic.Field(alias="connectionType")
    ] = None
    name: typing.Optional["StringType"] = None
    managing_organization: typing_extensions.Annotated[
        typing.Optional["Reference"],
        FieldMetadata(alias="managingOrganization"),
        pydantic.Field(alias="managingOrganization"),
    ] = None
    managing_organization_target: typing_extensions.Annotated[
        typing.Optional["Organization"],
        FieldMetadata(alias="managingOrganizationTarget"),
        pydantic.Field(alias="managingOrganizationTarget"),
    ] = None
    contact: typing.Optional[typing.List[ContactPoint]] = None
    period: typing.Optional[Period] = None
    payload_type: typing_extensions.Annotated[
        typing.Optional[typing.List[CodeableConcept]],
        FieldMetadata(alias="payloadType"),
        pydantic.Field(alias="payloadType"),
    ] = None
    payload_mime_type: typing_extensions.Annotated[
        typing.Optional[typing.List[CodeType]],
        FieldMetadata(alias="payloadMimeType"),
        pydantic.Field(alias="payloadMimeType"),
    ] = None
    address: typing.Optional[UrlType] = None
    header: typing.Optional[typing.List["StringType"]] = None
    identifier_first_rep: typing_extensions.Annotated[
        typing.Optional["Identifier"],
        FieldMetadata(alias="identifierFirstRep"),
        pydantic.Field(alias="identifierFirstRep"),
    ] = None
    status_element: typing_extensions.Annotated[
        typing.Optional[EnumerationEndpointStatus],
        FieldMetadata(alias="statusElement"),
        pydantic.Field(alias="statusElement"),
    ] = None
    name_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="nameElement"), pydantic.Field(alias="nameElement")
    ] = None
    contact_first_rep: typing_extensions.Annotated[
        typing.Optional[ContactPoint], FieldMetadata(alias="contactFirstRep"), pydantic.Field(alias="contactFirstRep")
    ] = None
    payload_type_first_rep: typing_extensions.Annotated[
        typing.Optional[CodeableConcept],
        FieldMetadata(alias="payloadTypeFirstRep"),
        pydantic.Field(alias="payloadTypeFirstRep"),
    ] = None
    address_element: typing_extensions.Annotated[
        typing.Optional[UrlType], FieldMetadata(alias="addressElement"), pydantic.Field(alias="addressElement")
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
from .identifier import Identifier
from .organization import Organization
from .reference import Reference

update_forward_refs(
    Endpoint,
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
