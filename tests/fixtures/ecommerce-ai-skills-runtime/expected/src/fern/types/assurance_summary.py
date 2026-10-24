

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssuranceSummary(UniversalBaseModel):
    check_count: typing.Optional[int] = None
    passed_count: typing.Optional[int] = None
    backup_id: typing.Optional[str] = None
    evidence_object_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
