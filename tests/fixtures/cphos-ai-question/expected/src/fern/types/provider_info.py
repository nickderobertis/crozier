

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProviderInfo(UniversalBaseModel):
    """
    服务商记录（api_key 已脱敏）。
    """

    id: str
    name: str
    kind: str
    base_url: typing.Optional[str] = None
    timeout: typing.Optional[int] = None
    max_retries: typing.Optional[int] = None
    api_key_set: bool = pydantic.Field()
    """
    是否已配置 API Key。
    """

    api_key_masked: typing.Optional[str] = pydantic.Field(default=None)
    """
    脱敏后的 Key 末尾提示。
    """

    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
