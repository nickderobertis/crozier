

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compliance_out import ComplianceOut
from .spec_out import SpecOut


class SpecResponse(UniversalBaseModel):
    compliance: ComplianceOut
    spec: SpecOut
    spec_markdown: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
