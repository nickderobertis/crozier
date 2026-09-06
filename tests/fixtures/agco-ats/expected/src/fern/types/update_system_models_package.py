

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsPackage(UniversalBaseModel):
    autorun: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Autorun"),
        pydantic.Field(
            alias="Autorun", description="Value is true if package should run automatically. Default value is false."
        ),
    ] = None
    """
    Value is true if package should run automatically. Default value is false.
    """

    crc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CRC"),
        pydantic.Field(alias="CRC", description="The CRC used to validate the download."),
    ]
    """
    The CRC used to validate the download.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The package description"),
    ]
    """
    The package description
    """

    localized_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LocalizedName"),
        pydantic.Field(
            alias="LocalizedName", description="Optional. The StringID used to localize the name of the Package"
        ),
    ] = None
    """
    Optional. The StringID used to localize the name of the Package
    """

    notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Notes about the package"),
    ] = None
    """
    Notes about the package
    """

    package_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageID"),
        pydantic.Field(alias="PackageID", description="Read Only. The package ID"),
    ] = None
    """
    Read Only. The package ID
    """

    package_type_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(alias="PackageTypeID", description="The id of the package type this package belongs to."),
    ]
    """
    The id of the package type this package belongs to.
    """

    previous_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="PreviousVersion"),
        pydantic.Field(
            alias="PreviousVersion",
            description="For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.",
        ),
    ] = None
    """
    For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.
    """

    release_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="ReleaseDate"),
        pydantic.Field(alias="ReleaseDate", description="The date the package was released"),
    ]
    """
    The date the package was released
    """

    released: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Released"),
        pydantic.Field(alias="Released", description="True if the package is released.  Default value is False."),
    ] = None
    """
    True if the package is released.  Default value is False.
    """

    remove_on_success: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="RemoveOnSuccess"),
        pydantic.Field(
            alias="RemoveOnSuccess",
            description="True to remove the package after successful execution.  Default value is False.",
        ),
    ] = None
    """
    True to remove the package after successful execution.  Default value is False.
    """

    size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Size"),
        pydantic.Field(
            alias="Size",
            description="The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.\r\n            If the size provided does not match the size in the response from the URL an error will be returned.",
        ),
    ] = None
    """
    The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                If the size provided does not match the size in the response from the URL an error will be returned.
    """

    switches: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Switches"),
        pydantic.Field(
            alias="Switches",
            description="The command line arguments for the package.  Default value is an empty string.",
        ),
    ] = None
    """
    The command line arguments for the package.  Default value is an empty string.
    """

    url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Url"),
        pydantic.Field(alias="Url", description="The Url to download the package from."),
    ]
    """
    The Url to download the package from.
    """

    version: typing_extensions.Annotated[
        int, FieldMetadata(alias="Version"), pydantic.Field(alias="Version", description="The version.")
    ]
    """
    The version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
