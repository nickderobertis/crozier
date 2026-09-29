

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fleet_ui_message_chunk_data_rlm_code_data import FleetUiMessageChunkDataRlmCodeData


class FleetUiMessageChunkDataRlmCode(UniversalBaseModel):
    id: typing.Optional[str] = None
    data: FleetUiMessageChunkDataRlmCodeData
    transient: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
