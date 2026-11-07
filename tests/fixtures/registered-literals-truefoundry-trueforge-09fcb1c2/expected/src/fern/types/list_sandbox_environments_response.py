

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_environment import SandboxEnvironment
from .token_pagination import TokenPagination


class ListSandboxEnvironmentsResponse(UniversalBaseModel):
    data: typing.List[SandboxEnvironment]
    pagination: TokenPagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
