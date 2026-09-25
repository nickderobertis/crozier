

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .has_max_choices import HasMaxChoices
from .has_min_choices import HasMinChoices
from .html import Html
from .is_first_option import IsFirstOption
from .is_hidden import IsHidden
from .is_last_option import IsLastOption
from .is_required import IsRequired
from .max_choices import MaxChoices
from .min_choices import MinChoices
from .name import Name
from .option_index import OptionIndex


class MatrixRowPayload(UniversalBaseModel):
    """
    Payload for MATRIX_ROW block type. Used for matrix question rows.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[IsRequired], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    index: OptionIndex
    is_first: typing_extensions.Annotated[
        IsFirstOption, FieldMetadata(alias="isFirst"), pydantic.Field(alias="isFirst")
    ]
    is_last: typing_extensions.Annotated[IsLastOption, FieldMetadata(alias="isLast"), pydantic.Field(alias="isLast")]
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
    name: typing.Optional[Name] = None
    html: typing.Optional[Html] = None
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display text for this matrix row.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
