

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_create import EntryCreate
from .fields import Fields


class StudyCreate(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the Study.
    """

    entry_information: typing_extensions.Annotated[
        EntryCreate, FieldMetadata(alias="entryInformation"), pydantic.Field(alias="entryInformation")
    ]
    fields: Fields
    folder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that contains the Study."),
    ]
    """
    ID of the folder that contains the Study.
    """

    name: str = pydantic.Field()
    """
    Name of the Study.
    """

    study_schema_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="studySchemaId"),
        pydantic.Field(alias="studySchemaId", description="The ID of the Study's schema."),
    ]
    """
    The ID of the Study's schema.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
