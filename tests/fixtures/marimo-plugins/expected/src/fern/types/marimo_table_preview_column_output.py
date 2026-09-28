

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_preview_column_output_stats import MarimoTablePreviewColumnOutputStats


class MarimoTablePreviewColumnOutput(UniversalBaseModel):
    chart_spec: typing.Optional[str] = None
    chart_code: typing.Optional[str] = None
    error: typing.Optional[str] = None
    missing_packages: typing.Optional[typing.List[str]] = None
    stats: typing.Optional[MarimoTablePreviewColumnOutputStats] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
