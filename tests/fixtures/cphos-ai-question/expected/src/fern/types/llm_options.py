

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_setting_spec import AppSettingSpec


class LlmOptions(UniversalBaseModel):
    """
    LLM / 应用设置的聚合元数据，驱动管理端表单按后端描述渲染。
    """

    provider_kinds: typing.List[str] = pydantic.Field()
    """
    已注册服务商类型清单。
    """

    agent_roles: typing.List[str] = pydantic.Field()
    """
    权威 Agent 角色清单。
    """

    app_settings: typing.List[AppSettingSpec] = pydantic.Field()
    """
    运行期应用设置项及其类型 / 约束。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
