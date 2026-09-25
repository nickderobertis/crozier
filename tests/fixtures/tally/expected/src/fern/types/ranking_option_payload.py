

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
from .html import Html
from .is_first_option import IsFirstOption
from .is_hidden import IsHidden
from .is_last_option import IsLastOption
from .is_required import IsRequired
from .name import Name
from .option_index import OptionIndex


class RankingOptionPayload(UniversalBaseModel):
    """
    Payload for RANKING_OPTION block type. Used for ranking/ordering questions.
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
    html: typing.Optional[Html] = None
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the ranking option.
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image of the ranking option.
    """

    randomize: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to randomize the ranking options. Only needs to be set on the first option in the group.
    """

    lock_in_place: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="lockInPlace"),
        pydantic.Field(
            alias="lockInPlace",
            description="Array of option UUIDs that should stay in their original position when randomize is enabled. Only needs to be set on the first option in the group.",
        ),
    ] = None
    """
    Array of option UUIDs that should stay in their original position when randomize is enabled. Only needs to be set on the first option in the group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
