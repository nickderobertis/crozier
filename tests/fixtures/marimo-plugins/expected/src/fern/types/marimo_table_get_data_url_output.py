

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_get_data_url_output_data_url import MarimoTableGetDataUrlOutputDataUrl
from .marimo_table_get_data_url_output_format import MarimoTableGetDataUrlOutputFormat


class MarimoTableGetDataUrlOutput(UniversalBaseModel):
    data_url: MarimoTableGetDataUrlOutputDataUrl
    format: MarimoTableGetDataUrlOutputFormat

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
