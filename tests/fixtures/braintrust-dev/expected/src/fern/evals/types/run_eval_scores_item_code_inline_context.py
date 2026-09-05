

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_eval_scores_item_code_inline_context_runtime import RunEvalScoresItemCodeInlineContextRuntime


class RunEvalScoresItemCodeInlineContext(UniversalBaseModel):
    runtime: RunEvalScoresItemCodeInlineContextRuntime
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
