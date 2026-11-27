

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assembly_validation_status_type import AssemblyValidationStatusType


class AssemblyValidationStatus(UniversalBaseModel):
    message: typing.Optional[str] = None
    type: typing.Optional[AssemblyValidationStatusType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
