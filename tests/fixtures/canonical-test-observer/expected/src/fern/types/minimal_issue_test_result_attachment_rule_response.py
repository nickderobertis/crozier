

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .execution_metadata import ExecutionMetadata
from .family_name import FamilyName
from .test_result_status import TestResultStatus


class MinimalIssueTestResultAttachmentRuleResponse(UniversalBaseModel):
    id: int
    enabled: bool
    families: typing.List[FamilyName]
    artefacts: typing.List[str]
    artefact_versions: typing.List[str]
    artefact_stages: typing.List[str]
    artefact_tracks: typing.List[str]
    environment_names: typing.List[str]
    test_plans: typing.List[str]
    test_case_names: typing.List[str]
    template_ids: typing.List[str]
    test_result_statuses: typing.List[TestResultStatus]
    execution_metadata: ExecutionMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
