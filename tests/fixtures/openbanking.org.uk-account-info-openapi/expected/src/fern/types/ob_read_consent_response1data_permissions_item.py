

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadConsentResponse1DataPermissionsItem(enum.StrEnum):
    """
    Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.
    """

    READ_ACCOUNTS_BASIC = "ReadAccountsBasic"
    READ_ACCOUNTS_DETAIL = "ReadAccountsDetail"
    READ_BALANCES = "ReadBalances"
    READ_BENEFICIARIES_BASIC = "ReadBeneficiariesBasic"
    READ_BENEFICIARIES_DETAIL = "ReadBeneficiariesDetail"
    READ_DIRECT_DEBITS = "ReadDirectDebits"
    READ_OFFERS = "ReadOffers"
    READ_PAN = "ReadPAN"
    READ_PARTY = "ReadParty"
    READ_PARTY_PSU = "ReadPartyPSU"
    READ_PRODUCTS = "ReadProducts"
    READ_SCHEDULED_PAYMENTS_BASIC = "ReadScheduledPaymentsBasic"
    READ_SCHEDULED_PAYMENTS_DETAIL = "ReadScheduledPaymentsDetail"
    READ_STANDING_ORDERS_BASIC = "ReadStandingOrdersBasic"
    READ_STANDING_ORDERS_DETAIL = "ReadStandingOrdersDetail"
    READ_STATEMENTS_BASIC = "ReadStatementsBasic"
    READ_STATEMENTS_DETAIL = "ReadStatementsDetail"
    READ_TRANSACTIONS_BASIC = "ReadTransactionsBasic"
    READ_TRANSACTIONS_CREDITS = "ReadTransactionsCredits"
    READ_TRANSACTIONS_DEBITS = "ReadTransactionsDebits"
    READ_TRANSACTIONS_DETAIL = "ReadTransactionsDetail"

    def visit(
        self,
        read_accounts_basic: typing.Callable[[], T_Result],
        read_accounts_detail: typing.Callable[[], T_Result],
        read_balances: typing.Callable[[], T_Result],
        read_beneficiaries_basic: typing.Callable[[], T_Result],
        read_beneficiaries_detail: typing.Callable[[], T_Result],
        read_direct_debits: typing.Callable[[], T_Result],
        read_offers: typing.Callable[[], T_Result],
        read_pan: typing.Callable[[], T_Result],
        read_party: typing.Callable[[], T_Result],
        read_party_psu: typing.Callable[[], T_Result],
        read_products: typing.Callable[[], T_Result],
        read_scheduled_payments_basic: typing.Callable[[], T_Result],
        read_scheduled_payments_detail: typing.Callable[[], T_Result],
        read_standing_orders_basic: typing.Callable[[], T_Result],
        read_standing_orders_detail: typing.Callable[[], T_Result],
        read_statements_basic: typing.Callable[[], T_Result],
        read_statements_detail: typing.Callable[[], T_Result],
        read_transactions_basic: typing.Callable[[], T_Result],
        read_transactions_credits: typing.Callable[[], T_Result],
        read_transactions_debits: typing.Callable[[], T_Result],
        read_transactions_detail: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadConsentResponse1DataPermissionsItem.READ_ACCOUNTS_BASIC:
            return read_accounts_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_ACCOUNTS_DETAIL:
            return read_accounts_detail()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_BALANCES:
            return read_balances()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_BENEFICIARIES_BASIC:
            return read_beneficiaries_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_BENEFICIARIES_DETAIL:
            return read_beneficiaries_detail()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_DIRECT_DEBITS:
            return read_direct_debits()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_OFFERS:
            return read_offers()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_PAN:
            return read_pan()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_PARTY:
            return read_party()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_PARTY_PSU:
            return read_party_psu()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_PRODUCTS:
            return read_products()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_SCHEDULED_PAYMENTS_BASIC:
            return read_scheduled_payments_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_SCHEDULED_PAYMENTS_DETAIL:
            return read_scheduled_payments_detail()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_STANDING_ORDERS_BASIC:
            return read_standing_orders_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_STANDING_ORDERS_DETAIL:
            return read_standing_orders_detail()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_STATEMENTS_BASIC:
            return read_statements_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_STATEMENTS_DETAIL:
            return read_statements_detail()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_TRANSACTIONS_BASIC:
            return read_transactions_basic()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_TRANSACTIONS_CREDITS:
            return read_transactions_credits()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_TRANSACTIONS_DEBITS:
            return read_transactions_debits()
        if self is ObReadConsentResponse1DataPermissionsItem.READ_TRANSACTIONS_DETAIL:
            return read_transactions_detail()
