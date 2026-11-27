

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .custom_fields import CustomFields
from .entry_schema import EntrySchema
from .entry_template_day import EntryTemplateDay
from .fields import Fields
from .user_summary import UserSummary


class EntryTemplate(UniversalBaseModel):
    """
    Entry templates are templates that users can base new notebook entries off of.
    """

    api_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiURL"),
        pydantic.Field(alias="apiURL", description="The canonical url of the Entry Template in the API."),
    ] = None
    """
    The canonical url of the Entry Template in the API.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the template was created at"),
    ] = None
    """
    DateTime the template was created at
    """

    creator: typing.Optional[UserSummary] = pydantic.Field(default=None)
    """
    UserSummary Resource of the user who created the template
    """

    custom_fields: typing_extensions.Annotated[
        typing.Optional[CustomFields], FieldMetadata(alias="customFields"), pydantic.Field(alias="customFields")
    ] = None
    days: typing.Optional[typing.List[EntryTemplateDay]] = pydantic.Field(default=None)
    """
    Array of day objects. Each day object has a day index (integer) and notes field (array of notes, expand further for details on note types).
    """

    fields: typing.Optional[Fields] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the entry template
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="DateTime the template was last modified"),
    ] = None
    """
    DateTime the template was last modified
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the template
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[EntrySchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Entry schema if set"),
    ] = None
    """
    Entry schema if set
    """

    template_collection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateCollectionId"),
        pydantic.Field(alias="templateCollectionId", description="ID of the collection that contains the template"),
    ] = None
    """
    ID of the collection that contains the template
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webURL"),
        pydantic.Field(alias="webURL", description="URL of the template"),
    ] = None
    """
    URL of the template
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
