

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .execution_metadata import ExecutionMetadata
from .family_name import FamilyName
from .test_execution_rerun_filters_assignee_ids import TestExecutionRerunFiltersAssigneeIds
from .test_execution_rerun_filters_reviewer_ids import TestExecutionRerunFiltersReviewerIds
from .test_execution_status import TestExecutionStatus


class TestExecutionRerunFilters(UniversalBaseModel):
    """
    Filter model for rerun create/delete operations.

    Excludes pagination (limit/offset) and search-only fields (event_names)
    that have no meaning in the rerun context.
    """

    families: typing.Optional[typing.List[FamilyName]] = None
    artefacts: typing.Optional[typing.List[str]] = None
    artefact_versions: typing.Optional[typing.List[str]] = None
    artefact_stages: typing.Optional[typing.List[str]] = None
    artefact_tracks: typing.Optional[typing.List[str]] = None
    artefact_is_archived: typing.Optional[bool] = None
    environments: typing.Optional[typing.List[str]] = None
    test_plans: typing.Optional[typing.List[str]] = None
    test_execution_statuses: typing.Optional[typing.List[TestExecutionStatus]] = None
    execution_metadata: typing.Optional[ExecutionMetadata] = None
    reviewer_ids: typing.Optional[TestExecutionRerunFiltersReviewerIds] = None
    assignee_ids: typing.Optional[TestExecutionRerunFiltersAssigneeIds] = None
    rerun_is_requested: typing.Optional[bool] = None
    execution_is_latest: typing.Optional[bool] = None
    from_date: typing.Optional[dt.datetime] = None
    until_date: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
