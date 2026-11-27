

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .field_create import FieldCreate
from .field_summary import FieldSummary


class FieldDefinition(FieldCreate, FieldSummary):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
