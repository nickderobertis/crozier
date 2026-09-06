

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentSubmissionSharedBusinessEntitiesContentSubmissionType(UniversalBaseModel):
    """
    A type of content available for submission
    """

    attribute_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AttributeTemplate"),
        pydantic.Field(
            alias="AttributeTemplate",
            description="A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}",
        ),
    ] = None
    """
    A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}
    """

    build_definition_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="BuildDefinitionID"),
        pydantic.Field(
            alias="BuildDefinitionID",
            description="The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.",
        ),
    ] = None
    """
    The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.
    """

    category_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CategoryTemplate"),
        pydantic.Field(
            alias="CategoryTemplate",
            description="A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}",
        ),
    ] = None
    """
    A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="A description for the Content Submission Type"),
    ]
    """
    A description for the Content Submission Type
    """

    enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Enabled"),
        pydantic.Field(alias="Enabled", description="Indicates whether this submission type is available to be used"),
    ] = None
    """
    Indicates whether this submission type is available to be used
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The ID of the Content Submission Type"),
    ] = None
    """
    The ID of the Content Submission Type
    """

    inventory_package_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InventoryPackageID"),
        pydantic.Field(
            alias="InventoryPackageID",
            description="The ID of the Inventory Package from which to read the version of the package installed.",
        ),
    ] = None
    """
    The ID of the Inventory Package from which to read the version of the package installed.
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobID"),
        pydantic.Field(
            alias="JobID",
            description="The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.",
        ),
    ] = None
    """
    The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The Name of the Content Submission Type"),
    ]
    """
    The Name of the Content Submission Type
    """

    release_notes_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReleaseNotesDescription"),
        pydantic.Field(
            alias="ReleaseNotesDescription",
            description="A description of how release notes for this Content Submission Type are used",
        ),
    ] = None
    """
    A description of how release notes for this Content Submission Type are used
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
