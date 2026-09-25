

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calculated_field_type import CalculatedFieldType
from .field_block_group_uuid import FieldBlockGroupUuid
from .field_question_type import FieldQuestionType
from .field_type import FieldType
from .field_uuid import FieldUuid


class Field(UniversalBaseModel):
    """
    A reference to a form field, used to dynamically access another field's value (e.g., for default answers or mentions).
    """

    uuid_: typing_extensions.Annotated[
        FieldUuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(
            alias="uuid",
            description="Unique identifier of the referenced field. A UUID for regular fields, or a UtilityUuid value when type is UTILITY.",
        ),
    ]
    """
    Unique identifier of the referenced field. A UUID for regular fields, or a UtilityUuid value when type is UTILITY.
    """

    type: FieldType = pydantic.Field()
    """
    The category of field being referenced.
    """

    question_type: typing_extensions.Annotated[
        FieldQuestionType,
        FieldMetadata(alias="questionType"),
        pydantic.Field(alias="questionType", description="The block type of the referenced field."),
    ]
    """
    The block type of the referenced field.
    """

    block_group_uuid: typing_extensions.Annotated[
        FieldBlockGroupUuid,
        FieldMetadata(alias="blockGroupUuid"),
        pydantic.Field(
            alias="blockGroupUuid",
            description="Identifier of the block group containing the referenced field. A UUID for regular fields, or a UtilityUuid value when type is UTILITY.",
        ),
    ]
    """
    Identifier of the block group containing the referenced field. A UUID for regular fields, or a UtilityUuid value when type is UTILITY.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display title of the referenced field.
    """

    calculated_field_type: typing_extensions.Annotated[
        typing.Optional[CalculatedFieldType],
        FieldMetadata(alias="calculatedFieldType"),
        pydantic.Field(
            alias="calculatedFieldType",
            description="For calculated fields, specifies whether the result is NUMBER or TEXT.",
        ),
    ] = None
    """
    For calculated fields, specifies whether the result is NUMBER or TEXT.
    """

    payload: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional configuration for utility fields. Only present when type is UTILITY.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
