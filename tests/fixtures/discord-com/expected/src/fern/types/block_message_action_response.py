

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .block_message_action_metadata_response import BlockMessageActionMetadataResponse


class BlockMessageActionResponse(UniversalBaseModel):
    type: int
    metadata: BlockMessageActionMetadataResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
