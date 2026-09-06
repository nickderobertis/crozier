

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListScriptsResponseRegisteredScriptsItem(UniversalBaseModel):
    """
    Registered custom code for application
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human readable id, derived from the user-specified display name
    """

    can_copy: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canCopy"),
        pydantic.Field(
            alias="canCopy", description="Define whether the script can be copied on site duplication and transfer"
        ),
    ] = None
    """
    Define whether the script can be copied on site duplication and transfer
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="User-facing name for the script. Must be between 1 and 50 alphanumeric characters",
        ),
    ] = None
    """
    User-facing name for the script. Must be between 1 and 50 alphanumeric characters
    """

    hosted_location: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hostedLocation"),
        pydantic.Field(alias="hostedLocation", description="URI for an externally hosted script location"),
    ] = None
    """
    URI for an externally hosted script location
    """

    integrity_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="integrityHash"),
        pydantic.Field(
            alias="integrityHash",
            description="Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)",
        ),
    ] = None
    """
    Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Timestamp when the script version was created"),
    ] = None
    """
    Timestamp when the script version was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Timestamp when the script version was last updated"),
    ] = None
    """
    Timestamp when the script version was last updated
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Semantic Version (SemVer) string, denoting the version of the script
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
