

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_result_status import TestResultStatus


class TestResultRequest(UniversalBaseModel):
    name: str
    status: TestResultStatus
    template_id: typing.Optional[str] = None
    category: typing.Optional[str] = None
    comment: typing.Optional[str] = None
    io_log: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
