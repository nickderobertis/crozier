

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SignalEvaluateCoreAttributes(UniversalBaseModel):
    """
    The core attributes object contains additional data that can be used to assess the ACH return risk. Examples of data include:

    `days_since_first_plaid_connection`: The number of days since the first time the Item was connected to an application via Plaid
    `plaid_connections_count_7d`: The number of times the Item has been connected to applications via Plaid over the past 7 days
    `plaid_connections_count_30d`: The number of times the Item has been connected to applications via Plaid over the past 30 days
    `total_plaid_connections_count`: The number of times the Item has been connected to applications via Plaid
    `is_savings_or_money_market_account`: Indicates whether the ACH transaction funding account is a savings/money market account

    For the full list and detailed documentation of core attributes available, or to request that core attributes not be returned, contact Sales or your Plaid account manager
    """

    address_change_count28d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="address_change_count_28d"),
        pydantic.Field(
            alias="address_change_count_28d",
            description="The number of times the account's addresses on file have changed over the past 28 days",
        ),
    ] = None
    """
    The number of times the account's addresses on file have changed over the past 28 days
    """

    address_change_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="address_change_count_90d"),
        pydantic.Field(
            alias="address_change_count_90d",
            description="The number of times the account's addresses on file have changed over the past 90 days",
        ),
    ] = None
    """
    The number of times the account's addresses on file have changed over the past 90 days
    """

    available_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Available balance, as of the `balance_last_updated` time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.
    """

    balance_last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated.
    """

    credit_transactions_count10d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="credit_transactions_count_10d"),
        pydantic.Field(
            alias="credit_transactions_count_10d",
            description="The total number of credit (inflow) transactions over the past 10 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of credit (inflow) transactions over the past 10 days from the account that will be debited
    """

    credit_transactions_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="credit_transactions_count_30d"),
        pydantic.Field(
            alias="credit_transactions_count_30d",
            description="The total number of credit (inflow) transactions over the past 30 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of credit (inflow) transactions over the past 30 days from the account that will be debited
    """

    credit_transactions_count60d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="credit_transactions_count_60d"),
        pydantic.Field(
            alias="credit_transactions_count_60d",
            description="The total number of credit (inflow) transactions over the past 60 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of credit (inflow) transactions over the past 60 days from the account that will be debited
    """

    credit_transactions_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="credit_transactions_count_90d"),
        pydantic.Field(
            alias="credit_transactions_count_90d",
            description="The total number of credit (inflow) transactions over the past 90 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of credit (inflow) transactions over the past 90 days from the account that will be debited
    """

    current_balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current balance, as of the `balance_last_updated` time. The current balance is the total amount of funds in the account.
    """

    days_since_first_plaid_connection: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of days since the first time the Item was connected to an application via Plaid
    """

    days_with_negative_balance_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="days_with_negative_balance_count_90d"),
        pydantic.Field(
            alias="days_with_negative_balance_count_90d",
            description="The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance",
        ),
    ] = None
    """
    The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance
    """

    debit_transactions_count10d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="debit_transactions_count_10d"),
        pydantic.Field(
            alias="debit_transactions_count_10d",
            description="The total number of debit (outflow) transactions over the past 10 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of debit (outflow) transactions over the past 10 days from the account that will be debited
    """

    debit_transactions_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="debit_transactions_count_30d"),
        pydantic.Field(
            alias="debit_transactions_count_30d",
            description="The total number of debit (outflow) transactions over the past 30 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of debit (outflow) transactions over the past 30 days from the account that will be debited
    """

    debit_transactions_count60d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="debit_transactions_count_60d"),
        pydantic.Field(
            alias="debit_transactions_count_60d",
            description="The total number of debit (outflow) transactions over the past 60 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of debit (outflow) transactions over the past 60 days from the account that will be debited
    """

    debit_transactions_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="debit_transactions_count_90d"),
        pydantic.Field(
            alias="debit_transactions_count_90d",
            description="The total number of debit (outflow) transactions over the past 90 days from the account that will be debited",
        ),
    ] = None
    """
    The total number of debit (outflow) transactions over the past 90 days from the account that will be debited
    """

    email_change_count28d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="email_change_count_28d"),
        pydantic.Field(
            alias="email_change_count_28d",
            description="The number of times the account's email addresses on file have changed over the past 28 days",
        ),
    ] = None
    """
    The number of times the account's email addresses on file have changed over the past 28 days
    """

    email_change_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="email_change_count_90d"),
        pydantic.Field(
            alias="email_change_count_90d",
            description="The number of times the account's email addresses on file have changed over the past 90 days",
        ),
    ] = None
    """
    The number of times the account's email addresses on file have changed over the past 90 days
    """

    failed_plaid_non_oauth_authentication_attempts_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="failed_plaid_non_oauth_authentication_attempts_count_30d"),
        pydantic.Field(
            alias="failed_plaid_non_oauth_authentication_attempts_count_30d",
            description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days",
        ),
    ] = None
    """
    The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
    """

    failed_plaid_non_oauth_authentication_attempts_count3d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="failed_plaid_non_oauth_authentication_attempts_count_3d"),
        pydantic.Field(
            alias="failed_plaid_non_oauth_authentication_attempts_count_3d",
            description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days",
        ),
    ] = None
    """
    The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
    """

    failed_plaid_non_oauth_authentication_attempts_count7d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="failed_plaid_non_oauth_authentication_attempts_count_7d"),
        pydantic.Field(
            alias="failed_plaid_non_oauth_authentication_attempts_count_7d",
            description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days",
        ),
    ] = None
    """
    The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
    """

    is_savings_or_money_market_account: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the ACH transaction funding account is a savings/money market account
    """

    nsf_overdraft_transactions_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nsf_overdraft_transactions_count_30d"),
        pydantic.Field(
            alias="nsf_overdraft_transactions_count_30d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited.
    """

    nsf_overdraft_transactions_count60d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nsf_overdraft_transactions_count_60d"),
        pydantic.Field(
            alias="nsf_overdraft_transactions_count_60d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited.
    """

    nsf_overdraft_transactions_count7d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nsf_overdraft_transactions_count_7d"),
        pydantic.Field(
            alias="nsf_overdraft_transactions_count_7d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited.
    """

    nsf_overdraft_transactions_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nsf_overdraft_transactions_count_90d"),
        pydantic.Field(
            alias="nsf_overdraft_transactions_count_90d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited.
    """

    p10eod_balance30d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p10_eod_balance_30d"),
        pydantic.Field(
            alias="p10_eod_balance_30d",
            description="The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited",
        ),
    ] = None
    """
    The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited
    """

    p10eod_balance31d_to60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p10_eod_balance_31d_to_60d"),
        pydantic.Field(
            alias="p10_eod_balance_31d_to_60d",
            description="The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited
    """

    p10eod_balance60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p10_eod_balance_60d"),
        pydantic.Field(
            alias="p10_eod_balance_60d",
            description="The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited
    """

    p10eod_balance61d_to90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p10_eod_balance_61d_to_90d"),
        pydantic.Field(
            alias="p10_eod_balance_61d_to_90d",
            description="The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited
    """

    p10eod_balance90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p10_eod_balance_90d"),
        pydantic.Field(
            alias="p10_eod_balance_90d",
            description="The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited",
        ),
    ] = None
    """
    The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited
    """

    p50credit_transactions_amount28d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_credit_transactions_amount_28d"),
        pydantic.Field(
            alias="p50_credit_transactions_amount_28d",
            description="The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited
    """

    p50debit_transactions_amount28d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_debit_transactions_amount_28d"),
        pydantic.Field(
            alias="p50_debit_transactions_amount_28d",
            description="The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited
    """

    p50eod_balance30d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_eod_balance_30d"),
        pydantic.Field(
            alias="p50_eod_balance_30d",
            description="The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be debited
    """

    p50eod_balance31d_to60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_eod_balance_31d_to_60d"),
        pydantic.Field(
            alias="p50_eod_balance_31d_to_60d",
            description="The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited
    """

    p50eod_balance60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_eod_balance_60d"),
        pydantic.Field(
            alias="p50_eod_balance_60d",
            description="The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be debited
    """

    p50eod_balance61d_to90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_eod_balance_61d_to_90d"),
        pydantic.Field(
            alias="p50_eod_balance_61d_to_90d",
            description="The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited
    """

    p50eod_balance90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p50_eod_balance_90d"),
        pydantic.Field(
            alias="p50_eod_balance_90d",
            description="The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be debited",
        ),
    ] = None
    """
    The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be debited
    """

    p90eod_balance30d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p90_eod_balance_30d"),
        pydantic.Field(
            alias="p90_eod_balance_30d",
            description="The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited",
        ),
    ] = None
    """
    The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited
    """

    p90eod_balance31d_to60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p90_eod_balance_31d_to_60d"),
        pydantic.Field(
            alias="p90_eod_balance_31d_to_60d",
            description="The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited
    """

    p90eod_balance60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p90_eod_balance_60d"),
        pydantic.Field(
            alias="p90_eod_balance_60d",
            description="The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited
    """

    p90eod_balance61d_to90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p90_eod_balance_61d_to_90d"),
        pydantic.Field(
            alias="p90_eod_balance_61d_to_90d",
            description="The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited",
        ),
    ] = None
    """
    The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited
    """

    p90eod_balance90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p90_eod_balance_90d"),
        pydantic.Field(
            alias="p90_eod_balance_90d",
            description="The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited",
        ),
    ] = None
    """
    The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited
    """

    p95credit_transactions_amount28d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p95_credit_transactions_amount_28d"),
        pydantic.Field(
            alias="p95_credit_transactions_amount_28d",
            description="The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited",
        ),
    ] = None
    """
    The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited
    """

    p95debit_transactions_amount28d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p95_debit_transactions_amount_28d"),
        pydantic.Field(
            alias="p95_debit_transactions_amount_28d",
            description="The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited",
        ),
    ] = None
    """
    The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited
    """

    phone_change_count28d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="phone_change_count_28d"),
        pydantic.Field(
            alias="phone_change_count_28d",
            description="The number of times the account's phone numbers on file have changed over the past 28 days",
        ),
    ] = None
    """
    The number of times the account's phone numbers on file have changed over the past 28 days
    """

    phone_change_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="phone_change_count_90d"),
        pydantic.Field(
            alias="phone_change_count_90d",
            description="The number of times the account's phone numbers on file have changed over the past 90 days",
        ),
    ] = None
    """
    The number of times the account's phone numbers on file have changed over the past 90 days
    """

    plaid_connections_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plaid_connections_count_30d"),
        pydantic.Field(
            alias="plaid_connections_count_30d",
            description="The number of times the Item has been connected to applications via Plaid over the past 30 days",
        ),
    ] = None
    """
    The number of times the Item has been connected to applications via Plaid over the past 30 days
    """

    plaid_connections_count7d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plaid_connections_count_7d"),
        pydantic.Field(
            alias="plaid_connections_count_7d",
            description="The number of times the Item has been connected to applications via Plaid over the past 7 days",
        ),
    ] = None
    """
    The number of times the Item has been connected to applications via Plaid over the past 7 days
    """

    plaid_non_oauth_authentication_attempts_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plaid_non_oauth_authentication_attempts_count_30d"),
        pydantic.Field(
            alias="plaid_non_oauth_authentication_attempts_count_30d",
            description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days",
        ),
    ] = None
    """
    The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days
    """

    plaid_non_oauth_authentication_attempts_count3d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plaid_non_oauth_authentication_attempts_count_3d"),
        pydantic.Field(
            alias="plaid_non_oauth_authentication_attempts_count_3d",
            description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days",
        ),
    ] = None
    """
    The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days
    """

    plaid_non_oauth_authentication_attempts_count7d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plaid_non_oauth_authentication_attempts_count_7d"),
        pydantic.Field(
            alias="plaid_non_oauth_authentication_attempts_count_7d",
            description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days",
        ),
    ] = None
    """
    The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days
    """

    total_credit_transactions_amount10d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_credit_transactions_amount_10d"),
        pydantic.Field(
            alias="total_credit_transactions_amount_10d",
            description="The total credit (inflow) transaction amount over the past 10 days from the account that will be debited",
        ),
    ] = None
    """
    The total credit (inflow) transaction amount over the past 10 days from the account that will be debited
    """

    total_credit_transactions_amount30d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_credit_transactions_amount_30d"),
        pydantic.Field(
            alias="total_credit_transactions_amount_30d",
            description="The total credit (inflow) transaction amount over the past 30 days from the account that will be debited",
        ),
    ] = None
    """
    The total credit (inflow) transaction amount over the past 30 days from the account that will be debited
    """

    total_credit_transactions_amount60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_credit_transactions_amount_60d"),
        pydantic.Field(
            alias="total_credit_transactions_amount_60d",
            description="The total credit (inflow) transaction amount over the past 60 days from the account that will be debited",
        ),
    ] = None
    """
    The total credit (inflow) transaction amount over the past 60 days from the account that will be debited
    """

    total_credit_transactions_amount90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_credit_transactions_amount_90d"),
        pydantic.Field(
            alias="total_credit_transactions_amount_90d",
            description="The total credit (inflow) transaction amount over the past 90 days from the account that will be debited",
        ),
    ] = None
    """
    The total credit (inflow) transaction amount over the past 90 days from the account that will be debited
    """

    total_debit_transactions_amount10d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_debit_transactions_amount_10d"),
        pydantic.Field(
            alias="total_debit_transactions_amount_10d",
            description="The total debit (outflow) transaction amount over the past 10 days from the account that will be debited",
        ),
    ] = None
    """
    The total debit (outflow) transaction amount over the past 10 days from the account that will be debited
    """

    total_debit_transactions_amount30d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_debit_transactions_amount_30d"),
        pydantic.Field(
            alias="total_debit_transactions_amount_30d",
            description="The total debit (outflow) transaction amount over the past 30 days from the account that will be debited",
        ),
    ] = None
    """
    The total debit (outflow) transaction amount over the past 30 days from the account that will be debited
    """

    total_debit_transactions_amount60d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_debit_transactions_amount_60d"),
        pydantic.Field(
            alias="total_debit_transactions_amount_60d",
            description="The total debit (outflow) transaction amount over the past 60 days from the account that will be debited",
        ),
    ] = None
    """
    The total debit (outflow) transaction amount over the past 60 days from the account that will be debited
    """

    total_debit_transactions_amount90d: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="total_debit_transactions_amount_90d"),
        pydantic.Field(
            alias="total_debit_transactions_amount_90d",
            description="The total debit (outflow) transaction amount over the past 90 days from the account that will be debited",
        ),
    ] = None
    """
    The total debit (outflow) transaction amount over the past 90 days from the account that will be debited
    """

    total_plaid_connections_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of times the Item has been connected to applications via Plaid
    """

    transactions_last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the transactions for the given account have been updated.
    """

    unauthorized_transactions_count30d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unauthorized_transactions_count_30d"),
        pydantic.Field(
            alias="unauthorized_transactions_count_30d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited.
    """

    unauthorized_transactions_count60d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unauthorized_transactions_count_60d"),
        pydantic.Field(
            alias="unauthorized_transactions_count_60d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited.
    """

    unauthorized_transactions_count7d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unauthorized_transactions_count_7d"),
        pydantic.Field(
            alias="unauthorized_transactions_count_7d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited.
    """

    unauthorized_transactions_count90d: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unauthorized_transactions_count_90d"),
        pydantic.Field(
            alias="unauthorized_transactions_count_90d",
            description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited.",
        ),
    ] = None
    """
    We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
