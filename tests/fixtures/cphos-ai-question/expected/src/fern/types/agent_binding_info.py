

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentBindingInfo(UniversalBaseModel):
    """
    Agent 角色到模型配置的绑定。
    """

    role: str = pydantic.Field()
    """
    Agent 角色名。
    """

    model_config_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    绑定的模型配置 ID；未绑定为 null。
    """

    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
