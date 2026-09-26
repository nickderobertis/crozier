

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .default_answer_string import DefaultAnswerString
from .has_default_answer import HasDefaultAnswer
from .has_max_choices import HasMaxChoices
from .has_min_choices import HasMinChoices
from .is_first_option import IsFirstOption
from .is_hidden import IsHidden
from .is_last_option import IsLastOption
from .is_required import IsRequired
from .max_choices import MaxChoices
from .min_choices import MinChoices
from .name import Name
from .option_index import OptionIndex


class CheckboxPayload(UniversalBaseModel):
    """
    Payload for CHECKBOX block type. Used for individual checkbox options within a checkbox group.
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
    index: OptionIndex
    is_first: typing_extensions.Annotated[
        IsFirstOption, FieldMetadata(alias="isFirst"), pydantic.Field(alias="isFirst")
    ]
    is_last: typing_extensions.Annotated[IsLastOption, FieldMetadata(alias="isLast"), pydantic.Field(alias="isLast")]
    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of an image displayed alongside this checkbox option.
    """

    has_min_choices: typing_extensions.Annotated[
        typing.Optional[HasMinChoices], FieldMetadata(alias="hasMinChoices"), pydantic.Field(alias="hasMinChoices")
    ] = None
    min_choices: typing_extensions.Annotated[
        typing.Optional[MinChoices], FieldMetadata(alias="minChoices"), pydantic.Field(alias="minChoices")
    ] = None
    has_max_choices: typing_extensions.Annotated[
        typing.Optional[HasMaxChoices], FieldMetadata(alias="hasMaxChoices"), pydantic.Field(alias="hasMaxChoices")
    ] = None
    max_choices: typing_extensions.Annotated[
        typing.Optional[MaxChoices], FieldMetadata(alias="maxChoices"), pydantic.Field(alias="maxChoices")
    ] = None
    has_other_option: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasOtherOption"),
        pydantic.Field(alias="hasOtherOption", description="True if the question group has an 'Other' option enabled."),
    ] = None
    """
    True if the question group has an 'Other' option enabled.
    """

    is_other_option: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isOtherOption"),
        pydantic.Field(
            alias="isOtherOption", description="True if this specific option is the 'Other' free-text field."
        ),
    ] = None
    """
    True if this specific option is the 'Other' free-text field.
    """

    randomize: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Randomize option order. Only needs to be set on the first option in the group.
    """

    lock_in_place: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="lockInPlace"),
        pydantic.Field(
            alias="lockInPlace",
            description="Array of option UUIDs that stay in their original position when randomize is enabled.",
        ),
    ] = None
    """
    Array of option UUIDs that stay in their original position when randomize is enabled.
    """

    name: typing.Optional[Name] = None
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display text of the checkbox option.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
