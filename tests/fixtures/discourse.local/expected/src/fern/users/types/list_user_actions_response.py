

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_user_actions_response_user_actions_item import ListUserActionsResponseUserActionsItem


class ListUserActionsResponse(UniversalBaseModel):
    user_actions: typing.List[ListUserActionsResponseUserActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
