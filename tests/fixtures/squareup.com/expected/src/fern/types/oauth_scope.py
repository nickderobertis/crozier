

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    APPOINTMENTS_BUSINESS_SETTINGS_READ = "APPOINTMENTS_BUSINESS_SETTINGS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to booking business settings. For example, to call the
    ListTeamMemberBookingProfiles endpoint.
    """

    APPOINTMENTS_READ = "APPOINTMENTS_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Grants read access to booking information. For example, to call the
    RetrieveBooking endpoint.
    """

    APPOINTMENTS_WRITE = "APPOINTMENTS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to booking information. For example, to call the CreateBooking endpoint.
    """

    BANK_ACCOUNTS_READ = "BANK_ACCOUNTS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to bank account information associated with the targeted
    Square account. For example, to call the Connect v1 ListBankAccounts endpoint.
    """

    CASH_DRAWER_READ = "CASH_DRAWER_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to cash drawer shift information. For example, to call the
    ListCashDrawerShifts endpoint.
    """

    CUSTOMERS_READ = "CUSTOMERS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to customer information. For example, to call the
    ListCustomers endpoint.
    """

    CUSTOMERS_WRITE = "CUSTOMERS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to customer information. For example, to create and update
    customer profiles.
    """

    DEVICE_CREDENTIAL_MANAGEMENT = "DEVICE_CREDENTIAL_MANAGEMENT"
    """
    __HTTP Method__: `POST`, `GET`
    
    Grants read/write access to device credentials information. For example, to
    call the CreateDeviceCode endpoint.
    """

    DISPUTES_READ = "DISPUTES_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to dispute information. For example, to call the RetrieveDispute
    endpoint.
    """

    DISPUTES_WRITE = "DISPUTES_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to dispute information. For example, to call the SubmitEvidence
    endpoint.
    """

    EMPLOYEES_READ = "EMPLOYEES_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to employee profile information. For example, to call the
    Connect v1 Employees API.
    """

    EMPLOYEES_WRITE = "EMPLOYEES_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to employee profile information. For example, to create
    and modify employee profiles.
    """

    GIFTCARDS_READ = "GIFTCARDS_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Grants read access to gift card information. For example, to call the RetrieveGiftCard
    endpoint.
    """

    GIFTCARDS_WRITE = "GIFTCARDS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to gift card information. For example, to call the CreateGiftCard
    endpoint.
    """

    INVENTORY_READ = "INVENTORY_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to inventory information. For example, to call the
    RetrieveInventoryCount endpoint.
    """

    INVENTORY_WRITE = "INVENTORY_WRITE"
    """
    __HTTP Method__:  `POST`, `PUT`, `DELETE`
    
    Grants write access to inventory information. For example, to call the
    BatchChangeInventory endpoint.
    """

    INVOICES_READ = "INVOICES_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Grants read access to invoice information. For example, to call the ListInvoices endpoint.
    """

    INVOICES_WRITE = "INVOICES_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to invoice information. For example, to call the CreateInvoice endpoint.
    """

    ITEMS_READ = "ITEMS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to business and location information. For example, to
    obtain a location ID for subsequent activity.
    """

    ITEMS_WRITE = "ITEMS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to product catalog information. For example, to modify or
    add to a product catalog.
    """

    LOYALTY_READ = "LOYALTY_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to loyalty information. For example, to call the
    ListLoyaltyPrograms endpoint.
    """

    LOYALTY_WRITE = "LOYALTY_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to loyalty information. For example, to call the
    CreateLoyaltyAccount endpoint.
    """

    MERCHANT_PROFILE_READ = "MERCHANT_PROFILE_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to business and location information. For example, to
    obtain a location ID for subsequent activity.
    """

    MERCHANT_PROFILE_WRITE = "MERCHANT_PROFILE_WRITE"
    """
    *Originally missing*
    """

    ONLINE_STORE_SITE_READ = "ONLINE_STORE_SITE_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Read access to ECOM online store site details.
    """

    ONLINE_STORE_SNIPPETS_READ = "ONLINE_STORE_SNIPPETS_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Read access to ECOM online store snippets on published websites.
    """

    ONLINE_STORE_SNIPPETS_WRITE = "ONLINE_STORE_SNIPPETS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Write access to ECOM online store snippets on published websites.
    """

    ORDERS_READ = "ORDERS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to order information. For example, to call the
    BatchRetrieveOrders endpoint.
    """

    ORDERS_WRITE = "ORDERS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to order information. For example, to call the
    CreateCheckout endpoint.
    """

    PAYMENTS_READ = "PAYMENTS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to transaction and refund information. For example, to call
    the RetrieveTransaction endpoint.
    """

    PAYMENTS_WRITE = "PAYMENTS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to transaction and refunds information. For example, to
    process payments with the Payments or Checkout API.
    """

    PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS = "PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Allow third party applications to deduct a portion of each transaction amount.
    __Required__ to use multiparty transaction functionality with the Payments
    API.
    """

    PAYMENTS_WRITE_IN_PERSON = "PAYMENTS_WRITE_IN_PERSON"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to payments and refunds information. For example, to
    process in-person payments.
    """

    PAYMENTS_WRITE_SHARED_ONFILE = "PAYMENTS_WRITE_SHARED_ONFILE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Allows the developer to process payments on behalf of a seller using a shared on file payment method.
    """

    SETTLEMENTS_READ = "SETTLEMENTS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to settlement (deposit) information. For example, to call
    the Connect v1 ListSettlements endpoint.
    """

    SUBSCRIPTIONS_READ = "SUBSCRIPTIONS_READ"
    """
    __HTTP Method__: `GET`, `POST`
    
    Grants read access to subscription information. For example, to call the RetrieveSubscription
    endpoint.
    """

    SUBSCRIPTIONS_WRITE = "SUBSCRIPTIONS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to subscription information. For example, to call the CreateSubscription
    endpoint.
    """

    TIMECARDS_READ = "TIMECARDS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to employee timecard information. For example, to call the
    Connect v2 SearchShifts endpoint.
    """

    TIMECARDS_SETTINGS_READ = "TIMECARDS_SETTINGS_READ"
    """
    __HTTP Method__: `GET`
    
    Grants read access to employee timecard settings information. For example, to
    call the GetBreakType endpoint.
    """

    TIMECARDS_SETTINGS_WRITE = "TIMECARDS_SETTINGS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to employee timecard settings information. For example, to
    call the UpdateBreakType endpoint.
    """

    TIMECARDS_WRITE = "TIMECARDS_WRITE"
    """
    __HTTP Method__: `POST`, `PUT`, `DELETE`
    
    Grants write access to employee shift information. For example, to create
    and modify employee shifts.
    """

    def visit(
        self,
        appointments_business_settings_read: typing.Callable[[], T_Result],
        appointments_read: typing.Callable[[], T_Result],
        appointments_write: typing.Callable[[], T_Result],
        bank_accounts_read: typing.Callable[[], T_Result],
        cash_drawer_read: typing.Callable[[], T_Result],
        customers_read: typing.Callable[[], T_Result],
        customers_write: typing.Callable[[], T_Result],
        device_credential_management: typing.Callable[[], T_Result],
        disputes_read: typing.Callable[[], T_Result],
        disputes_write: typing.Callable[[], T_Result],
        employees_read: typing.Callable[[], T_Result],
        employees_write: typing.Callable[[], T_Result],
        giftcards_read: typing.Callable[[], T_Result],
        giftcards_write: typing.Callable[[], T_Result],
        inventory_read: typing.Callable[[], T_Result],
        inventory_write: typing.Callable[[], T_Result],
        invoices_read: typing.Callable[[], T_Result],
        invoices_write: typing.Callable[[], T_Result],
        items_read: typing.Callable[[], T_Result],
        items_write: typing.Callable[[], T_Result],
        loyalty_read: typing.Callable[[], T_Result],
        loyalty_write: typing.Callable[[], T_Result],
        merchant_profile_read: typing.Callable[[], T_Result],
        merchant_profile_write: typing.Callable[[], T_Result],
        online_store_site_read: typing.Callable[[], T_Result],
        online_store_snippets_read: typing.Callable[[], T_Result],
        online_store_snippets_write: typing.Callable[[], T_Result],
        orders_read: typing.Callable[[], T_Result],
        orders_write: typing.Callable[[], T_Result],
        payments_read: typing.Callable[[], T_Result],
        payments_write: typing.Callable[[], T_Result],
        payments_write_additional_recipients: typing.Callable[[], T_Result],
        payments_write_in_person: typing.Callable[[], T_Result],
        payments_write_shared_onfile: typing.Callable[[], T_Result],
        settlements_read: typing.Callable[[], T_Result],
        subscriptions_read: typing.Callable[[], T_Result],
        subscriptions_write: typing.Callable[[], T_Result],
        timecards_read: typing.Callable[[], T_Result],
        timecards_settings_read: typing.Callable[[], T_Result],
        timecards_settings_write: typing.Callable[[], T_Result],
        timecards_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.APPOINTMENTS_BUSINESS_SETTINGS_READ:
            return appointments_business_settings_read()
        if self is OauthScope.APPOINTMENTS_READ:
            return appointments_read()
        if self is OauthScope.APPOINTMENTS_WRITE:
            return appointments_write()
        if self is OauthScope.BANK_ACCOUNTS_READ:
            return bank_accounts_read()
        if self is OauthScope.CASH_DRAWER_READ:
            return cash_drawer_read()
        if self is OauthScope.CUSTOMERS_READ:
            return customers_read()
        if self is OauthScope.CUSTOMERS_WRITE:
            return customers_write()
        if self is OauthScope.DEVICE_CREDENTIAL_MANAGEMENT:
            return device_credential_management()
        if self is OauthScope.DISPUTES_READ:
            return disputes_read()
        if self is OauthScope.DISPUTES_WRITE:
            return disputes_write()
        if self is OauthScope.EMPLOYEES_READ:
            return employees_read()
        if self is OauthScope.EMPLOYEES_WRITE:
            return employees_write()
        if self is OauthScope.GIFTCARDS_READ:
            return giftcards_read()
        if self is OauthScope.GIFTCARDS_WRITE:
            return giftcards_write()
        if self is OauthScope.INVENTORY_READ:
            return inventory_read()
        if self is OauthScope.INVENTORY_WRITE:
            return inventory_write()
        if self is OauthScope.INVOICES_READ:
            return invoices_read()
        if self is OauthScope.INVOICES_WRITE:
            return invoices_write()
        if self is OauthScope.ITEMS_READ:
            return items_read()
        if self is OauthScope.ITEMS_WRITE:
            return items_write()
        if self is OauthScope.LOYALTY_READ:
            return loyalty_read()
        if self is OauthScope.LOYALTY_WRITE:
            return loyalty_write()
        if self is OauthScope.MERCHANT_PROFILE_READ:
            return merchant_profile_read()
        if self is OauthScope.MERCHANT_PROFILE_WRITE:
            return merchant_profile_write()
        if self is OauthScope.ONLINE_STORE_SITE_READ:
            return online_store_site_read()
        if self is OauthScope.ONLINE_STORE_SNIPPETS_READ:
            return online_store_snippets_read()
        if self is OauthScope.ONLINE_STORE_SNIPPETS_WRITE:
            return online_store_snippets_write()
        if self is OauthScope.ORDERS_READ:
            return orders_read()
        if self is OauthScope.ORDERS_WRITE:
            return orders_write()
        if self is OauthScope.PAYMENTS_READ:
            return payments_read()
        if self is OauthScope.PAYMENTS_WRITE:
            return payments_write()
        if self is OauthScope.PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS:
            return payments_write_additional_recipients()
        if self is OauthScope.PAYMENTS_WRITE_IN_PERSON:
            return payments_write_in_person()
        if self is OauthScope.PAYMENTS_WRITE_SHARED_ONFILE:
            return payments_write_shared_onfile()
        if self is OauthScope.SETTLEMENTS_READ:
            return settlements_read()
        if self is OauthScope.SUBSCRIPTIONS_READ:
            return subscriptions_read()
        if self is OauthScope.SUBSCRIPTIONS_WRITE:
            return subscriptions_write()
        if self is OauthScope.TIMECARDS_READ:
            return timecards_read()
        if self is OauthScope.TIMECARDS_SETTINGS_READ:
            return timecards_settings_read()
        if self is OauthScope.TIMECARDS_SETTINGS_WRITE:
            return timecards_settings_write()
        if self is OauthScope.TIMECARDS_WRITE:
            return timecards_write()
