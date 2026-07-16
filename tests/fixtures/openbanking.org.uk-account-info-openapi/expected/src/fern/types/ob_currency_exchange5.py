

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_currency_exchange5instructed_amount import ObCurrencyExchange5InstructedAmount


class ObCurrencyExchange5(UniversalBaseModel):
    """
    Set of elements used to provide details on the currency exchange.
    """

    contract_identification: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ContractIdentification")
    ] = pydantic.Field(default=None)
    """
    Unique identification to unambiguously identify the foreign exchange contract.
    """

    exchange_rate: typing_extensions.Annotated[float, FieldMetadata(alias="ExchangeRate")] = pydantic.Field()
    """
    Factor used to convert an amount from one currency into another. This reflects the price at which one currency was bought with another currency.
    Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency).
    """

    instructed_amount: typing_extensions.Annotated[
        typing.Optional[ObCurrencyExchange5InstructedAmount], FieldMetadata(alias="InstructedAmount")
    ] = pydantic.Field(default=None)
    """
    Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.
    """

    quotation_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="QuotationDate")] = (
        pydantic.Field(default=None)
    )
    """
    Date and time at which an exchange rate is quoted.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    source_currency: typing_extensions.Annotated[str, FieldMetadata(alias="SourceCurrency")] = pydantic.Field()
    """
    Currency from which an amount is to be converted in a currency conversion.
    """

    target_currency: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TargetCurrency")] = (
        pydantic.Field(default=None)
    )
    """
    Currency into which an amount is to be converted in a currency conversion.
    """

    unit_currency: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UnitCurrency")] = (
        pydantic.Field(default=None)
    )
    """
    Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
