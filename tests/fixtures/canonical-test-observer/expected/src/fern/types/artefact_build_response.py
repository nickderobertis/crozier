

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_execution_response import TestExecutionResponse


class ArtefactBuildResponse(UniversalBaseModel):
    id: int
    architecture: str
    revision: typing.Optional[int] = None
    test_executions: typing.List[TestExecutionResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
