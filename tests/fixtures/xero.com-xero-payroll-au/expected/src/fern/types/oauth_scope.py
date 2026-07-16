

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    ACCOUNTING_ATTACHMENTS = "accounting.attachments"
    """
    Grant read-write access to attachments
    """

    ACCOUNTING_ATTACHMENTS_READ = "accounting.attachments.read"
    """
    Grant read-only access to attachments
    """

    ACCOUNTING_CONTACTS = "accounting.contacts"
    """
    Grant read-write access to contacts and contact groups
    """

    ACCOUNTING_CONTACTS_READ = "accounting.contacts.read"
    """
    Grant read-only access to contacts and contact groups
    """

    ACCOUNTING_JOURNALS_READ = "accounting.journals.read"
    """
    Grant read-only access to journals
    """

    ACCOUNTING_REPORTS_READ = "accounting.reports.read"
    """
    Grant read-only access to accounting reports
    """

    ACCOUNTING_SETTINGS = "accounting.settings"
    """
    Grant read-write access to organisation and account settings
    """

    ACCOUNTING_SETTINGS_READ = "accounting.settings.read"
    """
    Grant read-only access to organisation and account settings
    """

    ACCOUNTING_TRANSACTIONS = "accounting.transactions"
    """
    Grant read-write access to bank transactions, credit notes, invoices, repeating invoices
    """

    ACCOUNTING_TRANSACTIONS_READ = "accounting.transactions.read"
    """
    Grant read-only access to invoices
    """

    ASSETS_ASSETS_READ = "assets assets.read"
    """
    Grant read-only access to fixed assets
    """

    BANKFEEDS = "bankfeeds"
    """
    Grant read-write access to bankfeeds
    """

    EMAIL = "email"
    """
    Grant read-only access to your email
    """

    FILES = "files"
    """
    Grant read-write access to files and folders
    """

    FILES_READ = "files.read"
    """
    Grant read-only access to files and folders
    """

    OPENID = "openid"
    """
    Grant read-only access to your open id
    """

    PAYMENTSERVICES = "paymentservices"
    """
    Grant read-write access to payment services
    """

    PAYROLL = "payroll"
    """
    Grant read-write access to payroll
    """

    PAYROLL_EMPLOYEES = "payroll.employees"
    """
    Grant read-write access to payroll employees
    """

    PAYROLL_EMPLOYEES_READ = "payroll.employees.read"
    """
    Grant read-only access to payroll employees
    """

    PAYROLL_LEAVEAPPLICATIONS = "payroll.leaveapplications"
    """
    Grant read-write access to payroll leaveapplications
    """

    PAYROLL_LEAVEAPPLICATIONS_READ = "payroll.leaveapplications.read"
    """
    Grant read-only access to payroll leaveapplications
    """

    PAYROLL_PAYITEMS = "payroll.payitems"
    """
    Grant read-write access to payroll payitems
    """

    PAYROLL_PAYITEMS_READ = "payroll.payitems.read"
    """
    Grant read-only access to payroll payitems
    """

    PAYROLL_PAYROLLCALENDARS = "payroll.payrollcalendars"
    """
    Grant read-write access to payroll calendars
    """

    PAYROLL_PAYROLLCALENDARS_READ = "payroll.payrollcalendars.read"
    """
    Grant read-only access to payroll calendars
    """

    PAYROLL_PAYRUNS = "payroll.payruns"
    """
    Grant read-write access to payroll payruns
    """

    PAYROLL_PAYRUNS_READ = "payroll.payruns.read"
    """
    Grant read-only access to payroll payruns
    """

    PAYROLL_PAYSLIP = "payroll.payslip"
    """
    Grant read-write access to payroll payslips
    """

    PAYROLL_PAYSLIP_READ = "payroll.payslip.read"
    """
    Grant read-only access to payroll payslips
    """

    PAYROLL_READ = "payroll.read"
    """
    Grant read-only access to payroll
    """

    PAYROLL_SETTINGS_READ = "payroll.settings.read"
    """
    Grant read-only access to payroll settings
    """

    PAYROLL_SUPERFUNDPRODUCTS_READ = "payroll.superfundproducts.read"
    """
    Grant read-only access to payroll superfundproducts
    """

    PAYROLL_SUPERFUNDS = "payroll.superfunds"
    """
    Grant read-write access to payroll superfunds
    """

    PAYROLL_SUPERFUNDS_READ = "payroll.superfunds.read"
    """
    Grant read-only access to payroll superfunds
    """

    PAYROLL_TIMESHEETS = "payroll.timesheets"
    """
    Grant read-write access to payroll timesheets
    """

    PAYROLL_TIMESHEETS_READ = "payroll.timesheets.read"
    """
    Grant read-only access to payroll timesheets
    """

    PROFILE = "profile"
    """
    your profile information
    """

    PROJECTS = "projects"
    """
    Grant read-write access to projects
    """

    PROJECTS_READ = "projects.read"
    """
    Grant read-only access to projects
    """

    def visit(
        self,
        accounting_attachments: typing.Callable[[], T_Result],
        accounting_attachments_read: typing.Callable[[], T_Result],
        accounting_contacts: typing.Callable[[], T_Result],
        accounting_contacts_read: typing.Callable[[], T_Result],
        accounting_journals_read: typing.Callable[[], T_Result],
        accounting_reports_read: typing.Callable[[], T_Result],
        accounting_settings: typing.Callable[[], T_Result],
        accounting_settings_read: typing.Callable[[], T_Result],
        accounting_transactions: typing.Callable[[], T_Result],
        accounting_transactions_read: typing.Callable[[], T_Result],
        assets_assets_read: typing.Callable[[], T_Result],
        bankfeeds: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        files: typing.Callable[[], T_Result],
        files_read: typing.Callable[[], T_Result],
        openid: typing.Callable[[], T_Result],
        paymentservices: typing.Callable[[], T_Result],
        payroll: typing.Callable[[], T_Result],
        payroll_employees: typing.Callable[[], T_Result],
        payroll_employees_read: typing.Callable[[], T_Result],
        payroll_leaveapplications: typing.Callable[[], T_Result],
        payroll_leaveapplications_read: typing.Callable[[], T_Result],
        payroll_payitems: typing.Callable[[], T_Result],
        payroll_payitems_read: typing.Callable[[], T_Result],
        payroll_payrollcalendars: typing.Callable[[], T_Result],
        payroll_payrollcalendars_read: typing.Callable[[], T_Result],
        payroll_payruns: typing.Callable[[], T_Result],
        payroll_payruns_read: typing.Callable[[], T_Result],
        payroll_payslip: typing.Callable[[], T_Result],
        payroll_payslip_read: typing.Callable[[], T_Result],
        payroll_read: typing.Callable[[], T_Result],
        payroll_settings_read: typing.Callable[[], T_Result],
        payroll_superfundproducts_read: typing.Callable[[], T_Result],
        payroll_superfunds: typing.Callable[[], T_Result],
        payroll_superfunds_read: typing.Callable[[], T_Result],
        payroll_timesheets: typing.Callable[[], T_Result],
        payroll_timesheets_read: typing.Callable[[], T_Result],
        profile: typing.Callable[[], T_Result],
        projects: typing.Callable[[], T_Result],
        projects_read: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ACCOUNTING_ATTACHMENTS:
            return accounting_attachments()
        if self is OauthScope.ACCOUNTING_ATTACHMENTS_READ:
            return accounting_attachments_read()
        if self is OauthScope.ACCOUNTING_CONTACTS:
            return accounting_contacts()
        if self is OauthScope.ACCOUNTING_CONTACTS_READ:
            return accounting_contacts_read()
        if self is OauthScope.ACCOUNTING_JOURNALS_READ:
            return accounting_journals_read()
        if self is OauthScope.ACCOUNTING_REPORTS_READ:
            return accounting_reports_read()
        if self is OauthScope.ACCOUNTING_SETTINGS:
            return accounting_settings()
        if self is OauthScope.ACCOUNTING_SETTINGS_READ:
            return accounting_settings_read()
        if self is OauthScope.ACCOUNTING_TRANSACTIONS:
            return accounting_transactions()
        if self is OauthScope.ACCOUNTING_TRANSACTIONS_READ:
            return accounting_transactions_read()
        if self is OauthScope.ASSETS_ASSETS_READ:
            return assets_assets_read()
        if self is OauthScope.BANKFEEDS:
            return bankfeeds()
        if self is OauthScope.EMAIL:
            return email()
        if self is OauthScope.FILES:
            return files()
        if self is OauthScope.FILES_READ:
            return files_read()
        if self is OauthScope.OPENID:
            return openid()
        if self is OauthScope.PAYMENTSERVICES:
            return paymentservices()
        if self is OauthScope.PAYROLL:
            return payroll()
        if self is OauthScope.PAYROLL_EMPLOYEES:
            return payroll_employees()
        if self is OauthScope.PAYROLL_EMPLOYEES_READ:
            return payroll_employees_read()
        if self is OauthScope.PAYROLL_LEAVEAPPLICATIONS:
            return payroll_leaveapplications()
        if self is OauthScope.PAYROLL_LEAVEAPPLICATIONS_READ:
            return payroll_leaveapplications_read()
        if self is OauthScope.PAYROLL_PAYITEMS:
            return payroll_payitems()
        if self is OauthScope.PAYROLL_PAYITEMS_READ:
            return payroll_payitems_read()
        if self is OauthScope.PAYROLL_PAYROLLCALENDARS:
            return payroll_payrollcalendars()
        if self is OauthScope.PAYROLL_PAYROLLCALENDARS_READ:
            return payroll_payrollcalendars_read()
        if self is OauthScope.PAYROLL_PAYRUNS:
            return payroll_payruns()
        if self is OauthScope.PAYROLL_PAYRUNS_READ:
            return payroll_payruns_read()
        if self is OauthScope.PAYROLL_PAYSLIP:
            return payroll_payslip()
        if self is OauthScope.PAYROLL_PAYSLIP_READ:
            return payroll_payslip_read()
        if self is OauthScope.PAYROLL_READ:
            return payroll_read()
        if self is OauthScope.PAYROLL_SETTINGS_READ:
            return payroll_settings_read()
        if self is OauthScope.PAYROLL_SUPERFUNDPRODUCTS_READ:
            return payroll_superfundproducts_read()
        if self is OauthScope.PAYROLL_SUPERFUNDS:
            return payroll_superfunds()
        if self is OauthScope.PAYROLL_SUPERFUNDS_READ:
            return payroll_superfunds_read()
        if self is OauthScope.PAYROLL_TIMESHEETS:
            return payroll_timesheets()
        if self is OauthScope.PAYROLL_TIMESHEETS_READ:
            return payroll_timesheets_read()
        if self is OauthScope.PROFILE:
            return profile()
        if self is OauthScope.PROJECTS:
            return projects()
        if self is OauthScope.PROJECTS_READ:
            return projects_read()
