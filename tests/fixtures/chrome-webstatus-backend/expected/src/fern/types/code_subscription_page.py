

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_subscription_response import CodeSubscriptionResponse
from .page_metadata import PageMetadata


class CodeSubscriptionPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.Optional[typing.List[CodeSubscriptionResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
