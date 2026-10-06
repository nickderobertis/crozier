

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .component_health_status import ComponentHealthStatus


class ComponentHealth(UniversalBaseModel):
    """
    单个组件的健康状态。
    """

    status: ComponentHealthStatus = pydantic.Field()
    """
    组件健康状态。
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    异常时的简要说明（健康时为空）。
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
