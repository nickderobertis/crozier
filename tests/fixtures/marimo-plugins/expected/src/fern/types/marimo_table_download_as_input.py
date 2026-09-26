

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_download_as_input_format import MarimoTableDownloadAsInputFormat


class MarimoTableDownloadAsInput(UniversalBaseModel):
    format: MarimoTableDownloadAsInputFormat

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
