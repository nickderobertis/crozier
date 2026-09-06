

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsPriorityPackage(UniversalBaseModel):
    autorun: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Autorun"),
        pydantic.Field(
            alias="Autorun",
            description="Read Only. From the package specified by package ID.\r\n            Value is true if package should run automatically. Default value is false.",
        ),
    ] = None
    """
    Read Only. From the package specified by package ID.
                Value is true if package should run automatically. Default value is false.
    """

    crc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CRC"),
        pydantic.Field(alias="CRC", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="The ID of the client to receive the priority package"),
    ]
    """
    The ID of the client to receive the priority package
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    package_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="PackageID"),
        pydantic.Field(alias="PackageID", description="The ID of the package to push as a priority package."),
    ]
    """
    The ID of the package to push as a priority package.
    """

    package_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(alias="PackageTypeID", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    previous_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="PreviousVersion"),
        pydantic.Field(alias="PreviousVersion", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    priority_package_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PriorityPackageID"),
        pydantic.Field(alias="PriorityPackageID", description="Read Only. The ID of the priority package."),
    ] = None
    """
    Read Only. The ID of the priority package.
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="ReleaseDate"),
        pydantic.Field(
            alias="ReleaseDate",
            description="Read Only. From the package specified by package ID.\r\n            The date the package was released",
        ),
    ] = None
    """
    Read Only. From the package specified by package ID.
                The date the package was released
    """

    released: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Released"),
        pydantic.Field(alias="Released", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    remove_on_success: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="RemoveOnSuccess"),
        pydantic.Field(alias="RemoveOnSuccess", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Size"),
        pydantic.Field(alias="Size", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    switches: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Switches"),
        pydantic.Field(
            alias="Switches",
            description="The command line arguments for the priority package.  Default value is an empty string.",
        ),
    ] = None
    """
    The command line arguments for the priority package.  Default value is an empty string.
    """

    time_stamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="TimeStamp"),
        pydantic.Field(alias="TimeStamp", description="Read Only. The timestamp of the priority package."),
    ] = None
    """
    Read Only. The timestamp of the priority package.
    """

    url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Url"),
        pydantic.Field(alias="Url", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Version"),
        pydantic.Field(alias="Version", description="Read Only. From the package specified by package ID."),
    ] = None
    """
    Read Only. From the package specified by package ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
