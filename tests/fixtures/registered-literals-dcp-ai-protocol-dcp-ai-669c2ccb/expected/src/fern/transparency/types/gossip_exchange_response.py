

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.signed_tree_head import SignedTreeHead
from ...types.split_view_alert import SplitViewAlert


class GossipExchangeResponse(UniversalBaseModel):
    sth: typing.Optional[SignedTreeHead] = None
    alert: typing.Optional[SplitViewAlert] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
