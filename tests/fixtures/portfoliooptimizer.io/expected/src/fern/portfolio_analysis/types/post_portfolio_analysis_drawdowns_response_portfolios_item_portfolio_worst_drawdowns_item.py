

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem(UniversalBaseModel):
    drawdown_bottom: typing_extensions.Annotated[
        int, FieldMetadata(alias="drawdownBottom"), pydantic.Field(alias="drawdownBottom")
    ]
    drawdown_depth: typing_extensions.Annotated[
        float, FieldMetadata(alias="drawdownDepth"), pydantic.Field(alias="drawdownDepth")
    ]
    drawdown_end: typing_extensions.Annotated[
        int, FieldMetadata(alias="drawdownEnd"), pydantic.Field(alias="drawdownEnd")
    ]
    drawdown_start: typing_extensions.Annotated[
        int, FieldMetadata(alias="drawdownStart"), pydantic.Field(alias="drawdownStart")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
