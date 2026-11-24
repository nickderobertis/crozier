

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AllInputOptionsInput_Parquet(UniversalBaseModel):
    file_format: typing.Literal["parquet"] = "parquet"
    row_group: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllInputOptionsInput_Csv(UniversalBaseModel):
    file_format: typing.Literal["csv"] = "csv"
    delimiter: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AllInputOptionsInput = typing_extensions.Annotated[
    typing.Union[AllInputOptionsInput_Parquet, AllInputOptionsInput_Csv], pydantic.Field(discriminator="file_format")
]
