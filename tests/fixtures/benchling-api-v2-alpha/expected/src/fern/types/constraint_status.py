

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .constraint_status_status import ConstraintStatusStatus
from .field_definition import FieldDefinition


class ConstraintStatus(UniversalBaseModel):
    fields: typing.Optional[typing.List[FieldDefinition]] = None
    status: typing.Optional[ConstraintStatusStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
