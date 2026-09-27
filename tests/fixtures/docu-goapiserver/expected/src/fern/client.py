

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .absences.client import AbsencesClient, AsyncAbsencesClient
    from .activities_summary.client import ActivitiesSummaryClient, AsyncActivitiesSummaryClient
    from .activity_details.client import ActivityDetailsClient, AsyncActivityDetailsClient
    from .attendances.client import AsyncAttendancesClient, AttendancesClient
    from .billing_attendance_audits.client import AsyncBillingAttendanceAuditsClient, BillingAttendanceAuditsClient
    from .billing_plans.client import AsyncBillingPlansClient, BillingPlansClient
    from .classroom_attendance.client import AsyncClassroomAttendanceClient, ClassroomAttendanceClient
    from .companies.client import AsyncCompaniesClient, CompaniesClient
    from .data_refresh.client import AsyncDataRefreshClient, DataRefreshClient
    from .efficiency_ratios.client import AsyncEfficiencyRatiosClient, EfficiencyRatiosClient
    from .enrollment_tracker.client import AsyncEnrollmentTrackerClient, EnrollmentTrackerClient
    from .enrollments.client import AsyncEnrollmentsClient, EnrollmentsClient
    from .family_balances.client import AsyncFamilyBalancesClient, FamilyBalancesClient
    from .gusto_companies.client import AsyncGustoCompaniesClient, GustoCompaniesClient
    from .gusto_contractors.client import AsyncGustoContractorsClient, GustoContractorsClient
    from .gusto_employees.client import AsyncGustoEmployeesClient, GustoEmployeesClient
    from .gusto_payrolls.client import AsyncGustoPayrollsClient, GustoPayrollsClient
    from .leads.client import AsyncLeadsClient, LeadsClient
    from .new_start_tracker.client import AsyncNewStartTrackerClient, NewStartTrackerClient
    from .payments.client import AsyncPaymentsClient, PaymentsClient
    from .pre_registration_fallout.client import AsyncPreRegistrationFalloutClient, PreRegistrationFalloutClient
    from .procare_messages.client import AsyncProcareMessagesClient, ProcareMessagesClient
    from .procare_staff.client import AsyncProcareStaffClient, ProcareStaffClient
    from .rooms.client import AsyncRoomsClient, RoomsClient
    from .schools.client import AsyncSchoolsClient, SchoolsClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .sibling_discounts.client import AsyncSiblingDiscountsClient, SiblingDiscountsClient
    from .spaces.client import AsyncSpacesClient, SpacesClient
    from .students.client import AsyncStudentsClient, StudentsClient
    from .transition_tracker.client import AsyncTransitionTrackerClient, TransitionTrackerClient
    from .users.client import AsyncUsersClient, UsersClient
    from .waitlist.client import AsyncWaitlistClient, WaitlistClient
    from .withdrawal_tracker.client import AsyncWithdrawalTrackerClient, WithdrawalTrackerClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    host : typing.Optional[str]
        Server URL variable for 'host'. Defaults to 'api.example.com'.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        host: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        if host is not None:
            _host = host if host is not None else "api.example.com"
            base_url = "https://{host}/primula/api/v3".format(host=_host)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._sessions: typing.Optional[SessionsClient] = None
        self._schools: typing.Optional[SchoolsClient] = None
        self._companies: typing.Optional[CompaniesClient] = None
        self._rooms: typing.Optional[RoomsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._leads: typing.Optional[LeadsClient] = None
        self._students: typing.Optional[StudentsClient] = None
        self._payments: typing.Optional[PaymentsClient] = None
        self._enrollments: typing.Optional[EnrollmentsClient] = None
        self._family_balances: typing.Optional[FamilyBalancesClient] = None
        self._pre_registration_fallout: typing.Optional[PreRegistrationFalloutClient] = None
        self._absences: typing.Optional[AbsencesClient] = None
        self._waitlist: typing.Optional[WaitlistClient] = None
        self._billing_plans: typing.Optional[BillingPlansClient] = None
        self._spaces: typing.Optional[SpacesClient] = None
        self._enrollment_tracker: typing.Optional[EnrollmentTrackerClient] = None
        self._efficiency_ratios: typing.Optional[EfficiencyRatiosClient] = None
        self._procare_messages: typing.Optional[ProcareMessagesClient] = None
        self._attendances: typing.Optional[AttendancesClient] = None
        self._billing_attendance_audits: typing.Optional[BillingAttendanceAuditsClient] = None
        self._classroom_attendance: typing.Optional[ClassroomAttendanceClient] = None
        self._activities_summary: typing.Optional[ActivitiesSummaryClient] = None
        self._activity_details: typing.Optional[ActivityDetailsClient] = None
        self._data_refresh: typing.Optional[DataRefreshClient] = None
        self._sibling_discounts: typing.Optional[SiblingDiscountsClient] = None
        self._new_start_tracker: typing.Optional[NewStartTrackerClient] = None
        self._withdrawal_tracker: typing.Optional[WithdrawalTrackerClient] = None
        self._transition_tracker: typing.Optional[TransitionTrackerClient] = None
        self._gusto_companies: typing.Optional[GustoCompaniesClient] = None
        self._gusto_employees: typing.Optional[GustoEmployeesClient] = None
        self._gusto_contractors: typing.Optional[GustoContractorsClient] = None
        self._gusto_payrolls: typing.Optional[GustoPayrollsClient] = None
        self._procare_staff: typing.Optional[ProcareStaffClient] = None

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def schools(self):
        if self._schools is None:
            from .schools.client import SchoolsClient

            self._schools = SchoolsClient(client_wrapper=self._client_wrapper)
        return self._schools

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import CompaniesClient

            self._companies = CompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def rooms(self):
        if self._rooms is None:
            from .rooms.client import RoomsClient

            self._rooms = RoomsClient(client_wrapper=self._client_wrapper)
        return self._rooms

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def leads(self):
        if self._leads is None:
            from .leads.client import LeadsClient

            self._leads = LeadsClient(client_wrapper=self._client_wrapper)
        return self._leads

    @property
    def students(self):
        if self._students is None:
            from .students.client import StudentsClient

            self._students = StudentsClient(client_wrapper=self._client_wrapper)
        return self._students

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import PaymentsClient

            self._payments = PaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def enrollments(self):
        if self._enrollments is None:
            from .enrollments.client import EnrollmentsClient

            self._enrollments = EnrollmentsClient(client_wrapper=self._client_wrapper)
        return self._enrollments

    @property
    def family_balances(self):
        if self._family_balances is None:
            from .family_balances.client import FamilyBalancesClient

            self._family_balances = FamilyBalancesClient(client_wrapper=self._client_wrapper)
        return self._family_balances

    @property
    def pre_registration_fallout(self):
        if self._pre_registration_fallout is None:
            from .pre_registration_fallout.client import PreRegistrationFalloutClient

            self._pre_registration_fallout = PreRegistrationFalloutClient(client_wrapper=self._client_wrapper)
        return self._pre_registration_fallout

    @property
    def absences(self):
        if self._absences is None:
            from .absences.client import AbsencesClient

            self._absences = AbsencesClient(client_wrapper=self._client_wrapper)
        return self._absences

    @property
    def waitlist(self):
        if self._waitlist is None:
            from .waitlist.client import WaitlistClient

            self._waitlist = WaitlistClient(client_wrapper=self._client_wrapper)
        return self._waitlist

    @property
    def billing_plans(self):
        if self._billing_plans is None:
            from .billing_plans.client import BillingPlansClient

            self._billing_plans = BillingPlansClient(client_wrapper=self._client_wrapper)
        return self._billing_plans

    @property
    def spaces(self):
        if self._spaces is None:
            from .spaces.client import SpacesClient

            self._spaces = SpacesClient(client_wrapper=self._client_wrapper)
        return self._spaces

    @property
    def enrollment_tracker(self):
        if self._enrollment_tracker is None:
            from .enrollment_tracker.client import EnrollmentTrackerClient

            self._enrollment_tracker = EnrollmentTrackerClient(client_wrapper=self._client_wrapper)
        return self._enrollment_tracker

    @property
    def efficiency_ratios(self):
        if self._efficiency_ratios is None:
            from .efficiency_ratios.client import EfficiencyRatiosClient

            self._efficiency_ratios = EfficiencyRatiosClient(client_wrapper=self._client_wrapper)
        return self._efficiency_ratios

    @property
    def procare_messages(self):
        if self._procare_messages is None:
            from .procare_messages.client import ProcareMessagesClient

            self._procare_messages = ProcareMessagesClient(client_wrapper=self._client_wrapper)
        return self._procare_messages

    @property
    def attendances(self):
        if self._attendances is None:
            from .attendances.client import AttendancesClient

            self._attendances = AttendancesClient(client_wrapper=self._client_wrapper)
        return self._attendances

    @property
    def billing_attendance_audits(self):
        if self._billing_attendance_audits is None:
            from .billing_attendance_audits.client import BillingAttendanceAuditsClient

            self._billing_attendance_audits = BillingAttendanceAuditsClient(client_wrapper=self._client_wrapper)
        return self._billing_attendance_audits

    @property
    def classroom_attendance(self):
        if self._classroom_attendance is None:
            from .classroom_attendance.client import ClassroomAttendanceClient

            self._classroom_attendance = ClassroomAttendanceClient(client_wrapper=self._client_wrapper)
        return self._classroom_attendance

    @property
    def activities_summary(self):
        if self._activities_summary is None:
            from .activities_summary.client import ActivitiesSummaryClient

            self._activities_summary = ActivitiesSummaryClient(client_wrapper=self._client_wrapper)
        return self._activities_summary

    @property
    def activity_details(self):
        if self._activity_details is None:
            from .activity_details.client import ActivityDetailsClient

            self._activity_details = ActivityDetailsClient(client_wrapper=self._client_wrapper)
        return self._activity_details

    @property
    def data_refresh(self):
        if self._data_refresh is None:
            from .data_refresh.client import DataRefreshClient

            self._data_refresh = DataRefreshClient(client_wrapper=self._client_wrapper)
        return self._data_refresh

    @property
    def sibling_discounts(self):
        if self._sibling_discounts is None:
            from .sibling_discounts.client import SiblingDiscountsClient

            self._sibling_discounts = SiblingDiscountsClient(client_wrapper=self._client_wrapper)
        return self._sibling_discounts

    @property
    def new_start_tracker(self):
        if self._new_start_tracker is None:
            from .new_start_tracker.client import NewStartTrackerClient

            self._new_start_tracker = NewStartTrackerClient(client_wrapper=self._client_wrapper)
        return self._new_start_tracker

    @property
    def withdrawal_tracker(self):
        if self._withdrawal_tracker is None:
            from .withdrawal_tracker.client import WithdrawalTrackerClient

            self._withdrawal_tracker = WithdrawalTrackerClient(client_wrapper=self._client_wrapper)
        return self._withdrawal_tracker

    @property
    def transition_tracker(self):
        if self._transition_tracker is None:
            from .transition_tracker.client import TransitionTrackerClient

            self._transition_tracker = TransitionTrackerClient(client_wrapper=self._client_wrapper)
        return self._transition_tracker

    @property
    def gusto_companies(self):
        if self._gusto_companies is None:
            from .gusto_companies.client import GustoCompaniesClient

            self._gusto_companies = GustoCompaniesClient(client_wrapper=self._client_wrapper)
        return self._gusto_companies

    @property
    def gusto_employees(self):
        if self._gusto_employees is None:
            from .gusto_employees.client import GustoEmployeesClient

            self._gusto_employees = GustoEmployeesClient(client_wrapper=self._client_wrapper)
        return self._gusto_employees

    @property
    def gusto_contractors(self):
        if self._gusto_contractors is None:
            from .gusto_contractors.client import GustoContractorsClient

            self._gusto_contractors = GustoContractorsClient(client_wrapper=self._client_wrapper)
        return self._gusto_contractors

    @property
    def gusto_payrolls(self):
        if self._gusto_payrolls is None:
            from .gusto_payrolls.client import GustoPayrollsClient

            self._gusto_payrolls = GustoPayrollsClient(client_wrapper=self._client_wrapper)
        return self._gusto_payrolls

    @property
    def procare_staff(self):
        if self._procare_staff is None:
            from .procare_staff.client import ProcareStaffClient

            self._procare_staff = ProcareStaffClient(client_wrapper=self._client_wrapper)
        return self._procare_staff


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    host : typing.Optional[str]
        Server URL variable for 'host'. Defaults to 'api.example.com'.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        host: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        if host is not None:
            _host = host if host is not None else "api.example.com"
            base_url = "https://{host}/primula/api/v3".format(host=_host)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._schools: typing.Optional[AsyncSchoolsClient] = None
        self._companies: typing.Optional[AsyncCompaniesClient] = None
        self._rooms: typing.Optional[AsyncRoomsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._leads: typing.Optional[AsyncLeadsClient] = None
        self._students: typing.Optional[AsyncStudentsClient] = None
        self._payments: typing.Optional[AsyncPaymentsClient] = None
        self._enrollments: typing.Optional[AsyncEnrollmentsClient] = None
        self._family_balances: typing.Optional[AsyncFamilyBalancesClient] = None
        self._pre_registration_fallout: typing.Optional[AsyncPreRegistrationFalloutClient] = None
        self._absences: typing.Optional[AsyncAbsencesClient] = None
        self._waitlist: typing.Optional[AsyncWaitlistClient] = None
        self._billing_plans: typing.Optional[AsyncBillingPlansClient] = None
        self._spaces: typing.Optional[AsyncSpacesClient] = None
        self._enrollment_tracker: typing.Optional[AsyncEnrollmentTrackerClient] = None
        self._efficiency_ratios: typing.Optional[AsyncEfficiencyRatiosClient] = None
        self._procare_messages: typing.Optional[AsyncProcareMessagesClient] = None
        self._attendances: typing.Optional[AsyncAttendancesClient] = None
        self._billing_attendance_audits: typing.Optional[AsyncBillingAttendanceAuditsClient] = None
        self._classroom_attendance: typing.Optional[AsyncClassroomAttendanceClient] = None
        self._activities_summary: typing.Optional[AsyncActivitiesSummaryClient] = None
        self._activity_details: typing.Optional[AsyncActivityDetailsClient] = None
        self._data_refresh: typing.Optional[AsyncDataRefreshClient] = None
        self._sibling_discounts: typing.Optional[AsyncSiblingDiscountsClient] = None
        self._new_start_tracker: typing.Optional[AsyncNewStartTrackerClient] = None
        self._withdrawal_tracker: typing.Optional[AsyncWithdrawalTrackerClient] = None
        self._transition_tracker: typing.Optional[AsyncTransitionTrackerClient] = None
        self._gusto_companies: typing.Optional[AsyncGustoCompaniesClient] = None
        self._gusto_employees: typing.Optional[AsyncGustoEmployeesClient] = None
        self._gusto_contractors: typing.Optional[AsyncGustoContractorsClient] = None
        self._gusto_payrolls: typing.Optional[AsyncGustoPayrollsClient] = None
        self._procare_staff: typing.Optional[AsyncProcareStaffClient] = None

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def schools(self):
        if self._schools is None:
            from .schools.client import AsyncSchoolsClient

            self._schools = AsyncSchoolsClient(client_wrapper=self._client_wrapper)
        return self._schools

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import AsyncCompaniesClient

            self._companies = AsyncCompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def rooms(self):
        if self._rooms is None:
            from .rooms.client import AsyncRoomsClient

            self._rooms = AsyncRoomsClient(client_wrapper=self._client_wrapper)
        return self._rooms

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def leads(self):
        if self._leads is None:
            from .leads.client import AsyncLeadsClient

            self._leads = AsyncLeadsClient(client_wrapper=self._client_wrapper)
        return self._leads

    @property
    def students(self):
        if self._students is None:
            from .students.client import AsyncStudentsClient

            self._students = AsyncStudentsClient(client_wrapper=self._client_wrapper)
        return self._students

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import AsyncPaymentsClient

            self._payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def enrollments(self):
        if self._enrollments is None:
            from .enrollments.client import AsyncEnrollmentsClient

            self._enrollments = AsyncEnrollmentsClient(client_wrapper=self._client_wrapper)
        return self._enrollments

    @property
    def family_balances(self):
        if self._family_balances is None:
            from .family_balances.client import AsyncFamilyBalancesClient

            self._family_balances = AsyncFamilyBalancesClient(client_wrapper=self._client_wrapper)
        return self._family_balances

    @property
    def pre_registration_fallout(self):
        if self._pre_registration_fallout is None:
            from .pre_registration_fallout.client import AsyncPreRegistrationFalloutClient

            self._pre_registration_fallout = AsyncPreRegistrationFalloutClient(client_wrapper=self._client_wrapper)
        return self._pre_registration_fallout

    @property
    def absences(self):
        if self._absences is None:
            from .absences.client import AsyncAbsencesClient

            self._absences = AsyncAbsencesClient(client_wrapper=self._client_wrapper)
        return self._absences

    @property
    def waitlist(self):
        if self._waitlist is None:
            from .waitlist.client import AsyncWaitlistClient

            self._waitlist = AsyncWaitlistClient(client_wrapper=self._client_wrapper)
        return self._waitlist

    @property
    def billing_plans(self):
        if self._billing_plans is None:
            from .billing_plans.client import AsyncBillingPlansClient

            self._billing_plans = AsyncBillingPlansClient(client_wrapper=self._client_wrapper)
        return self._billing_plans

    @property
    def spaces(self):
        if self._spaces is None:
            from .spaces.client import AsyncSpacesClient

            self._spaces = AsyncSpacesClient(client_wrapper=self._client_wrapper)
        return self._spaces

    @property
    def enrollment_tracker(self):
        if self._enrollment_tracker is None:
            from .enrollment_tracker.client import AsyncEnrollmentTrackerClient

            self._enrollment_tracker = AsyncEnrollmentTrackerClient(client_wrapper=self._client_wrapper)
        return self._enrollment_tracker

    @property
    def efficiency_ratios(self):
        if self._efficiency_ratios is None:
            from .efficiency_ratios.client import AsyncEfficiencyRatiosClient

            self._efficiency_ratios = AsyncEfficiencyRatiosClient(client_wrapper=self._client_wrapper)
        return self._efficiency_ratios

    @property
    def procare_messages(self):
        if self._procare_messages is None:
            from .procare_messages.client import AsyncProcareMessagesClient

            self._procare_messages = AsyncProcareMessagesClient(client_wrapper=self._client_wrapper)
        return self._procare_messages

    @property
    def attendances(self):
        if self._attendances is None:
            from .attendances.client import AsyncAttendancesClient

            self._attendances = AsyncAttendancesClient(client_wrapper=self._client_wrapper)
        return self._attendances

    @property
    def billing_attendance_audits(self):
        if self._billing_attendance_audits is None:
            from .billing_attendance_audits.client import AsyncBillingAttendanceAuditsClient

            self._billing_attendance_audits = AsyncBillingAttendanceAuditsClient(client_wrapper=self._client_wrapper)
        return self._billing_attendance_audits

    @property
    def classroom_attendance(self):
        if self._classroom_attendance is None:
            from .classroom_attendance.client import AsyncClassroomAttendanceClient

            self._classroom_attendance = AsyncClassroomAttendanceClient(client_wrapper=self._client_wrapper)
        return self._classroom_attendance

    @property
    def activities_summary(self):
        if self._activities_summary is None:
            from .activities_summary.client import AsyncActivitiesSummaryClient

            self._activities_summary = AsyncActivitiesSummaryClient(client_wrapper=self._client_wrapper)
        return self._activities_summary

    @property
    def activity_details(self):
        if self._activity_details is None:
            from .activity_details.client import AsyncActivityDetailsClient

            self._activity_details = AsyncActivityDetailsClient(client_wrapper=self._client_wrapper)
        return self._activity_details

    @property
    def data_refresh(self):
        if self._data_refresh is None:
            from .data_refresh.client import AsyncDataRefreshClient

            self._data_refresh = AsyncDataRefreshClient(client_wrapper=self._client_wrapper)
        return self._data_refresh

    @property
    def sibling_discounts(self):
        if self._sibling_discounts is None:
            from .sibling_discounts.client import AsyncSiblingDiscountsClient

            self._sibling_discounts = AsyncSiblingDiscountsClient(client_wrapper=self._client_wrapper)
        return self._sibling_discounts

    @property
    def new_start_tracker(self):
        if self._new_start_tracker is None:
            from .new_start_tracker.client import AsyncNewStartTrackerClient

            self._new_start_tracker = AsyncNewStartTrackerClient(client_wrapper=self._client_wrapper)
        return self._new_start_tracker

    @property
    def withdrawal_tracker(self):
        if self._withdrawal_tracker is None:
            from .withdrawal_tracker.client import AsyncWithdrawalTrackerClient

            self._withdrawal_tracker = AsyncWithdrawalTrackerClient(client_wrapper=self._client_wrapper)
        return self._withdrawal_tracker

    @property
    def transition_tracker(self):
        if self._transition_tracker is None:
            from .transition_tracker.client import AsyncTransitionTrackerClient

            self._transition_tracker = AsyncTransitionTrackerClient(client_wrapper=self._client_wrapper)
        return self._transition_tracker

    @property
    def gusto_companies(self):
        if self._gusto_companies is None:
            from .gusto_companies.client import AsyncGustoCompaniesClient

            self._gusto_companies = AsyncGustoCompaniesClient(client_wrapper=self._client_wrapper)
        return self._gusto_companies

    @property
    def gusto_employees(self):
        if self._gusto_employees is None:
            from .gusto_employees.client import AsyncGustoEmployeesClient

            self._gusto_employees = AsyncGustoEmployeesClient(client_wrapper=self._client_wrapper)
        return self._gusto_employees

    @property
    def gusto_contractors(self):
        if self._gusto_contractors is None:
            from .gusto_contractors.client import AsyncGustoContractorsClient

            self._gusto_contractors = AsyncGustoContractorsClient(client_wrapper=self._client_wrapper)
        return self._gusto_contractors

    @property
    def gusto_payrolls(self):
        if self._gusto_payrolls is None:
            from .gusto_payrolls.client import AsyncGustoPayrollsClient

            self._gusto_payrolls = AsyncGustoPayrollsClient(client_wrapper=self._client_wrapper)
        return self._gusto_payrolls

    @property
    def procare_staff(self):
        if self._procare_staff is None:
            from .procare_staff.client import AsyncProcareStaffClient

            self._procare_staff = AsyncProcareStaffClient(client_wrapper=self._client_wrapper)
        return self._procare_staff


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
