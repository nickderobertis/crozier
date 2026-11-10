

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_usage_unit import ModelUsageUnit


class Model(UniversalBaseModel):
    """
    Model definition used for transforming usage into USD cost and/or tokenization.
    """

    id: str
    model_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="modelName"),
        pydantic.Field(
            alias="modelName",
            description="Name of the model definition. If multiple with the same name exist, they are applied in the following order: (1) custom over built-in, (2) newest according to startTime where model.startTime<observation.startTime",
        ),
    ]
    """
    Name of the model definition. If multiple with the same name exist, they are applied in the following order: (1) custom over built-in, (2) newest according to startTime where model.startTime<observation.startTime
    """

    match_pattern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="matchPattern"),
        pydantic.Field(
            alias="matchPattern",
            description="Regex pattern which matches this model definition to generation.model. Useful in case of fine-tuned models. If you want to exact match, use `(?i)^modelname$`",
        ),
    ]
    """
    Regex pattern which matches this model definition to generation.model. Useful in case of fine-tuned models. If you want to exact match, use `(?i)^modelname$`
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startDate"),
        pydantic.Field(alias="startDate", description="Apply only to generations which are newer than this ISO date."),
    ] = None
    """
    Apply only to generations which are newer than this ISO date.
    """

    unit: typing.Optional[ModelUsageUnit] = pydantic.Field(default=None)
    """
    Unit used by this model.
    """

    input_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="inputPrice"),
        pydantic.Field(alias="inputPrice", description="Price (USD) per input unit"),
    ] = None
    """
    Price (USD) per input unit
    """

    output_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outputPrice"),
        pydantic.Field(alias="outputPrice", description="Price (USD) per output unit"),
    ] = None
    """
    Price (USD) per output unit
    """

    total_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalPrice"),
        pydantic.Field(
            alias="totalPrice", description="Price (USD) per total unit. Cannot be set if input or output price is set."
        ),
    ] = None
    """
    Price (USD) per total unit. Cannot be set if input or output price is set.
    """

    tokenizer_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tokenizerId"),
        pydantic.Field(
            alias="tokenizerId",
            description="Optional. Tokenizer to be applied to observations which match to this model. See docs for more details.",
        ),
    ] = None
    """
    Optional. Tokenizer to be applied to observations which match to this model. See docs for more details.
    """

    tokenizer_config: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="tokenizerConfig"),
        pydantic.Field(
            alias="tokenizerConfig",
            description="Optional. Configuration for the selected tokenizer. Needs to be JSON. See docs for more details.",
        ),
    ] = None
    """
    Optional. Configuration for the selected tokenizer. Needs to be JSON. See docs for more details.
    """

    is_langfuse_managed: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isLangfuseManaged"), pydantic.Field(alias="isLangfuseManaged")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
