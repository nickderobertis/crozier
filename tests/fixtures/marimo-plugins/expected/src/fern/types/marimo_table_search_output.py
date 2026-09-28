

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_search_output_data import MarimoTableSearchOutputData
from .marimo_table_search_output_raw_data import MarimoTableSearchOutputRawData
from .marimo_table_search_output_total_rows import MarimoTableSearchOutputTotalRows


class MarimoTableSearchOutput(UniversalBaseModel):
    data: MarimoTableSearchOutputData
    total_rows: MarimoTableSearchOutputTotalRows
    cell_styles: typing.Optional[
        typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]]
    ] = None
    cell_hover_texts: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Optional[str]]]]] = None
    raw_data: typing.Optional[MarimoTableSearchOutputRawData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
