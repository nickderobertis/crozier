

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.block import Block


class ListFormBlocksResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    blocks: typing.Optional[typing.List[Block]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ListFormBlocksResponse)
