

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkEventName(enum.StrEnum):
    """
    A string representing the event that has just occurred in the Link flow.
    """

    BANK_INCOME_INSIGHTS_COMPLETED = "BANK_INCOME_INSIGHTS_COMPLETED"
    CLOSE_OAUTH = "CLOSE_OAUTH"
    ERROR = "ERROR"
    EXIT = "EXIT"
    FAIL_OAUTH = "FAIL_OAUTH"
    HANDOFF = "HANDOFF"
    OPEN = "OPEN"
    OPEN_MY_PLAID = "OPEN_MY_PLAID"
    OPEN_OAUTH = "OPEN_OAUTH"
    SEARCH_INSTITUTION = "SEARCH_INSTITUTION"
    SELECT_AUTH_TYPE = "SELECT_AUTH_TYPE"
    SELECT_BRAND = "SELECT_BRAND"
    SELECT_DEGRADED_INSTITUTION = "SELECT_DEGRADED_INSTITUTION"
    SELECT_DOWN_INSTITUTION = "SELECT_DOWN_INSTITUTION"
    SELECT_INSTITUTION = "SELECT_INSTITUTION"
    SUBMIT_ACCOUNT_NUMBER = "SUBMIT_ACCOUNT_NUMBER"
    SUBMIT_CREDENTIALS = "SUBMIT_CREDENTIALS"
    SUBMIT_DOCUMENTS = "SUBMIT_DOCUMENTS"
    SUBMIT_DOCUMENTS_ERROR = "SUBMIT_DOCUMENTS_ERROR"
    SUBMIT_DOCUMENTS_SUCCESS = "SUBMIT_DOCUMENTS_SUCCESS"
    SUBMIT_MFA = "SUBMIT_MFA"
    SUBMIT_ROUTING_NUMBER = "SUBMIT_ROUTING_NUMBER"
    TRANSITION_VIEW = "TRANSITION_VIEW"
    VIEW_DATA_TYPES = "VIEW_DATA_TYPES"

    def visit(
        self,
        bank_income_insights_completed: typing.Callable[[], T_Result],
        close_oauth: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        exit: typing.Callable[[], T_Result],
        fail_oauth: typing.Callable[[], T_Result],
        handoff: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        open_my_plaid: typing.Callable[[], T_Result],
        open_oauth: typing.Callable[[], T_Result],
        search_institution: typing.Callable[[], T_Result],
        select_auth_type: typing.Callable[[], T_Result],
        select_brand: typing.Callable[[], T_Result],
        select_degraded_institution: typing.Callable[[], T_Result],
        select_down_institution: typing.Callable[[], T_Result],
        select_institution: typing.Callable[[], T_Result],
        submit_account_number: typing.Callable[[], T_Result],
        submit_credentials: typing.Callable[[], T_Result],
        submit_documents: typing.Callable[[], T_Result],
        submit_documents_error: typing.Callable[[], T_Result],
        submit_documents_success: typing.Callable[[], T_Result],
        submit_mfa: typing.Callable[[], T_Result],
        submit_routing_number: typing.Callable[[], T_Result],
        transition_view: typing.Callable[[], T_Result],
        view_data_types: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkEventName.BANK_INCOME_INSIGHTS_COMPLETED:
            return bank_income_insights_completed()
        if self is LinkEventName.CLOSE_OAUTH:
            return close_oauth()
        if self is LinkEventName.ERROR:
            return error()
        if self is LinkEventName.EXIT:
            return exit()
        if self is LinkEventName.FAIL_OAUTH:
            return fail_oauth()
        if self is LinkEventName.HANDOFF:
            return handoff()
        if self is LinkEventName.OPEN:
            return open()
        if self is LinkEventName.OPEN_MY_PLAID:
            return open_my_plaid()
        if self is LinkEventName.OPEN_OAUTH:
            return open_oauth()
        if self is LinkEventName.SEARCH_INSTITUTION:
            return search_institution()
        if self is LinkEventName.SELECT_AUTH_TYPE:
            return select_auth_type()
        if self is LinkEventName.SELECT_BRAND:
            return select_brand()
        if self is LinkEventName.SELECT_DEGRADED_INSTITUTION:
            return select_degraded_institution()
        if self is LinkEventName.SELECT_DOWN_INSTITUTION:
            return select_down_institution()
        if self is LinkEventName.SELECT_INSTITUTION:
            return select_institution()
        if self is LinkEventName.SUBMIT_ACCOUNT_NUMBER:
            return submit_account_number()
        if self is LinkEventName.SUBMIT_CREDENTIALS:
            return submit_credentials()
        if self is LinkEventName.SUBMIT_DOCUMENTS:
            return submit_documents()
        if self is LinkEventName.SUBMIT_DOCUMENTS_ERROR:
            return submit_documents_error()
        if self is LinkEventName.SUBMIT_DOCUMENTS_SUCCESS:
            return submit_documents_success()
        if self is LinkEventName.SUBMIT_MFA:
            return submit_mfa()
        if self is LinkEventName.SUBMIT_ROUTING_NUMBER:
            return submit_routing_number()
        if self is LinkEventName.TRANSITION_VIEW:
            return transition_view()
        if self is LinkEventName.VIEW_DATA_TYPES:
            return view_data_types()
