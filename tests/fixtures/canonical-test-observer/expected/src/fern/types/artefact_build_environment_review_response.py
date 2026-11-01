

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_build_environment_review_decision import ArtefactBuildEnvironmentReviewDecision
from .artefact_build_minimal_response import ArtefactBuildMinimalResponse
from .environment_response import EnvironmentResponse
from .reviewer_response import ReviewerResponse


class ArtefactBuildEnvironmentReviewResponse(UniversalBaseModel):
    id: int
    review_decision: typing.List[ArtefactBuildEnvironmentReviewDecision]
    review_comment: str
    environment: EnvironmentResponse
    artefact_build: ArtefactBuildMinimalResponse
    reviewers: typing.Optional[typing.List[ReviewerResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
