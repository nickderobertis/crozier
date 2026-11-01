

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WptRunMetric(UniversalBaseModel):
    run_timestamp: dt.datetime = pydantic.Field()
    """
    The start timestamp of the run.
    """

    total_tests_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of tests
    """

    test_pass_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of passing tests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
