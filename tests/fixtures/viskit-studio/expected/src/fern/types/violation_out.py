

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .violation_out_severity import ViolationOutSeverity


class ViolationOut(UniversalBaseModel):
    location: str
    matched_text: str
    rule_id: str
    severity: ViolationOutSeverity
    suggestion: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
