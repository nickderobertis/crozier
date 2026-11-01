

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_result_search_filters import TestResultSearchFilters


class IssueAttachmentRequest(UniversalBaseModel):
    test_results: typing.Optional[typing.List[int]] = None
    test_results_filters: typing.Optional[TestResultSearchFilters] = None
    attachment_rule: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
