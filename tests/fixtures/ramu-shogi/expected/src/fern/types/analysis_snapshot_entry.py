

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class AnalysisSnapshotEntry(UniversalBaseModel):
    ply: int
    eval_cp: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="evalCp"), pydantic.Field(alias="evalCp")
    ] = None
    eval_mate: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="evalMate"),
        pydantic.Field(
            alias="evalMate",
            description="詰み手数 (先手視点、+ が先手勝ち)。手数不明の詰みは予約センチネル ±100000 で表す。",
        ),
    ] = None
    """
    詰み手数 (先手視点、+ が先手勝ち)。手数不明の詰みは予約センチネル ±100000 で表す。
    """

    depth: typing.Optional[int] = None
    pv: typing.Optional[typing.List[str]] = None
    multi_pv: typing_extensions.Annotated[
        typing.Optional["JsonValue"], FieldMetadata(alias="multiPv"), pydantic.Field(alias="multiPv")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value import JsonValue

update_forward_refs(AnalysisSnapshotEntry, JsonValue=JsonValue)
