

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataDisciplinaryHistoryArrayItem(UniversalBaseModel):
    action: typing.Optional[str] = None
    case_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseNumber"), pydantic.Field(alias="caseNumber")
    ] = None
    complaint: typing.Optional[str] = None
    contact_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contactId"), pydantic.Field(alias="contactId")
    ] = None
    date_of_action: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateOfAction"), pydantic.Field(alias="dateOfAction")
    ] = None
    definition: typing.Optional[str] = None
    disciplinary_decision: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="disciplinaryDecision"), pydantic.Field(alias="disciplinaryDecision")
    ] = None
    entry_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="entryDate"), pydantic.Field(alias="entryDate")
    ] = None
    information: typing.Optional[str] = None
    link: typing.Optional[str] = None
    note: typing.Optional[str] = None
    probation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="probationDate"), pydantic.Field(alias="probationDate")
    ] = None
    reinstated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="reinstatedDate"), pydantic.Field(alias="reinstatedDate")
    ] = None
    rule: typing.Optional[str] = None
    rule_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ruleNumber"), pydantic.Field(alias="ruleNumber")
    ] = None
    section_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="sectionDate"), pydantic.Field(alias="sectionDate")
    ] = None
    status: typing.Optional[str] = None
    stay_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="stayDate"), pydantic.Field(alias="stayDate")
    ] = None
    supreme_court: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supremeCourt"), pydantic.Field(alias="supremeCourt")
    ] = None
    term: typing.Optional[str] = None
    type_of_action: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeOfAction"), pydantic.Field(alias="typeOfAction")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
