

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .insight_example import InsightExample


class InsightWithMetadata(UniversalBaseModel):
    insight_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="insightText"), pydantic.Field(alias="insightText")
    ]
    number_of_queries: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfQueries"), pydantic.Field(alias="numberOfQueries")
    ]
    examples: typing.List[InsightExample]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
