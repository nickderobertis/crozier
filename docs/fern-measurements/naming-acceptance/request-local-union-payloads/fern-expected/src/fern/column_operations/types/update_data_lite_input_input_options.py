

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateDataLiteInputInputOptions_Csv(UniversalBaseModel):
    file_format: typing.Literal["csv"] = "csv"
    row_group: typing.Optional[int] = None
    delimiter: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateDataLiteInputInputOptions_Parquet(UniversalBaseModel):
    file_format: typing.Literal["parquet"] = "parquet"
    row_group: typing.Optional[int] = None
    delimiter: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UpdateDataLiteInputInputOptions = typing_extensions.Annotated[
    typing.Union[UpdateDataLiteInputInputOptions_Csv, UpdateDataLiteInputInputOptions_Parquet],
    pydantic.Field(discriminator="file_format"),
]
