

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_check_result_comparator import LoadCheckResultComparator
from .load_check_result_source import LoadCheckResultSource


class LoadCheckResult(UniversalBaseModel):
    """
    the aggregate pass/fail counts for one distinct per-step check across a load run
    """

    step: typing.Optional[str] = pydantic.Field(default=None)
    """
    the step label (step name or index) the check ran on
    """

    source: typing.Optional[LoadCheckResultSource] = None
    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    the header name (HEADER) or JSONPath (BODY_JSONPATH); absent for STATUS
    """

    comparator: typing.Optional[LoadCheckResultComparator] = None
    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    the expected comparand value
    """

    passed: typing.Optional[int] = None
    failed: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
