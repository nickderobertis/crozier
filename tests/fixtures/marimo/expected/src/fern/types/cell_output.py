

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_channel import CellChannel
from .cell_output_data import CellOutputData
from .cell_output_mimetype import CellOutputMimetype


class CellOutput(UniversalBaseModel):
    channel: CellChannel
    data: CellOutputData
    mimetype: CellOutputMimetype
    timestamp: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
