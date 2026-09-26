

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .game_record_summary import GameRecordSummary


class GameRecordDetail(GameRecordSummary):
    initial_sfen: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialSfen"), pydantic.Field(alias="initialSfen")
    ]
    metadata: typing.Optional["JsonValue"] = None
    moves: typing.List[str]
    kifu_text: typing_extensions.Annotated[str, FieldMetadata(alias="kifuText"), pydantic.Field(alias="kifuText")]
    started_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value import JsonValue

update_forward_refs(GameRecordDetail, JsonValue=JsonValue)
