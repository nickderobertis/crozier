

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_grant import UserGrant


class GetAgentGrantsResponse(UniversalBaseModel):
    data: typing.List[UserGrant] = pydantic.Field()
    """
    Array of user grants for the specified agent.
    Typically contains one grant (upsert semantics).
    Empty array if no grants exist.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
