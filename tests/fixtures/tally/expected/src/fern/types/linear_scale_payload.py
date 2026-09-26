

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .has_default_answer import HasDefaultAnswer
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class LinearScalePayload(UniversalBaseModel):
    """
    Payload for LINEAR_SCALE block type. Used for scale/slider questions.
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
        typing.Optional[int],
        FieldMetadata(alias="defaultAnswer"),
        pydantic.Field(
            alias="defaultAnswer", description="Default selected value. Must be within the start-end range."
        ),
    ] = None
    """
    Default selected value. Must be within the start-end range.
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    Starting value of the scale (0-100). Defaults to 0.
    """

    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    Ending value of the scale (0-100). Must be >= start. Defaults to 10.
    """

    step: typing.Optional[int] = pydantic.Field(default=None)
    """
    Step increment between scale values. Must be >= 1. Defaults to 1.
    """

    has_left_label: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasLeftLabel"),
        pydantic.Field(alias="hasLeftLabel", description="When true, leftLabel must be provided."),
    ] = None
    """
    When true, leftLabel must be provided.
    """

    left_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="leftLabel"),
        pydantic.Field(
            alias="leftLabel",
            description="Label displayed at the start of the scale. Required when hasLeftLabel is true.",
        ),
    ] = None
    """
    Label displayed at the start of the scale. Required when hasLeftLabel is true.
    """

    has_center_label: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasCenterLabel"),
        pydantic.Field(alias="hasCenterLabel", description="When true, centerLabel must be provided."),
    ] = None
    """
    When true, centerLabel must be provided.
    """

    center_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="centerLabel"),
        pydantic.Field(
            alias="centerLabel",
            description="Label displayed at the center of the scale. Required when hasCenterLabel is true.",
        ),
    ] = None
    """
    Label displayed at the center of the scale. Required when hasCenterLabel is true.
    """

    has_right_label: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasRightLabel"),
        pydantic.Field(alias="hasRightLabel", description="When true, rightLabel must be provided."),
    ] = None
    """
    When true, rightLabel must be provided.
    """

    right_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rightLabel"),
        pydantic.Field(
            alias="rightLabel",
            description="Label displayed at the end of the scale. Required when hasRightLabel is true.",
        ),
    ] = None
    """
    Label displayed at the end of the scale. Required when hasRightLabel is true.
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
