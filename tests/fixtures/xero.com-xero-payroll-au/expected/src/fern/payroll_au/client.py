

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deduction_type import DeductionType
from ..types.earnings_rate import EarningsRate
from ..types.employee import Employee
from ..types.employees import Employees
from ..types.leave_application import LeaveApplication
from ..types.leave_applications import LeaveApplications
from ..types.leave_type import LeaveType
from ..types.pay_items import PayItems
from ..types.pay_run import PayRun
from ..types.pay_runs import PayRuns
from ..types.payroll_calendar import PayrollCalendar
from ..types.payroll_calendars import PayrollCalendars
from ..types.payslip_lines import PayslipLines
from ..types.payslip_object import PayslipObject
from ..types.payslips import Payslips
from ..types.reimbursement_type import ReimbursementType
from ..types.settings_object import SettingsObject
from ..types.super_fund import SuperFund
from ..types.super_fund_products import SuperFundProducts
from ..types.super_funds import SuperFunds
from ..types.timesheet import Timesheet
from ..types.timesheet_object import TimesheetObject
from ..types.timesheets import Timesheets
from .raw_client import AsyncRawPayrollAuClient, RawPayrollAuClient


OMIT = typing.cast(typing.Any, ...)


class PayrollAuClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPayrollAuClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPayrollAuClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPayrollAuClient
        """
        return self._raw_client

    def get_employees(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employees:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 employees will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_employees(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_employees(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_employee(
        self, *, request: typing.Sequence[Employee], request_options: typing.Optional[RequestOptions] = None
    ) -> Employees:
        """
        Parameters
        ----------
        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            A successful request

        Examples
        --------
        from fern import Employee, FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_employee(
            request=[
                Employee(
                    date_of_birth="/Date(322560000000+0000)/",
                    first_name="Karen",
                    last_name="Jones",
                )
            ],
        )
        """
        _response = self._raw_client.create_employee(request=request, request_options=request_options)
        return _response.data

    def get_employee(self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Employees:
        """
        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_employee(
            employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_employee(employee_id, request_options=request_options)
        return _response.data

    def update_employee(
        self,
        employee_id: str,
        *,
        request: typing.Sequence[Employee],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employees:
        """
        Update properties on a single employee

        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            A successful request

        Examples
        --------
        from fern import Employee, FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_employee(
            employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[
                Employee(
                    date_of_birth="/Date(322560000000+0000)/",
                    first_name="Karen",
                    last_name="Jones",
                )
            ],
        )
        """
        _response = self._raw_client.update_employee(employee_id, request=request, request_options=request_options)
        return _response.data

    def get_leave_applications(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_leave_applications(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_leave_applications(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_leave_application(
        self, *, request: typing.Sequence[LeaveApplication], request_options: typing.Optional[RequestOptions] = None
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            A successful request

        Examples
        --------
        from fern import FernApi, LeaveApplication

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_leave_application(
            request=[LeaveApplication()],
        )
        """
        _response = self._raw_client.create_leave_application(request=request, request_options=request_options)
        return _response.data

    def get_leave_application(
        self, leave_application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_leave_application(
            leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_leave_application(leave_application_id, request_options=request_options)
        return _response.data

    def update_leave_application(
        self,
        leave_application_id: str,
        *,
        request: typing.Sequence[LeaveApplication],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            A successful request

        Examples
        --------
        from fern import FernApi, LeaveApplication

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_leave_application(
            leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[LeaveApplication()],
        )
        """
        _response = self._raw_client.update_leave_application(
            leave_application_id, request=request, request_options=request_options
        )
        return _response.data

    def get_pay_items(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayItems:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayItems
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_pay_items(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_pay_items(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_pay_item(
        self,
        *,
        deduction_types: typing.Optional[typing.Sequence[DeductionType]] = OMIT,
        earnings_rates: typing.Optional[typing.Sequence[EarningsRate]] = OMIT,
        leave_types: typing.Optional[typing.Sequence[LeaveType]] = OMIT,
        reimbursement_types: typing.Optional[typing.Sequence[ReimbursementType]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayItems:
        """
        Parameters
        ----------
        deduction_types : typing.Optional[typing.Sequence[DeductionType]]

        earnings_rates : typing.Optional[typing.Sequence[EarningsRate]]

        leave_types : typing.Optional[typing.Sequence[LeaveType]]

        reimbursement_types : typing.Optional[typing.Sequence[ReimbursementType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayItems
            A successful request - currently returns empty array for JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_pay_item()
        """
        _response = self._raw_client.create_pay_item(
            deduction_types=deduction_types,
            earnings_rates=earnings_rates,
            leave_types=leave_types,
            reimbursement_types=reimbursement_types,
            request_options=request_options,
        )
        return _response.data

    def get_pay_runs(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayRuns:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 PayRuns will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_pay_runs(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_pay_runs(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_pay_run(
        self, *, request: typing.Sequence[PayRun], request_options: typing.Optional[RequestOptions] = None
    ) -> PayRuns:
        """
        Parameters
        ----------
        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            A successful request

        Examples
        --------
        from fern import FernApi, PayRun

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_pay_run(
            request=[
                PayRun(
                    payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
                )
            ],
        )
        """
        _response = self._raw_client.create_pay_run(request=request, request_options=request_options)
        return _response.data

    def get_pay_run(self, pay_run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PayRuns:
        """
        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_pay_run(
            pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_pay_run(pay_run_id, request_options=request_options)
        return _response.data

    def update_pay_run(
        self,
        pay_run_id: str,
        *,
        request: typing.Sequence[PayRun],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayRuns:
        """
        Update properties on a single PayRun

        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            A successful request

        Examples
        --------
        from fern import FernApi, PayRun

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_pay_run(
            pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[
                PayRun(
                    payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
                )
            ],
        )
        """
        _response = self._raw_client.update_pay_run(pay_run_id, request=request, request_options=request_options)
        return _response.data

    def get_payroll_calendars(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_payroll_calendars(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_payroll_calendars(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_payroll_calendar(
        self, *, request: typing.Sequence[PayrollCalendar], request_options: typing.Optional[RequestOptions] = None
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        request : typing.Sequence[PayrollCalendar]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            A successful request

        Examples
        --------
        from fern import FernApi, PayrollCalendar

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_payroll_calendar(
            request=[PayrollCalendar()],
        )
        """
        _response = self._raw_client.create_payroll_calendar(request=request, request_options=request_options)
        return _response.data

    def get_payroll_calendar(
        self, payroll_calendar_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        payroll_calendar_id : str
            Payroll Calendar id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_payroll_calendar(
            payroll_calendar_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_payroll_calendar(payroll_calendar_id, request_options=request_options)
        return _response.data

    def get_payslip(self, payslip_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PayslipObject:
        """
        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayslipObject
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_payslip(
            payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_payslip(payslip_id, request_options=request_options)
        return _response.data

    def update_payslip(
        self,
        payslip_id: str,
        *,
        request: typing.Sequence[PayslipLines],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payslips:
        """
        Update lines on a single payslips

        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request : typing.Sequence[PayslipLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payslips
            A successful request - currently returns empty array for JSON

        Examples
        --------
        from fern import FernApi, PayslipLines

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_payslip(
            payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[PayslipLines()],
        )
        """
        _response = self._raw_client.update_payslip(payslip_id, request=request, request_options=request_options)
        return _response.data

    def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsObject:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsObject
            payroll settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_settings()
        """
        _response = self._raw_client.get_settings(request_options=request_options)
        return _response.data

    def get_superfund_products(
        self,
        *,
        abn: typing.Optional[str] = None,
        usi: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFundProducts:
        """
        Parameters
        ----------
        abn : typing.Optional[str]
            The ABN of the Regulated SuperFund

        usi : typing.Optional[str]
            The USI of the Regulated SuperFund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFundProducts
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_superfund_products(
            usi="OSF0001AU",
        )
        """
        _response = self._raw_client.get_superfund_products(abn=abn, usi=usi, request_options=request_options)
        return _response.data

    def get_superfunds(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFunds:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_superfunds(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_superfunds(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_superfund(
        self, *, request: typing.Sequence[SuperFund], request_options: typing.Optional[RequestOptions] = None
    ) -> SuperFunds:
        """
        Parameters
        ----------
        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            A successful request

        Examples
        --------
        from fern import FernApi, SuperFund, SuperFundType

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_superfund(
            request=[
                SuperFund(
                    type=SuperFundType.REGULATED,
                )
            ],
        )
        """
        _response = self._raw_client.create_superfund(request=request, request_options=request_options)
        return _response.data

    def get_superfund(
        self, super_fund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuperFunds:
        """
        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_superfund(
            super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_superfund(super_fund_id, request_options=request_options)
        return _response.data

    def update_superfund(
        self,
        super_fund_id: str,
        *,
        request: typing.Sequence[SuperFund],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFunds:
        """
        Update properties on a single Superfund

        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            A successful request

        Examples
        --------
        from fern import FernApi, SuperFund, SuperFundType

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_superfund(
            super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[
                SuperFund(
                    type=SuperFundType.REGULATED,
                )
            ],
        )
        """
        _response = self._raw_client.update_superfund(super_fund_id, request=request, request_options=request_options)
        return _response.data

    def get_timesheets(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Timesheets:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 timesheets will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_timesheets(
            where='Status=="ACTIVE"',
            order="EmailAddress%20DESC",
        )
        """
        _response = self._raw_client.get_timesheets(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def create_timesheet(
        self, *, request: typing.Sequence[Timesheet], request_options: typing.Optional[RequestOptions] = None
    ) -> Timesheets:
        """
        Parameters
        ----------
        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            A successful request

        Examples
        --------
        from fern import FernApi, Timesheet

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.create_timesheet(
            request=[
                Timesheet(
                    employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
                    end_date="/Date(322560000000+0000)/",
                    start_date="/Date(322560000000+0000)/",
                )
            ],
        )
        """
        _response = self._raw_client.create_timesheet(request=request, request_options=request_options)
        return _response.data

    def get_timesheet(
        self, timesheet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TimesheetObject:
        """
        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimesheetObject
            search results matching criteria

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.get_timesheet(
            timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
        )
        """
        _response = self._raw_client.get_timesheet(timesheet_id, request_options=request_options)
        return _response.data

    def update_timesheet(
        self,
        timesheet_id: str,
        *,
        request: typing.Sequence[Timesheet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Timesheets:
        """
        Update properties on a single timesheet

        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            A successful request

        Examples
        --------
        from fern import FernApi, Timesheet

        client = FernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )
        client.payroll_au.update_timesheet(
            timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            request=[
                Timesheet(
                    employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
                    end_date="/Date(322560000000+0000)/",
                    start_date="/Date(322560000000+0000)/",
                )
            ],
        )
        """
        _response = self._raw_client.update_timesheet(timesheet_id, request=request, request_options=request_options)
        return _response.data


class AsyncPayrollAuClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPayrollAuClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPayrollAuClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPayrollAuClient
        """
        return self._raw_client

    async def get_employees(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employees:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 employees will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_employees(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_employees(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_employee(
        self, *, request: typing.Sequence[Employee], request_options: typing.Optional[RequestOptions] = None
    ) -> Employees:
        """
        Parameters
        ----------
        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Employee

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_employee(
                request=[
                    Employee(
                        date_of_birth="/Date(322560000000+0000)/",
                        first_name="Karen",
                        last_name="Jones",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_employee(request=request, request_options=request_options)
        return _response.data

    async def get_employee(
        self, employee_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Employees:
        """
        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_employee(
                employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_employee(employee_id, request_options=request_options)
        return _response.data

    async def update_employee(
        self,
        employee_id: str,
        *,
        request: typing.Sequence[Employee],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employees:
        """
        Update properties on a single employee

        Parameters
        ----------
        employee_id : str
            Employee id for single object

        request : typing.Sequence[Employee]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employees
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Employee

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_employee(
                employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[
                    Employee(
                        date_of_birth="/Date(322560000000+0000)/",
                        first_name="Karen",
                        last_name="Jones",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_employee(
            employee_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_leave_applications(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_leave_applications(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_leave_applications(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_leave_application(
        self, *, request: typing.Sequence[LeaveApplication], request_options: typing.Optional[RequestOptions] = None
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LeaveApplication

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_leave_application(
                request=[LeaveApplication()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_leave_application(request=request, request_options=request_options)
        return _response.data

    async def get_leave_application(
        self, leave_application_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_leave_application(
                leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_leave_application(leave_application_id, request_options=request_options)
        return _response.data

    async def update_leave_application(
        self,
        leave_application_id: str,
        *,
        request: typing.Sequence[LeaveApplication],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LeaveApplications:
        """
        Parameters
        ----------
        leave_application_id : str
            Leave Application id for single object

        request : typing.Sequence[LeaveApplication]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaveApplications
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LeaveApplication

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_leave_application(
                leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[LeaveApplication()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_leave_application(
            leave_application_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_pay_items(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayItems:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayItems
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_pay_items(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pay_items(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_pay_item(
        self,
        *,
        deduction_types: typing.Optional[typing.Sequence[DeductionType]] = OMIT,
        earnings_rates: typing.Optional[typing.Sequence[EarningsRate]] = OMIT,
        leave_types: typing.Optional[typing.Sequence[LeaveType]] = OMIT,
        reimbursement_types: typing.Optional[typing.Sequence[ReimbursementType]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayItems:
        """
        Parameters
        ----------
        deduction_types : typing.Optional[typing.Sequence[DeductionType]]

        earnings_rates : typing.Optional[typing.Sequence[EarningsRate]]

        leave_types : typing.Optional[typing.Sequence[LeaveType]]

        reimbursement_types : typing.Optional[typing.Sequence[ReimbursementType]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayItems
            A successful request - currently returns empty array for JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_pay_item()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pay_item(
            deduction_types=deduction_types,
            earnings_rates=earnings_rates,
            leave_types=leave_types,
            reimbursement_types=reimbursement_types,
            request_options=request_options,
        )
        return _response.data

    async def get_pay_runs(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayRuns:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 PayRuns will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_pay_runs(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pay_runs(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_pay_run(
        self, *, request: typing.Sequence[PayRun], request_options: typing.Optional[RequestOptions] = None
    ) -> PayRuns:
        """
        Parameters
        ----------
        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PayRun

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_pay_run(
                request=[
                    PayRun(
                        payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pay_run(request=request, request_options=request_options)
        return _response.data

    async def get_pay_run(self, pay_run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PayRuns:
        """
        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_pay_run(
                pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pay_run(pay_run_id, request_options=request_options)
        return _response.data

    async def update_pay_run(
        self,
        pay_run_id: str,
        *,
        request: typing.Sequence[PayRun],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayRuns:
        """
        Update properties on a single PayRun

        Parameters
        ----------
        pay_run_id : str
            PayRun id for single object

        request : typing.Sequence[PayRun]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayRuns
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PayRun

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_pay_run(
                pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[
                    PayRun(
                        payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pay_run(pay_run_id, request=request, request_options=request_options)
        return _response.data

    async def get_payroll_calendars(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 objects will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_payroll_calendars(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payroll_calendars(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_payroll_calendar(
        self, *, request: typing.Sequence[PayrollCalendar], request_options: typing.Optional[RequestOptions] = None
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        request : typing.Sequence[PayrollCalendar]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PayrollCalendar

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_payroll_calendar(
                request=[PayrollCalendar()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payroll_calendar(request=request, request_options=request_options)
        return _response.data

    async def get_payroll_calendar(
        self, payroll_calendar_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayrollCalendars:
        """
        Parameters
        ----------
        payroll_calendar_id : str
            Payroll Calendar id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayrollCalendars
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_payroll_calendar(
                payroll_calendar_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payroll_calendar(payroll_calendar_id, request_options=request_options)
        return _response.data

    async def get_payslip(
        self, payslip_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PayslipObject:
        """
        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayslipObject
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_payslip(
                payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payslip(payslip_id, request_options=request_options)
        return _response.data

    async def update_payslip(
        self,
        payslip_id: str,
        *,
        request: typing.Sequence[PayslipLines],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payslips:
        """
        Update lines on a single payslips

        Parameters
        ----------
        payslip_id : str
            Payslip id for single object

        request : typing.Sequence[PayslipLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payslips
            A successful request - currently returns empty array for JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PayslipLines

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_payslip(
                payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[PayslipLines()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_payslip(payslip_id, request=request, request_options=request_options)
        return _response.data

    async def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsObject:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsObject
            payroll settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings(request_options=request_options)
        return _response.data

    async def get_superfund_products(
        self,
        *,
        abn: typing.Optional[str] = None,
        usi: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFundProducts:
        """
        Parameters
        ----------
        abn : typing.Optional[str]
            The ABN of the Regulated SuperFund

        usi : typing.Optional[str]
            The USI of the Regulated SuperFund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFundProducts
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_superfund_products(
                usi="OSF0001AU",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_superfund_products(abn=abn, usi=usi, request_options=request_options)
        return _response.data

    async def get_superfunds(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFunds:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_superfunds(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_superfunds(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_superfund(
        self, *, request: typing.Sequence[SuperFund], request_options: typing.Optional[RequestOptions] = None
    ) -> SuperFunds:
        """
        Parameters
        ----------
        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SuperFund, SuperFundType

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_superfund(
                request=[
                    SuperFund(
                        type=SuperFundType.REGULATED,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_superfund(request=request, request_options=request_options)
        return _response.data

    async def get_superfund(
        self, super_fund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuperFunds:
        """
        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_superfund(
                super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_superfund(super_fund_id, request_options=request_options)
        return _response.data

    async def update_superfund(
        self,
        super_fund_id: str,
        *,
        request: typing.Sequence[SuperFund],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuperFunds:
        """
        Update properties on a single Superfund

        Parameters
        ----------
        super_fund_id : str
            Superfund id for single object

        request : typing.Sequence[SuperFund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuperFunds
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SuperFund, SuperFundType

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_superfund(
                super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[
                    SuperFund(
                        type=SuperFundType.REGULATED,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_superfund(
            super_fund_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_timesheets(
        self,
        *,
        where: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Timesheets:
        """
        Parameters
        ----------
        where : typing.Optional[str]
            Filter by an any element

        order : typing.Optional[str]
            Order by an any element

        page : typing.Optional[int]
            e.g. page=1 – Up to 100 timesheets will be returned in a single API call

        if_modified_since : typing.Optional[str]
            Only records created or modified since this timestamp will be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_timesheets(
                where='Status=="ACTIVE"',
                order="EmailAddress%20DESC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_timesheets(
            where=where, order=order, page=page, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def create_timesheet(
        self, *, request: typing.Sequence[Timesheet], request_options: typing.Optional[RequestOptions] = None
    ) -> Timesheets:
        """
        Parameters
        ----------
        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Timesheet

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.create_timesheet(
                request=[
                    Timesheet(
                        employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
                        end_date="/Date(322560000000+0000)/",
                        start_date="/Date(322560000000+0000)/",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_timesheet(request=request, request_options=request_options)
        return _response.data

    async def get_timesheet(
        self, timesheet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TimesheetObject:
        """
        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimesheetObject
            search results matching criteria

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.get_timesheet(
                timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_timesheet(timesheet_id, request_options=request_options)
        return _response.data

    async def update_timesheet(
        self,
        timesheet_id: str,
        *,
        request: typing.Sequence[Timesheet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Timesheets:
        """
        Update properties on a single timesheet

        Parameters
        ----------
        timesheet_id : str
            Timesheet id for single object

        request : typing.Sequence[Timesheet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timesheets
            A successful request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Timesheet

        client = AsyncFernApi(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payroll_au.update_timesheet(
                timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
                request=[
                    Timesheet(
                        employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
                        end_date="/Date(322560000000+0000)/",
                        start_date="/Date(322560000000+0000)/",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_timesheet(
            timesheet_id, request=request, request_options=request_options
        )
        return _response.data
