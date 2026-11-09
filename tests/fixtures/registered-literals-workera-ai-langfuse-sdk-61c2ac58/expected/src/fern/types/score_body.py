

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_score_value import CreateScoreValue
from .score_data_type import ScoreDataType


class ScoreBody(UniversalBaseModel):
    id: typing.Optional[str] = None
    trace_id: typing_extensions.Annotated[str, FieldMetadata(alias="traceId"), pydantic.Field(alias="traceId")]
    name: str
    environment: typing.Optional[str] = None
    value: CreateScoreValue = pydantic.Field()
    """
    The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)
    """

    observation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="observationId"), pydantic.Field(alias="observationId")
    ] = None
    comment: typing.Optional[str] = None
    data_type: typing_extensions.Annotated[
        typing.Optional[ScoreDataType],
        FieldMetadata(alias="dataType"),
        pydantic.Field(
            alias="dataType",
            description="When set, must match the score value's type. If not set, will be inferred from the score value or config",
        ),
    ] = None
    """
    When set, must match the score value's type. If not set, will be inferred from the score value or config
    """

    config_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="configId"),
        pydantic.Field(
            alias="configId",
            description="Reference a score config on a score. When set, the score name must equal the config name and scores must comply with the config's range and data type. For categorical scores, the value must map to a config category. Numeric scores might be constrained by the score config's max and min values",
        ),
    ] = None
    """
    Reference a score config on a score. When set, the score name must equal the config name and scores must comply with the config's range and data type. For categorical scores, the value must map to a config category. Numeric scores might be constrained by the score config's max and min values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
