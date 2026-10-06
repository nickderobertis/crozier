

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProviderKindsResponse(UniversalBaseModel):
    """
    已注册的服务商类型（provider kind）清单。
    """

    kinds: typing.List[str] = pydantic.Field()
    """
    服务商注册中心已注册的 kind（按字典序）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
