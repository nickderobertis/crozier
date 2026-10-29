

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .concept_element_id import ConceptElementId
from .cq_concept_tables import CqConceptTables
from .cq_days_before_days import CqDaysBeforeDays
from .cq_external_format_item import CqExternalFormatItem
from .date_range import DateRange
from .execution_id import ExecutionId
from .select_id import SelectId


class CqElement_And(UniversalBaseModel):
    type: typing.Literal["AND"] = "AND"
    children: typing.Optional[typing.List["CqElement"]] = None
    create_exists: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="createExists"), pydantic.Field(alias="createExists")
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_Before(UniversalBaseModel):
    type: typing.Literal["BEFORE"] = "BEFORE"
    index: typing.Optional["CqSampled"] = None
    preceding: typing.Optional["CqSampled"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_BeforeOrNever(UniversalBaseModel):
    type: typing.Literal["BEFORE_OR_NEVER"] = "BEFORE_OR_NEVER"
    days: typing.Optional[int] = None
    index: typing.Optional["CqSampled"] = None
    preceding: typing.Optional["CqSampled"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_BeforeOrSame(UniversalBaseModel):
    type: typing.Literal["BEFORE_OR_SAME"] = "BEFORE_OR_SAME"
    index: typing.Optional["CqSampled"] = None
    preceding: typing.Optional["CqSampled"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_Concept(UniversalBaseModel):
    type: typing.Literal["CONCEPT"] = "CONCEPT"
    ids: typing.Optional[ConceptElementId] = None
    tables: typing.Optional[CqConceptTables] = None
    selects: typing.Optional[typing.List[SelectId]] = None
    exclude_from_secondary_id: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromSecondaryId"),
        pydantic.Field(alias="excludeFromSecondaryId"),
    ] = None
    exclude_from_time_aggregation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromTimeAggregation"),
        pydantic.Field(alias="excludeFromTimeAggregation"),
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_DateRestriction(UniversalBaseModel):
    type: typing.Literal["DATE_RESTRICTION"] = "DATE_RESTRICTION"
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    child: typing.Optional["CqElement"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_DaysBefore(UniversalBaseModel):
    type: typing.Literal["DAYS_BEFORE"] = "DAYS_BEFORE"
    days: typing.Optional[CqDaysBeforeDays] = None
    index: typing.Optional["CqSampled"] = None
    preceding: typing.Optional["CqSampled"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_External(UniversalBaseModel):
    type: typing.Literal["EXTERNAL"] = "EXTERNAL"
    format: typing.Optional[typing.List[CqExternalFormatItem]] = None
    values: typing.Optional[typing.List[typing.List[str]]] = None
    only_singles: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="onlySingles"), pydantic.Field(alias="onlySingles")
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_Negation(UniversalBaseModel):
    type: typing.Literal["NEGATION"] = "NEGATION"
    child: typing.Optional["CqElement"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_Or(UniversalBaseModel):
    type: typing.Literal["OR"] = "OR"
    children: typing.Optional[typing.List["CqElement"]] = None
    create_exists: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="createExists"), pydantic.Field(alias="createExists")
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_ResultInfoDecorator(UniversalBaseModel):
    type: typing.Literal["RESULT_INFO_DECORATOR"] = "RESULT_INFO_DECORATOR"
    values: typing.Optional[typing.Dict[str, str]] = None
    child: typing.Optional["CqElement"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_Same(UniversalBaseModel):
    type: typing.Literal["SAME"] = "SAME"
    index: typing.Optional["CqSampled"] = None
    preceding: typing.Optional["CqSampled"] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CqElement_SavedQuery(UniversalBaseModel):
    type: typing.Literal["SAVED_QUERY"] = "SAVED_QUERY"
    query_id: typing_extensions.Annotated[
        typing.Optional[ExecutionId], FieldMetadata(alias="queryId"), pydantic.Field(alias="queryId")
    ] = None
    exclude_from_secondary_id: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromSecondaryId"),
        pydantic.Field(alias="excludeFromSecondaryId"),
    ] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CqElement = typing_extensions.Annotated[
    typing.Union[
        CqElement_And,
        CqElement_Before,
        CqElement_BeforeOrNever,
        CqElement_BeforeOrSame,
        CqElement_Concept,
        CqElement_DateRestriction,
        CqElement_DaysBefore,
        CqElement_External,
        CqElement_Negation,
        CqElement_Or,
        CqElement_ResultInfoDecorator,
        CqElement_Same,
        CqElement_SavedQuery,
    ],
    pydantic.Field(discriminator="type"),
]
from .cq_before import CqBefore
from .cq_before_or_same import CqBeforeOrSame
from .cq_date_restriction import CqDateRestriction
from .cq_days_before import CqDaysBefore
from .cq_days_before_or_never import CqDaysBeforeOrNever
from .cq_negation import CqNegation
from .cq_or import CqOr
from .cq_result_info_decorator import CqResultInfoDecorator
from .cq_same import CqSame
from .cq_sampled import CqSampled
from .cq_and import CqAnd

update_forward_refs(
    CqElement_And,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_Before,
    CqAnd=CqAnd,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_BeforeOrNever,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_BeforeOrSame,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_DateRestriction,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_DaysBefore,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_Negation,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_Or,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_ResultInfoDecorator,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    CqElement_Same,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSampled=CqSampled,
)
