

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assurance_check_status import AssuranceCheckStatus


class AssuranceCheck(UniversalBaseModel):
    name: str
    status: AssuranceCheckStatus
    code: str
    count: typing.Optional[int] = None
    error_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
