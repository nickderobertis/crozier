

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KvsCnTreeGetResponseNodesItemKvsetsOneItemJob(UniversalBaseModel):
    id: typing.Optional[int] = None
    action: typing.Optional[str] = None
    rule: typing.Optional[str] = None
    wmesg: typing.Optional[str] = None
    time: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
