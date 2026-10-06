

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .component_health import ComponentHealth
from .health_status_status import HealthStatusStatus


class HealthStatus(UniversalBaseModel):
    """
    服务整体与组件级健康信息。
    """

    status: HealthStatusStatus = pydantic.Field()
    """
    整体状态：所有组件正常为 ok，任一组件异常为 degraded。
    """

    components: typing.Optional[typing.Dict[str, ComponentHealth]] = pydantic.Field(default=None)
    """
    组件级健康明细（如 db / worker）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
