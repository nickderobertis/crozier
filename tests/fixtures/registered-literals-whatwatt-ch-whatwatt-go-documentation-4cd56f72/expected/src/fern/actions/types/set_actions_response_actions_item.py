

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_actions_response_actions_item_requests_item import SetActionsResponseActionsItemRequestsItem


class SetActionsResponseActionsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    enable: typing.Optional[bool] = None
    requests: typing.Optional[typing.List[SetActionsResponseActionsItemRequestsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
