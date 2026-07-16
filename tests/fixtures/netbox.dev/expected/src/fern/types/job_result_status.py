

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_result_status_label import JobResultStatusLabel
from .job_result_status_value import JobResultStatusValue


class JobResultStatus(UniversalBaseModel):
    label: JobResultStatusLabel
    value: JobResultStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
