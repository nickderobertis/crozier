

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .default_answer_number import DefaultAnswerNumber
from .has_default_answer import HasDefaultAnswer
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class RatingPayload(UniversalBaseModel):
    """
    Payload for RATING block type. Used for star rating questions.
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
        typing.Optional[DefaultAnswerNumber],
        FieldMetadata(alias="defaultAnswer"),
        pydantic.Field(alias="defaultAnswer"),
    ] = None
    stars: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of stars for the rating scale (1-10). Defaults to 5.
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
