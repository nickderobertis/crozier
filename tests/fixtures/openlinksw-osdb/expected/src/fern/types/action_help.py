

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ActionHelp(UniversalBaseModel):
    action_id: str = pydantic.Field()
    """
    A unique one word identifier for the action.
    """

    help_text: str = pydantic.Field()
    """
    The help text for the action.
    """

    service_id: str = pydantic.Field()
    """
    A unique one word identifier for the service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
