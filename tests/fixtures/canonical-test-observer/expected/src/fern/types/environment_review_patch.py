

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_build_environment_review_decision import ArtefactBuildEnvironmentReviewDecision


class EnvironmentReviewPatch(UniversalBaseModel):
    id: typing.Optional[int] = None
    review_decision: typing.Optional[typing.List[ArtefactBuildEnvironmentReviewDecision]] = None
    review_comment: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
