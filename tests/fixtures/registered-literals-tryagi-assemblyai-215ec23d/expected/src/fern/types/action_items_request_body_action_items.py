

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_items_request_body_action_items_effort import ActionItemsRequestBodyActionItemsEffort


class ActionItemsRequestBodyActionItems(UniversalBaseModel):
    include_decisions: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Option to include decision making in action items.
    """

    effort: typing.Optional[ActionItemsRequestBodyActionItemsEffort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
