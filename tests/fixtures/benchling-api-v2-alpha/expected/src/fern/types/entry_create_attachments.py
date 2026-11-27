

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .custom_fields import CustomFields
from .entry_attachments import EntryAttachments
from .entry_create_attachments_review_record import EntryCreateAttachmentsReviewRecord
from .entry_create_author_ids import EntryCreateAuthorIds
from .fields import Fields
from .initial_table import InitialTable


class EntryCreateAttachments(EntryAttachments):
    review_record: typing_extensions.Annotated[
        typing.Optional[EntryCreateAttachmentsReviewRecord],
        FieldMetadata(alias="reviewRecord"),
        pydantic.Field(alias="reviewRecord"),
    ] = None
    author_ids: typing_extensions.Annotated[
        typing.Optional[EntryCreateAuthorIds], FieldMetadata(alias="authorIds"), pydantic.Field(alias="authorIds")
    ] = None
    custom_fields: typing_extensions.Annotated[
        typing.Optional[CustomFields],
        FieldMetadata(alias="customFields"),
        pydantic.Field(alias="customFields", description="Custom fields to add to the entry"),
    ] = None
    """
    Custom fields to add to the entry
    """

    entry_template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entryTemplateId"),
        pydantic.Field(alias="entryTemplateId", description="ID of the template to clone the entry from"),
    ] = None
    """
    ID of the template to clone the entry from
    """

    fields: typing.Optional[Fields] = pydantic.Field(default=None)
    """
    Fields to set on the entry. Must correspond with the schema's field definitions.
    """

    folder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that will contain the entry"),
    ]
    """
    ID of the folder that will contain the entry
    """

    initial_tables: typing_extensions.Annotated[
        typing.Optional[typing.List[InitialTable]],
        FieldMetadata(alias="initialTables"),
        pydantic.Field(
            alias="initialTables",
            description="An array of table API IDs and blob id pairs to seed tables from the template while creating the entry. The entryTemplateId parameter must be set to use this parameter. The table API IDs should be the API Identifiers of the tables in the given template.\n- If a template table has one row, the values in that row act as default values for cloned entries.\n- If a template table has multiple rows, there is no default value and those rows are added to the cloned entry along with the provided csv data.\n- If a table has default values, they will be populated in any respective undefined columns in the csv data.\n- If a table has no default values, undefined columns from csv data will be empty.\n- If no csv data is provided for a table, the table in the entry will be populated with whatever values are in the respective template table.",
        ),
    ] = None
    """
    An array of table API IDs and blob id pairs to seed tables from the template while creating the entry. The entryTemplateId parameter must be set to use this parameter. The table API IDs should be the API Identifiers of the tables in the given template.
    - If a template table has one row, the values in that row act as default values for cloned entries.
    - If a template table has multiple rows, there is no default value and those rows are added to the cloned entry along with the provided csv data.
    - If a table has default values, they will be populated in any respective undefined columns in the csv data.
    - If a table has no default values, undefined columns from csv data will be empty.
    - If no csv data is provided for a table, the table in the entry will be populated with whatever values are in the respective template table.
    """

    name: str = pydantic.Field()
    """
    Name of the entry
    """

    schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schemaId"),
        pydantic.Field(alias="schemaId", description="ID of the entry's schema"),
    ] = None
    """
    ID of the entry's schema
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
