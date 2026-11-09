

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SecurityOverride(UniversalBaseModel):
    """
    Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Either a valid `iso_currency_code` or `unofficial_currency_code`
    """

    cusip: typing.Optional[str] = pydantic.Field(default=None)
    """
    9-character CUSIP, an identifier assigned to North American securities. Please note that Plaid's customers must hold a license directly from CUSIP Global Services to receive CUSIP & ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com.
    """

    isin: typing.Optional[str] = pydantic.Field(default=None)
    """
    12-character ISIN, a globally unique securities identifier. Please note that Plaid's customers must hold a license directly from CUSIP Global Services to receive CUSIP & ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A descriptive name for the security, suitable for display.
    """

    sedol: typing.Optional[str] = pydantic.Field(default=None)
    """
    7-character SEDOL, an identifier assigned to securities in the UK.
    """

    ticker_symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
