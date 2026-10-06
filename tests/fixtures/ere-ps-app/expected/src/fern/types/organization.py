

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .address import Address
from .boolean_type import BooleanType
from .code_type import CodeType
from .codeable_concept import CodeableConcept
from .contact_point import ContactPoint
from .fhir_version_enum import FhirVersionEnum
from .i_base_meta_type import IBaseMetaType
from .i_id_type import IIdType
from .i_primitive_type_string import IPrimitiveTypeString
from .narrative import Narrative
from .organization_contact_component import OrganizationContactComponent
from .resource import Resource
from .resource_type import ResourceType


class Organization(UniversalBaseModel):
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
    active: typing.Optional[BooleanType] = None
    type: typing.Optional[typing.List[CodeableConcept]] = None
    name: typing.Optional["StringType"] = None
    alias: typing.Optional[typing.List["StringType"]] = None
    telecom: typing.Optional[typing.List[ContactPoint]] = None
    address: typing.Optional[typing.List[Address]] = None
    part_of: typing_extensions.Annotated[
        typing.Optional["Reference"], FieldMetadata(alias="partOf"), pydantic.Field(alias="partOf")
    ] = None
    part_of_target: typing_extensions.Annotated[
        typing.Optional["Organization"], FieldMetadata(alias="partOfTarget"), pydantic.Field(alias="partOfTarget")
    ] = None
    contact: typing.Optional[typing.List[OrganizationContactComponent]] = None
    endpoint: typing.Optional[typing.List["Reference"]] = None
    endpoint_target: typing_extensions.Annotated[
        typing.Optional[typing.List["Endpoint"]],
        FieldMetadata(alias="endpointTarget"),
        pydantic.Field(alias="endpointTarget"),
    ] = None
    identifier_first_rep: typing_extensions.Annotated[
        typing.Optional["Identifier"],
        FieldMetadata(alias="identifierFirstRep"),
        pydantic.Field(alias="identifierFirstRep"),
    ] = None
    active_element: typing_extensions.Annotated[
        typing.Optional[BooleanType], FieldMetadata(alias="activeElement"), pydantic.Field(alias="activeElement")
    ] = None
    type_first_rep: typing_extensions.Annotated[
        typing.Optional[CodeableConcept], FieldMetadata(alias="typeFirstRep"), pydantic.Field(alias="typeFirstRep")
    ] = None
    name_element: typing_extensions.Annotated[
        typing.Optional["StringType"], FieldMetadata(alias="nameElement"), pydantic.Field(alias="nameElement")
    ] = None
    telecom_first_rep: typing_extensions.Annotated[
        typing.Optional[ContactPoint], FieldMetadata(alias="telecomFirstRep"), pydantic.Field(alias="telecomFirstRep")
    ] = None
    address_first_rep: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="addressFirstRep"), pydantic.Field(alias="addressFirstRep")
    ] = None
    contact_first_rep: typing_extensions.Annotated[
        typing.Optional[OrganizationContactComponent],
        FieldMetadata(alias="contactFirstRep"),
        pydantic.Field(alias="contactFirstRep"),
    ] = None
    endpoint_first_rep: typing_extensions.Annotated[
        typing.Optional["Reference"], FieldMetadata(alias="endpointFirstRep"), pydantic.Field(alias="endpointFirstRep")
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
from .reference import Reference

update_forward_refs(
    Organization,
    Endpoint=Endpoint,
    Extension=Extension,
    Identifier=Identifier,
    Reference=Reference,
    StringType=StringType,
    Type=Type,
    UriType=UriType,
    XhtmlNode=XhtmlNode,
    XhtmlNodeList=XhtmlNodeList,
)
