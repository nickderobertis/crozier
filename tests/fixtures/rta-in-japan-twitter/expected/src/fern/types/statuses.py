

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .media import Media
from .statuses_entities import StatusesEntities
from .user import User


class Statuses(UniversalBaseModel):
    id: str
    text: str
    user: User
    created_at: dt.datetime
    entities: typing.Optional[StatusesEntities] = None
    media: typing.Optional[typing.List[Media]] = None
    in_reply_to_status: typing.Optional["Statuses"] = None
    quoted_status: typing.Optional["Statuses"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Statuses)
