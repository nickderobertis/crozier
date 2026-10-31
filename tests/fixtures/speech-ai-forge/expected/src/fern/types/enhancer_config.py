

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enhancer_config_solver import EnhancerConfigSolver


class EnhancerConfig(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    model: typing.Optional[str] = None
    nfe: typing.Optional[int] = None
    solver: typing.Optional[EnhancerConfigSolver] = None
    lambd: typing.Optional[float] = None
    tau: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
