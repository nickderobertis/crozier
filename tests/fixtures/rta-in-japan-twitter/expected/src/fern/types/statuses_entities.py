

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .statuses_entities_mentions_item import StatusesEntitiesMentionsItem
from .statuses_entities_urls_item import StatusesEntitiesUrlsItem


class StatusesEntities(UniversalBaseModel):
    annotations: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    urls: typing.Optional[typing.List[StatusesEntitiesUrlsItem]] = None
    hashtags: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    mentions: typing.Optional[typing.List[StatusesEntitiesMentionsItem]] = None
    cashtags: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
