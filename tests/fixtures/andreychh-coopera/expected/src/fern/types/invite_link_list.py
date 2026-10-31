

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_link import InviteLink


class InviteLinkList(UniversalBaseModel):
    """
    Invite links in an object, for the same reason teams are: a team that has issued many of them will one day be answered a page at a time, and the room for saying so has to exist before it is needed.
    """

    items: typing.List[InviteLink]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
