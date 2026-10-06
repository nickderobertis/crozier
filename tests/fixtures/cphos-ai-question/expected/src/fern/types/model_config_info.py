

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelConfigInfo(UniversalBaseModel):
    """
    模型配置记录。
    """

    id: str
    name: str
    provider_id: str
    model: typing.Optional[str] = None
    temperature: typing.Optional[float] = None
    max_tokens: typing.Optional[int] = None
    streaming: typing.Optional[bool] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
