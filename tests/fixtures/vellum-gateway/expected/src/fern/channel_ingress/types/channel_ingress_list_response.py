

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_ingress_list_response_problems_item import ChannelIngressListResponseProblemsItem
from .channel_ingress_list_response_sources_item import ChannelIngressListResponseSourcesItem


class ChannelIngressListResponse(UniversalBaseModel):
    sources: typing.List[ChannelIngressListResponseSourcesItem]
    problems: typing.List[ChannelIngressListResponseProblemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
