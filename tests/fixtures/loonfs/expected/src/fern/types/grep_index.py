

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .pin_id import PinId
from .run_no import RunNo


class GrepIndex_Active(UniversalBaseModel):
    """
    The maintenance status of a namespace's grep index.
    """

    status: typing.Literal["active"] = "active"
    built_through_seq: ChangeSeq
    namespace_id: NamespaceId
    next_event_index: int
    next_run_no: RunNo
    reorganize_pending: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GrepIndex_Backfilling(UniversalBaseModel):
    """
    The maintenance status of a namespace's grep index.
    """

    status: typing.Literal["backfilling"] = "backfilling"
    captured_seq: ChangeSeq
    checkpoint_id: PinId
    cursor_inode_id: typing.Optional[InodeId] = None
    namespace_id: NamespaceId
    next_run_no: RunNo
    reorganize_pending: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GrepIndex_Disabled(UniversalBaseModel):
    """
    The maintenance status of a namespace's grep index.
    """

    status: typing.Literal["disabled"] = "disabled"
    namespace_id: NamespaceId
    next_run_no: RunNo
    reorganize_pending: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GrepIndex = typing_extensions.Annotated[
    typing.Union[GrepIndex_Active, GrepIndex_Backfilling, GrepIndex_Disabled], pydantic.Field(discriminator="status")
]
