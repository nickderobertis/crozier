

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_metadata import PageMetadata
from .subscription_response import SubscriptionResponse


class SubscriptionPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.Optional[typing.List[SubscriptionResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
