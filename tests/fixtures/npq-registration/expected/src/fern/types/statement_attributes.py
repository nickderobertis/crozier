

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StatementAttributes(UniversalBaseModel):
    month: typing.Optional[str] = pydantic.Field(default=None)
    """
    The month which appears on the statement in the DfE portal.
    """

    year: typing.Optional[str] = pydantic.Field(default=None)
    """
    The calendar year which appears on the statement in the dfe portal.
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cohort - 2021 or 2022 - which the statement funds.
    """

    cut_off_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The milestone cut off or review point for the statement.
    """

    payment_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date we expect to pay you for any declarations attached to the statement, which are eligible for payment.
    """

    paid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the DfE has paid providers for any declarations attached to the statement.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the statement was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the statement was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
