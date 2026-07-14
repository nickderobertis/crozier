

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LogUnifiedApi(str, enum.Enum):
    """
    Which Unified Api request was made to.
    """

    CRM = "crm"
    LEAD = "lead"
    PROXY = "proxy"
    VAULT = "vault"
    ACCOUNTING = "accounting"
    HRIS = "hris"
    ATS = "ats"
    ECOMMERCE = "ecommerce"
    ISSUE_TRACKING = "issue-tracking"
    POS = "pos"
    FILE_STORAGE = "file-storage"
    SMS = "sms"

    def visit(
        self,
        crm: typing.Callable[[], T_Result],
        lead: typing.Callable[[], T_Result],
        proxy: typing.Callable[[], T_Result],
        vault: typing.Callable[[], T_Result],
        accounting: typing.Callable[[], T_Result],
        hris: typing.Callable[[], T_Result],
        ats: typing.Callable[[], T_Result],
        ecommerce: typing.Callable[[], T_Result],
        issue_tracking: typing.Callable[[], T_Result],
        pos: typing.Callable[[], T_Result],
        file_storage: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogUnifiedApi.CRM:
            return crm()
        if self is LogUnifiedApi.LEAD:
            return lead()
        if self is LogUnifiedApi.PROXY:
            return proxy()
        if self is LogUnifiedApi.VAULT:
            return vault()
        if self is LogUnifiedApi.ACCOUNTING:
            return accounting()
        if self is LogUnifiedApi.HRIS:
            return hris()
        if self is LogUnifiedApi.ATS:
            return ats()
        if self is LogUnifiedApi.ECOMMERCE:
            return ecommerce()
        if self is LogUnifiedApi.ISSUE_TRACKING:
            return issue_tracking()
        if self is LogUnifiedApi.POS:
            return pos()
        if self is LogUnifiedApi.FILE_STORAGE:
            return file_storage()
        if self is LogUnifiedApi.SMS:
            return sms()
