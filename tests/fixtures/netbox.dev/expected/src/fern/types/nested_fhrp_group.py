

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_fhrp_group_protocol import NestedFhrpGroupProtocol


class NestedFhrpGroup(UniversalBaseModel):
    display: typing.Optional[str] = None
    group_id: int
    id: typing.Optional[int] = None
    protocol: NestedFhrpGroupProtocol
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
