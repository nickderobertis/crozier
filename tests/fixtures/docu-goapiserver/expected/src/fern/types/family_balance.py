

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FamilyBalance(UniversalBaseModel):
    """
    A sparse row containing only the selected fields. Default fields: family_id, family_name, balance, transaction_date.
    """

    family_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family id.
    """

    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    School id.
    """

    family_name: typing.Optional[str] = None
    family_student_count: typing.Optional[int] = None
    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction id.
    """

    transaction_date: typing.Optional[dt.date] = None
    amount: typing.Optional[float] = None
    balance: typing.Optional[float] = None
    receipt_number: typing.Optional[str] = None
    kind: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
