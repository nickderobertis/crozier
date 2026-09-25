

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .default_answer_string import DefaultAnswerString
from .disable_days import DisableDays
from .has_default_answer import HasDefaultAnswer
from .input_date_payload_date_range import InputDatePayloadDateRange
from .input_date_payload_format import InputDatePayloadFormat
from .input_date_payload_start_week_on import InputDatePayloadStartWeekOn
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class InputDatePayload(UniversalBaseModel):
    """
    Payload for INPUT_DATE block type. Used for date picker fields.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[IsRequired], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    has_default_answer: typing_extensions.Annotated[
        typing.Optional[HasDefaultAnswer],
        FieldMetadata(alias="hasDefaultAnswer"),
        pydantic.Field(alias="hasDefaultAnswer"),
    ] = None
    default_answer: typing_extensions.Annotated[
        typing.Optional[DefaultAnswerString],
        FieldMetadata(alias="defaultAnswer"),
        pydantic.Field(alias="defaultAnswer"),
    ] = None
    placeholder: typing.Optional[str] = None
    disable_days: typing_extensions.Annotated[
        typing.Optional[typing.List[DisableDays]],
        FieldMetadata(alias="disableDays"),
        pydantic.Field(alias="disableDays", description="Array of days or date ranges to disable in the date picker."),
    ] = None
    """
    Array of days or date ranges to disable in the date picker.
    """

    format: typing.Optional[InputDatePayloadFormat] = pydantic.Field(default=None)
    """
    Display format for the date.
    """

    before_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="beforeDate"),
        pydantic.Field(alias="beforeDate", description="Disable dates before this date."),
    ] = None
    """
    Disable dates before this date.
    """

    after_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="afterDate"),
        pydantic.Field(alias="afterDate", description="Disable dates after this date."),
    ] = None
    """
    Disable dates after this date.
    """

    date_range: typing_extensions.Annotated[
        typing.Optional[InputDatePayloadDateRange],
        FieldMetadata(alias="dateRange"),
        pydantic.Field(alias="dateRange", description="Restrict selectable dates to a specific range."),
    ] = None
    """
    Restrict selectable dates to a specific range.
    """

    specific_dates: typing_extensions.Annotated[
        typing.Optional[typing.List[dt.date]],
        FieldMetadata(alias="specificDates"),
        pydantic.Field(alias="specificDates", description="Array of specific dates to disable."),
    ] = None
    """
    Array of specific dates to disable.
    """

    start_week_on: typing_extensions.Annotated[
        typing.Optional[InputDatePayloadStartWeekOn],
        FieldMetadata(alias="startWeekOn"),
        pydantic.Field(
            alias="startWeekOn",
            description="Day the week starts on in the calendar view. 0=Sunday, 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday.",
        ),
    ] = None
    """
    Day the week starts on in the calendar view. 0=Sunday, 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday.
    """

    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None
    name: typing.Optional[Name] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
