

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .c3test_result_status import C3TestResultStatus


class C3TestResult(UniversalBaseModel):
    name: str
    template_id: typing.Optional[str] = None
    status: C3TestResultStatus
    category: str
    comment: str
    io_log: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
