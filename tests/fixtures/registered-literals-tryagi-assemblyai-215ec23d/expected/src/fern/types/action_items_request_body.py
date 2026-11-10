

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_items_request_body_action_items import ActionItemsRequestBodyActionItems


class ActionItemsRequestBody(UniversalBaseModel):
    """
    Request body for [Action Items](https://www.assemblyai.com/docs/speech-understanding/action-items).
    """

    action_items: ActionItemsRequestBodyActionItems

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
