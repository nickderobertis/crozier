

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_dataframe_search_output_data import MarimoDataframeSearchOutputData


class MarimoDataframeSearchOutput(UniversalBaseModel):
    data: MarimoDataframeSearchOutputData
    total_rows: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
