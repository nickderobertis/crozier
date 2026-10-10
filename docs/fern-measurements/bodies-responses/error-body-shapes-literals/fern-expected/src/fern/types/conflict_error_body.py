

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .conflict_error_body_state import ConflictErrorBodyState
from .journal_context import JournalContext


class ConflictErrorBody(UniversalBaseModel):
    state: ConflictErrorBodyState
    context: JournalContext

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
