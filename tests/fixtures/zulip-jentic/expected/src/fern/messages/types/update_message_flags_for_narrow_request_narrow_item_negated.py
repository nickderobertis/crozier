

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_message_flags_for_narrow_request_narrow_item_negated_operand import (
    UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand,
)


class UpdateMessageFlagsForNarrowRequestNarrowItemNegated(UniversalBaseModel):
    operator: str
    operand: UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand
    negated: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
