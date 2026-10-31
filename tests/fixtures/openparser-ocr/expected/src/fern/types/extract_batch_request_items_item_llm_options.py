

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extract_batch_request_items_item_llm_options_reasoning_effort import (
    ExtractBatchRequestItemsItemLlmOptionsReasoningEffort,
)


class ExtractBatchRequestItemsItemLlmOptions(UniversalBaseModel):
    reasoning_effort: typing.Optional[ExtractBatchRequestItemsItemLlmOptionsReasoningEffort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
