

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .billable_owner_type import BillableOwnerType


class BillableOwnerBody(UniversalBaseModel):
    id: typing.Optional[str] = None
    login: typing.Optional[str] = None
    type: typing.Optional[BillableOwnerType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
