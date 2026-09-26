

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok86(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    description: str
    fully_specified_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fullySpecifiedName"), pydantic.Field(alias="fullySpecifiedName")
    ]
    is_chronic: typing_extensions.Annotated[str, FieldMetadata(alias="isChronic"), pydantic.Field(alias="isChronic")]
    has_secondary_condition: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasSecondaryCondition"), pydantic.Field(alias="hasSecondaryCondition")
    ]
    problem_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="problemStatusId"), pydantic.Field(alias="problemStatusId")
    ]
    problem_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="problemStatus"), pydantic.Field(alias="problemStatus")
    ]
    recent_note_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="recentNoteId"), pydantic.Field(alias="recentNoteId")
    ]
    last_addressed_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAddressedDate"), pydantic.Field(alias="lastAddressedDate")
    ]
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    resolved_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedReason"), pydantic.Field(alias="resolvedReason")
    ]
    concept_id: typing_extensions.Annotated[str, FieldMetadata(alias="conceptId"), pydantic.Field(alias="conceptId")]
    is_comorbid: typing_extensions.Annotated[str, FieldMetadata(alias="isComorbid"), pydantic.Field(alias="isComorbid")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
