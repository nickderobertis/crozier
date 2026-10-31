

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .execution_metadata import ExecutionMetadata
from .family_name import FamilyName
from .test_execution_status import TestExecutionStatus
from .test_result_search_filters_assignee_ids import TestResultSearchFiltersAssigneeIds
from .test_result_search_filters_issues import TestResultSearchFiltersIssues
from .test_result_search_filters_reviewer_ids import TestResultSearchFiltersReviewerIds
from .test_result_status import TestResultStatus


class TestResultSearchFilters(UniversalBaseModel):
    families: typing.Optional[typing.List[FamilyName]] = None
    artefacts: typing.Optional[typing.List[str]] = None
    artefact_versions: typing.Optional[typing.List[str]] = None
    artefact_stages: typing.Optional[typing.List[str]] = None
    artefact_tracks: typing.Optional[typing.List[str]] = None
    artefact_is_archived: typing.Optional[bool] = None
    environments: typing.Optional[typing.List[str]] = None
    test_cases: typing.Optional[typing.List[str]] = None
    template_ids: typing.Optional[typing.List[str]] = None
    test_plans: typing.Optional[typing.List[str]] = None
    execution_metadata: typing.Optional[ExecutionMetadata] = None
    issues: typing.Optional[TestResultSearchFiltersIssues] = None
    test_result_statuses: typing.Optional[typing.List[TestResultStatus]] = None
    test_execution_statuses: typing.Optional[typing.List[TestExecutionStatus]] = None
    reviewer_ids: typing.Optional[TestResultSearchFiltersReviewerIds] = None
    assignee_ids: typing.Optional[TestResultSearchFiltersAssigneeIds] = None
    rerun_is_requested: typing.Optional[bool] = None
    execution_is_latest: typing.Optional[bool] = None
    from_date: typing.Optional[dt.datetime] = None
    until_date: typing.Optional[dt.datetime] = None
    offset: typing.Optional[int] = None
    limit: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
