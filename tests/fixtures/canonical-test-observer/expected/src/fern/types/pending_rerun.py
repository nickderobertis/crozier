

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_build_minimal_response import ArtefactBuildMinimalResponse
from .artefact_response import ArtefactResponse
from .family_name import FamilyName
from .test_execution_response import TestExecutionResponse


class PendingRerun(UniversalBaseModel):
    test_execution_id: int
    ci_link: typing.Optional[str] = None
    family: FamilyName
    test_execution: TestExecutionResponse
    artefact: ArtefactResponse
    artefact_build: ArtefactBuildMinimalResponse
    priority: int
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
