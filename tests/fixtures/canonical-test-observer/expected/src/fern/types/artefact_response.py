

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artefact_status import ArtefactStatus
from .environment_response import EnvironmentResponse
from .reviewer_response import ReviewerResponse


class ArtefactResponse(UniversalBaseModel):
    id: int
    name: str
    version: str
    track: str
    store: str
    branch: str
    series: str
    repo: str
    source: str
    os: str
    release: str
    owner: str
    sha256: str
    image_url: str
    stage: str
    family: str
    status: ArtefactStatus
    comment: str
    attributes: typing.Dict[str, typing.Any]
    archived: bool
    reviewers: typing.List[ReviewerResponse]
    due_date: typing.Optional[dt.date] = None
    created_at: dt.datetime
    bug_link: str
    jira_issue: typing.Optional[str] = None
    all_environment_reviews_count: int
    completed_environment_reviews_count: int
    expected_environments: typing.List[EnvironmentResponse]
    missing_expected_environments: typing.List[EnvironmentResponse]
    assignee: typing.Optional[ReviewerResponse] = pydantic.Field(default=None)
    """
    Backward-compatible assignee field. Populated from the first entry in reviewers when present.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
