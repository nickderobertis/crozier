

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class GetDatasetsDatasetNameDetailsItemIdResponse(UniversalBaseModel):
    item_id: typing.Optional[str] = None
    item_data: typing.Optional[typing.List["Block"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.block import Block
from ...types.block_value import BlockValue

update_forward_refs(GetDatasetsDatasetNameDetailsItemIdResponse, Block=Block, BlockValue=BlockValue)
