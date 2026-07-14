

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UnifiedApiId(str, enum.Enum):
    """
    Name of Apideck Unified API
    """

    ACCOUNTING = "accounting"
    ATS = "ats"
    CALENDAR = "calendar"
    CRM = "crm"
    CSP = "csp"
    CUSTOMER_SUPPORT = "customer-support"
    ECOMMERCE = "ecommerce"
    EMAIL = "email"
    EMAIL_MARKETING = "email-marketing"
    EXPENSE_MANAGEMENT = "expense-management"
    FILE_STORAGE = "file-storage"
    FORM = "form"
    HRIS = "hris"
    LEAD = "lead"
    PAYROLL = "payroll"
    POS = "pos"
    PROCUREMENT = "procurement"
    PROJECT_MANAGEMENT = "project-management"
    SCRIPT = "script"
    SMS = "sms"
    SPREADSHEET = "spreadsheet"
    TEAM_MESSAGING = "team-messaging"
    ISSUE_TRACKING = "issue-tracking"
    TIME_REGISTRATION = "time-registration"
    TRANSACTIONAL_EMAIL = "transactional-email"
    VAULT = "vault"

    def visit(
        self,
        accounting: typing.Callable[[], T_Result],
        ats: typing.Callable[[], T_Result],
        calendar: typing.Callable[[], T_Result],
        crm: typing.Callable[[], T_Result],
        csp: typing.Callable[[], T_Result],
        customer_support: typing.Callable[[], T_Result],
        ecommerce: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        email_marketing: typing.Callable[[], T_Result],
        expense_management: typing.Callable[[], T_Result],
        file_storage: typing.Callable[[], T_Result],
        form: typing.Callable[[], T_Result],
        hris: typing.Callable[[], T_Result],
        lead: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
        pos: typing.Callable[[], T_Result],
        procurement: typing.Callable[[], T_Result],
        project_management: typing.Callable[[], T_Result],
        script: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        spreadsheet: typing.Callable[[], T_Result],
        team_messaging: typing.Callable[[], T_Result],
        issue_tracking: typing.Callable[[], T_Result],
        time_registration: typing.Callable[[], T_Result],
        transactional_email: typing.Callable[[], T_Result],
        vault: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnifiedApiId.ACCOUNTING:
            return accounting()
        if self is UnifiedApiId.ATS:
            return ats()
        if self is UnifiedApiId.CALENDAR:
            return calendar()
        if self is UnifiedApiId.CRM:
            return crm()
        if self is UnifiedApiId.CSP:
            return csp()
        if self is UnifiedApiId.CUSTOMER_SUPPORT:
            return customer_support()
        if self is UnifiedApiId.ECOMMERCE:
            return ecommerce()
        if self is UnifiedApiId.EMAIL:
            return email()
        if self is UnifiedApiId.EMAIL_MARKETING:
            return email_marketing()
        if self is UnifiedApiId.EXPENSE_MANAGEMENT:
            return expense_management()
        if self is UnifiedApiId.FILE_STORAGE:
            return file_storage()
        if self is UnifiedApiId.FORM:
            return form()
        if self is UnifiedApiId.HRIS:
            return hris()
        if self is UnifiedApiId.LEAD:
            return lead()
        if self is UnifiedApiId.PAYROLL:
            return payroll()
        if self is UnifiedApiId.POS:
            return pos()
        if self is UnifiedApiId.PROCUREMENT:
            return procurement()
        if self is UnifiedApiId.PROJECT_MANAGEMENT:
            return project_management()
        if self is UnifiedApiId.SCRIPT:
            return script()
        if self is UnifiedApiId.SMS:
            return sms()
        if self is UnifiedApiId.SPREADSHEET:
            return spreadsheet()
        if self is UnifiedApiId.TEAM_MESSAGING:
            return team_messaging()
        if self is UnifiedApiId.ISSUE_TRACKING:
            return issue_tracking()
        if self is UnifiedApiId.TIME_REGISTRATION:
            return time_registration()
        if self is UnifiedApiId.TRANSACTIONAL_EMAIL:
            return transactional_email()
        if self is UnifiedApiId.VAULT:
            return vault()
