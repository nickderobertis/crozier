

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LastDataAccessTimes(UniversalBaseModel):
    """
    Describes the last time each datatype was accessed by an application.
    """

    account_balance_info: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time account_balance_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    account_routing_number: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time account_routing_number was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    application_id: str = pydantic.Field()
    """
    ID of the application accessing data.
    """

    contact_details: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time contact_details was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    credit_and_loans: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time credit_and_loans was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    investments: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time investments was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    payroll_info: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time payroll_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    transaction_risk_info: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time transaction_risk_info was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    transactions: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time transactions was accessed by this application in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format in UTC. null if never accessed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
