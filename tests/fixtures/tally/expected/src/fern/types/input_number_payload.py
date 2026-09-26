

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .decimal_separator import DecimalSeparator
from .default_answer_string import DefaultAnswerString
from .has_default_answer import HasDefaultAnswer
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name
from .number_format import NumberFormat
from .thousands_separator import ThousandsSeparator


class InputNumberPayload(UniversalBaseModel):
    """
    Payload for INPUT_NUMBER block type. Used for numeric input fields.
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
    has_min_number: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMinNumber"),
        pydantic.Field(
            alias="hasMinNumber",
            description="Set to true to enable minNumber; minNumber must be present if hasMinNumber is true.",
        ),
    ] = None
    """
    Set to true to enable minNumber; minNumber must be present if hasMinNumber is true.
    """

    min_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="minNumber"),
        pydantic.Field(alias="minNumber", description="The minimum allowed value (required if hasMinNumber is true)."),
    ] = None
    """
    The minimum allowed value (required if hasMinNumber is true).
    """

    has_max_number: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMaxNumber"),
        pydantic.Field(
            alias="hasMaxNumber",
            description="Set to true to enable maxNumber; maxNumber must be present if hasMaxNumber is true.",
        ),
    ] = None
    """
    Set to true to enable maxNumber; maxNumber must be present if hasMaxNumber is true.
    """

    max_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxNumber"),
        pydantic.Field(alias="maxNumber", description="The maximum allowed value (required if hasMaxNumber is true)."),
    ] = None
    """
    The maximum allowed value (required if hasMaxNumber is true).
    """

    decimal_separator: typing_extensions.Annotated[
        typing.Optional[DecimalSeparator],
        FieldMetadata(alias="decimalSeparator"),
        pydantic.Field(alias="decimalSeparator"),
    ] = None
    thousands_separator: typing_extensions.Annotated[
        typing.Optional[ThousandsSeparator],
        FieldMetadata(alias="thousandsSeparator"),
        pydantic.Field(alias="thousandsSeparator"),
    ] = None
    format: typing.Optional[NumberFormat] = None
    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom prefix to display before the number (e.g., currency symbol). Used with NumberFormat.Custom.
    """

    suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom suffix to display after the number (e.g., unit). Used with NumberFormat.Custom.
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
