

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentSubmissionSharedBusinessEntitiesContentReleaseVersion(UniversalBaseModel):
    """
    ContentReleaseVersion class
    """

    content_definition_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ContentDefinitionID"),
        pydantic.Field(alias="ContentDefinitionID", description="ContentDefinitionID"),
    ] = None
    """
    ContentDefinitionID
    """

    content_release_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ContentReleaseID"),
        pydantic.Field(alias="ContentReleaseID", description="ContentReleaseID"),
    ] = None
    """
    ContentReleaseID
    """

    deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Deleted"),
        pydantic.Field(alias="Deleted", description="deleted flag"),
    ] = None
    """
    deleted flag
    """

    publisher_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="PublisherUserID"),
        pydantic.Field(alias="PublisherUserID", description="PublisherUser ID"),
    ] = None
    """
    PublisherUser ID
    """

    release_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ReleaseID"),
        pydantic.Field(alias="ReleaseID", description="rele4ase Id"),
    ] = None
    """
    rele4ase Id
    """

    test_report_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TestReportUrl"),
        pydantic.Field(
            alias="TestReportUrl", description="The URL at which test reports for this content can be found"
        ),
    ] = None
    """
    The URL at which test reports for this content can be found
    """

    updated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="UpdatedDate"),
        pydantic.Field(alias="UpdatedDate", description="Updated Date"),
    ] = None
    """
    Updated Date
    """

    version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Version"), pydantic.Field(alias="Version", description="version")
    ] = None
    """
    version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
