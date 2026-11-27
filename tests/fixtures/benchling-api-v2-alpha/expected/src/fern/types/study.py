

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archive_record import ArchiveRecord
from .fields import Fields
from .study_phase import StudyPhase
from .user_summary import UserSummary


class Study(UniversalBaseModel):
    archive_record: typing_extensions.Annotated[
        typing.Optional[ArchiveRecord], FieldMetadata(alias="archiveRecord"), pydantic.Field(alias="archiveRecord")
    ] = None
    authors: typing.Optional[typing.List[UserSummary]] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the Study was created."),
    ] = None
    """
    DateTime the Study was created.
    """

    creator: typing.Optional[UserSummary] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the Study.
    """

    design_entry_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="designEntryId"),
        pydantic.Field(alias="designEntryId", description="The ID of the design entry associated with the Study."),
    ] = None
    """
    The ID of the design entry associated with the Study.
    """

    fields: typing.Optional[Fields] = pydantic.Field(default=None)
    """
    Fields to set on the Study. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.
    """

    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that contains the Study."),
    ] = None
    """
    ID of the folder that contains the Study.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the Study.
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="DateTime the Study was last modified."),
    ] = None
    """
    DateTime the Study was last modified.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Study.
    """

    phase: typing.Optional[StudyPhase] = pydantic.Field(default=None)
    """
    The phase of the Study.
    """

    study_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="studySchemaId"),
        pydantic.Field(alias="studySchemaId", description="The ID of the Study's schema."),
    ] = None
    """
    The ID of the Study's schema.
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webURL"),
        pydantic.Field(alias="webURL", description="URL of the Study."),
    ] = None
    """
    URL of the Study.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
