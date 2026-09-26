

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ComplianceMetadataModel(UniversalBaseModel):
    """
    Model for ComplianceMetadata
    """

    compliance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="complianceId"),
        pydantic.Field(alias="complianceId", description="Compliance Section UUID"),
    ] = None
    """
    Compliance Section UUID
    """

    custom_assigned: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="customAssigned"), pydantic.Field(alias="customAssigned")
    ] = None
    policy_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId", description="Policy ID")
    ] = None
    """
    Policy ID
    """

    requirement_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requirementDescription"),
        pydantic.Field(alias="requirementDescription", description="Requirement description"),
    ] = None
    """
    Requirement description
    """

    requirement_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requirementId"),
        pydantic.Field(alias="requirementId", description="Requirement ID"),
    ] = None
    """
    Requirement ID
    """

    requirement_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requirementName"),
        pydantic.Field(alias="requirementName", description="Requirement name"),
    ] = None
    """
    Requirement name
    """

    section_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sectionDescription"),
        pydantic.Field(alias="sectionDescription", description="Section name"),
    ] = None
    """
    Section name
    """

    section_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sectionId"),
        pydantic.Field(alias="sectionId", description="Section Id"),
    ] = None
    """
    Section Id
    """

    section_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sectionLabel"),
        pydantic.Field(alias="sectionLabel", description="Section Label"),
    ] = None
    """
    Section Label
    """

    standard_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="standardDescription"),
        pydantic.Field(alias="standardDescription", description="Compliance standard description"),
    ] = None
    """
    Compliance standard description
    """

    standard_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="standardId"), pydantic.Field(alias="standardId")
    ] = None
    standard_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="standardName"),
        pydantic.Field(alias="standardName", description="Compliance standard name"),
    ] = None
    """
    Compliance standard name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
