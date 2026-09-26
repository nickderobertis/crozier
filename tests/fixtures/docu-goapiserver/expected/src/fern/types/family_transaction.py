

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FamilyTransaction(UniversalBaseModel):
    """
    Family Transaction.
    """

    id: str
    date: dt.datetime
    student_id: typing.Optional[str] = None
    type: str
    description: str
    status: str
    amount: float
    balance: float
    service_start: typing.Optional[dt.datetime] = None
    service_end: typing.Optional[dt.datetime] = None
    sub_type: typing.Optional[str] = None
    receipt_number: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
