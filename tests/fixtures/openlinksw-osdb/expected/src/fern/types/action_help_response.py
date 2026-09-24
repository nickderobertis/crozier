

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_help import ActionHelp
from .action_help_response_status import ActionHelpResponseStatus


class ActionHelpResponse(UniversalBaseModel):
    api: str = pydantic.Field()
    """
    The path of the REST API method
    """

    method: str = pydantic.Field()
    """
    The name of the REST API method
    """

    response: ActionHelp
    status: ActionHelpResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
