

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsUpdateGroup(UniversalBaseModel):
    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the update group"),
    ]
    """
    The description of the update group
    """

    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ID"), pydantic.Field(alias="ID")] = None
    inventory_frequency: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="InventoryFrequency"),
        pydantic.Field(
            alias="InventoryFrequency",
            description="The time in minutes between inventory checks. Default value is 1440 minutes (one day).",
        ),
    ] = None
    """
    The time in minutes between inventory checks. Default value is 1440 minutes (one day).
    """

    inventory_package: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InventoryPackage"),
        pydantic.Field(alias="InventoryPackage", description="The Package ID of the package used for inventory"),
    ] = None
    """
    The Package ID of the package used for inventory
    """

    localized_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LocalizedDescription"),
        pydantic.Field(
            alias="LocalizedDescription",
            description="Optional. The StringID used to localize the description of the update group",
        ),
    ] = None
    """
    Optional. The StringID used to localize the description of the update group
    """

    localized_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LocalizedName"),
        pydantic.Field(
            alias="LocalizedName", description="Optional. The StringID used to localize the name of the update group"
        ),
    ] = None
    """
    Optional. The StringID used to localize the name of the update group
    """

    priority: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Priority"),
        pydantic.Field(
            alias="Priority",
            description="The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.",
        ),
    ]
    """
    The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.
    """

    report_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReportField"),
        pydantic.Field(
            alias="ReportField",
            description="A field to return in the status report for this update group.\r\n            Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})",
        ),
    ] = None
    """
    A field to return in the status report for this update group.
                Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})
    """

    update_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="UpdateType"), pydantic.Field(alias="UpdateType", description="The update type name")
    ]
    """
    The update type name
    """

    validating_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ValidatingField"),
        pydantic.Field(
            alias="ValidatingField",
            description="A field used for validation in the status report for this update group.\r\n            Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})",
        ),
    ] = None
    """
    A field used for validation in the status report for this update group.
                Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})
    """

    value_to_validate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ValueToValidate"),
        pydantic.Field(alias="ValueToValidate", description="The value to validate the ValidationField against."),
    ] = None
    """
    The value to validate the ValidationField against.
    """

    version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Version"),
        pydantic.Field(
            alias="Version",
            description="The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType",
        ),
    ] = None
    """
    The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
