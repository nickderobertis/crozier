

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsPackageType(UniversalBaseModel):
    attribute: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Attribute"),
        pydantic.Field(
            alias="Attribute",
            description="The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.",
        ),
    ] = None
    """
    The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.
    """

    category: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Category"),
        pydantic.Field(
            alias="Category",
            description="The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.",
        ),
    ] = None
    """
    The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the package type"),
    ]
    """
    The description of the package type
    """

    icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Icon"),
        pydantic.Field(alias="Icon", description="Optional.  The icon to use for the PackageType, in base 64"),
    ] = None
    """
    Optional.  The icon to use for the PackageType, in base 64
    """

    inventory_frequency: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="InventoryFrequency"),
        pydantic.Field(
            alias="InventoryFrequency",
            description="The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).",
        ),
    ] = None
    """
    The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).
    """

    inventory_package: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InventoryPackage"),
        pydantic.Field(
            alias="InventoryPackage",
            description="The inventory package used to determine what version of this package type is installed.",
        ),
    ] = None
    """
    The inventory package used to determine what version of this package type is installed.
    """

    localized_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LocalizedDescription"),
        pydantic.Field(
            alias="LocalizedDescription",
            description="Optional. The StringID used to localize the description of the PackageType",
        ),
    ] = None
    """
    Optional. The StringID used to localize the description of the PackageType
    """

    localized_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LocalizedName"),
        pydantic.Field(
            alias="LocalizedName", description="Optional. The StringID used to localize the name of the PackageType"
        ),
    ] = None
    """
    Optional. The StringID used to localize the name of the PackageType
    """

    max_delta_packages: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxDeltaPackages"),
        pydantic.Field(
            alias="MaxDeltaPackages",
            description='The maximum number of "chained" delta packages to use when updating the client',
        ),
    ] = None
    """
    The maximum number of "chained" delta packages to use when updating the client
    """

    package_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(alias="PackageTypeID", description="Read Only. The package type id."),
    ] = None
    """
    Read Only. The package type id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
