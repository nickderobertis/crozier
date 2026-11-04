

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts(UniversalBaseModel):
    """
    Test counts for a given pipeline number
    """

    error: int = pydantic.Field()
    """
    The number of tests with the error status
    """

    failure: int = pydantic.Field()
    """
    The number of tests with the failure status
    """

    skipped: int = pydantic.Field()
    """
    The number of tests with the skipped status
    """

    success: int = pydantic.Field()
    """
    The number of tests with the success status
    """

    total: int = pydantic.Field()
    """
    The total number of tests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
