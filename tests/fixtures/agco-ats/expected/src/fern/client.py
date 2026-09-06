

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .activities.client import ActivitiesClient, AsyncActivitiesClient
    from .activityruns.client import ActivityrunsClient, AsyncActivityrunsClient
    from .aftermarketservices.client import AftermarketservicesClient, AsyncAftermarketservicesClient
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .authorizationcategories.client import AsyncAuthorizationcategoriesClient, AuthorizationcategoriesClient
    from .authorizationcodedefinitions.client import (
        AsyncAuthorizationcodedefinitionsClient,
        AuthorizationcodedefinitionsClient,
    )
    from .authorizationcodes.client import AsyncAuthorizationcodesClient, AuthorizationcodesClient
    from .authorizationcontactinformation.client import (
        AsyncAuthorizationcontactinformationClient,
        AuthorizationcontactinformationClient,
    )
    from .brands.client import AsyncBrandsClient, BrandsClient
    from .bundles.client import AsyncBundlesClient, BundlesClient
    from .clients.client import AsyncClientsClient, ClientsClient
    from .contentdefinitions.client import AsyncContentdefinitionsClient, ContentdefinitionsClient
    from .contentrelease.client import AsyncContentreleaseClient, ContentreleaseClient
    from .contentsubmissions.client import AsyncContentsubmissionsClient, ContentsubmissionsClient
    from .contentsubmissiontypes.client import AsyncContentsubmissiontypesClient, ContentsubmissiontypesClient
    from .dealerbycountry.client import AsyncDealerbycountryClient, DealerbycountryClient
    from .dealers.client import AsyncDealersClient, DealersClient
    from .files.client import AsyncFilesClient, FilesClient
    from .fileuploadindexfields.client import AsyncFileuploadindexfieldsClient, FileuploadindexfieldsClient
    from .fileuploads.client import AsyncFileuploadsClient, FileuploadsClient
    from .fileuploadtypes.client import AsyncFileuploadtypesClient, FileuploadtypesClient
    from .globalimagecategories.client import AsyncGlobalimagecategoriesClient, GlobalimagecategoriesClient
    from .globalimages.client import AsyncGlobalimagesClient, GlobalimagesClient
    from .jobruns.client import AsyncJobrunsClient, JobrunsClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .languages.client import AsyncLanguagesClient, LanguagesClient
    from .licenseactivations.client import AsyncLicenseactivationsClient, LicenseactivationsClient
    from .licenses.client import AsyncLicensesClient, LicensesClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .packagereports.client import AsyncPackagereportsClient, PackagereportsClient
    from .packages.client import AsyncPackagesClient, PackagesClient
    from .packagetypes.client import AsyncPackagetypesClient, PackagetypesClient
    from .packagetypetobundles.client import AsyncPackagetypetobundlesClient, PackagetypetobundlesClient
    from .permissions.client import AsyncPermissionsClient, PermissionsClient
    from .prioritypackages.client import AsyncPrioritypackagesClient, PrioritypackagesClient
    from .release.client import AsyncReleaseClient, ReleaseClient
    from .reporting.client import AsyncReportingClient, ReportingClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .steps.client import AsyncStepsClient, StepsClient
    from .stringdefinitions.client import AsyncStringdefinitionsClient, StringdefinitionsClient
    from .stringtranslations.client import AsyncStringtranslationsClient, StringtranslationsClient
    from .translationkeys.client import AsyncTranslationkeysClient, TranslationkeysClient
    from .translationrequests.client import AsyncTranslationrequestsClient, TranslationrequestsClient
    from .translationsets.client import AsyncTranslationsetsClient, TranslationsetsClient
    from .updategroupclientrelationships.client import (
        AsyncUpdategroupclientrelationshipsClient,
        UpdategroupclientrelationshipsClient,
    )
    from .updategroups.client import AsyncUpdategroupsClient, UpdategroupsClient
    from .updategroupsubscriptions.client import AsyncUpdategroupsubscriptionsClient, UpdategroupsubscriptionsClient
    from .updatesystem.client import AsyncUpdatesystemClient, UpdatesystemClient
    from .usercontentdefinitions.client import AsyncUsercontentdefinitionsClient, UsercontentdefinitionsClient
    from .userpermissions.client import AsyncUserpermissionsClient, UserpermissionsClient
    from .users.client import AsyncUsersClient, UsersClient
    from .voucherhistory.client import AsyncVoucherhistoryClient, VoucherhistoryClient
    from .vouchers.client import AsyncVouchersClient, VouchersClient


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._aftermarketservices: typing.Optional[AftermarketservicesClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._authorizationcategories: typing.Optional[AuthorizationcategoriesClient] = None
        self._authorizationcodedefinitions: typing.Optional[AuthorizationcodedefinitionsClient] = None
        self._authorizationcodes: typing.Optional[AuthorizationcodesClient] = None
        self._authorizationcontactinformation: typing.Optional[AuthorizationcontactinformationClient] = None
        self._brands: typing.Optional[BrandsClient] = None
        self._bundles: typing.Optional[BundlesClient] = None
        self._clients: typing.Optional[ClientsClient] = None
        self._updatesystem: typing.Optional[UpdatesystemClient] = None
        self._packagereports: typing.Optional[PackagereportsClient] = None
        self._contentdefinitions: typing.Optional[ContentdefinitionsClient] = None
        self._contentrelease: typing.Optional[ContentreleaseClient] = None
        self._contentsubmissions: typing.Optional[ContentsubmissionsClient] = None
        self._contentsubmissiontypes: typing.Optional[ContentsubmissiontypesClient] = None
        self._dealerbycountry: typing.Optional[DealerbycountryClient] = None
        self._dealers: typing.Optional[DealersClient] = None
        self._fileuploadindexfields: typing.Optional[FileuploadindexfieldsClient] = None
        self._fileuploadtypes: typing.Optional[FileuploadtypesClient] = None
        self._fileuploads: typing.Optional[FileuploadsClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._globalimagecategories: typing.Optional[GlobalimagecategoriesClient] = None
        self._globalimages: typing.Optional[GlobalimagesClient] = None
        self._languages: typing.Optional[LanguagesClient] = None
        self._licenseactivations: typing.Optional[LicenseactivationsClient] = None
        self._licenses: typing.Optional[LicensesClient] = None
        self._logs: typing.Optional[LogsClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._packagetypes: typing.Optional[PackagetypesClient] = None
        self._packagetypetobundles: typing.Optional[PackagetypetobundlesClient] = None
        self._packages: typing.Optional[PackagesClient] = None
        self._permissions: typing.Optional[PermissionsClient] = None
        self._prioritypackages: typing.Optional[PrioritypackagesClient] = None
        self._release: typing.Optional[ReleaseClient] = None
        self._reporting: typing.Optional[ReportingClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._userpermissions: typing.Optional[UserpermissionsClient] = None
        self._stringdefinitions: typing.Optional[StringdefinitionsClient] = None
        self._stringtranslations: typing.Optional[StringtranslationsClient] = None
        self._translationkeys: typing.Optional[TranslationkeysClient] = None
        self._translationrequests: typing.Optional[TranslationrequestsClient] = None
        self._translationsets: typing.Optional[TranslationsetsClient] = None
        self._updategroupclientrelationships: typing.Optional[UpdategroupclientrelationshipsClient] = None
        self._updategroupsubscriptions: typing.Optional[UpdategroupsubscriptionsClient] = None
        self._updategroups: typing.Optional[UpdategroupsClient] = None
        self._usercontentdefinitions: typing.Optional[UsercontentdefinitionsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._voucherhistory: typing.Optional[VoucherhistoryClient] = None
        self._vouchers: typing.Optional[VouchersClient] = None
        self._activities: typing.Optional[ActivitiesClient] = None
        self._activityruns: typing.Optional[ActivityrunsClient] = None
        self._agents: typing.Optional[AgentsClient] = None
        self._jobruns: typing.Optional[JobrunsClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._steps: typing.Optional[StepsClient] = None

    @property
    def aftermarketservices(self):
        if self._aftermarketservices is None:
            from .aftermarketservices.client import AftermarketservicesClient

            self._aftermarketservices = AftermarketservicesClient(client_wrapper=self._client_wrapper)
        return self._aftermarketservices

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def authorizationcategories(self):
        if self._authorizationcategories is None:
            from .authorizationcategories.client import AuthorizationcategoriesClient

            self._authorizationcategories = AuthorizationcategoriesClient(client_wrapper=self._client_wrapper)
        return self._authorizationcategories

    @property
    def authorizationcodedefinitions(self):
        if self._authorizationcodedefinitions is None:
            from .authorizationcodedefinitions.client import AuthorizationcodedefinitionsClient

            self._authorizationcodedefinitions = AuthorizationcodedefinitionsClient(client_wrapper=self._client_wrapper)
        return self._authorizationcodedefinitions

    @property
    def authorizationcodes(self):
        if self._authorizationcodes is None:
            from .authorizationcodes.client import AuthorizationcodesClient

            self._authorizationcodes = AuthorizationcodesClient(client_wrapper=self._client_wrapper)
        return self._authorizationcodes

    @property
    def authorizationcontactinformation(self):
        if self._authorizationcontactinformation is None:
            from .authorizationcontactinformation.client import AuthorizationcontactinformationClient

            self._authorizationcontactinformation = AuthorizationcontactinformationClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorizationcontactinformation

    @property
    def brands(self):
        if self._brands is None:
            from .brands.client import BrandsClient

            self._brands = BrandsClient(client_wrapper=self._client_wrapper)
        return self._brands

    @property
    def bundles(self):
        if self._bundles is None:
            from .bundles.client import BundlesClient

            self._bundles = BundlesClient(client_wrapper=self._client_wrapper)
        return self._bundles

    @property
    def clients(self):
        if self._clients is None:
            from .clients.client import ClientsClient

            self._clients = ClientsClient(client_wrapper=self._client_wrapper)
        return self._clients

    @property
    def updatesystem(self):
        if self._updatesystem is None:
            from .updatesystem.client import UpdatesystemClient

            self._updatesystem = UpdatesystemClient(client_wrapper=self._client_wrapper)
        return self._updatesystem

    @property
    def packagereports(self):
        if self._packagereports is None:
            from .packagereports.client import PackagereportsClient

            self._packagereports = PackagereportsClient(client_wrapper=self._client_wrapper)
        return self._packagereports

    @property
    def contentdefinitions(self):
        if self._contentdefinitions is None:
            from .contentdefinitions.client import ContentdefinitionsClient

            self._contentdefinitions = ContentdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._contentdefinitions

    @property
    def contentrelease(self):
        if self._contentrelease is None:
            from .contentrelease.client import ContentreleaseClient

            self._contentrelease = ContentreleaseClient(client_wrapper=self._client_wrapper)
        return self._contentrelease

    @property
    def contentsubmissions(self):
        if self._contentsubmissions is None:
            from .contentsubmissions.client import ContentsubmissionsClient

            self._contentsubmissions = ContentsubmissionsClient(client_wrapper=self._client_wrapper)
        return self._contentsubmissions

    @property
    def contentsubmissiontypes(self):
        if self._contentsubmissiontypes is None:
            from .contentsubmissiontypes.client import ContentsubmissiontypesClient

            self._contentsubmissiontypes = ContentsubmissiontypesClient(client_wrapper=self._client_wrapper)
        return self._contentsubmissiontypes

    @property
    def dealerbycountry(self):
        if self._dealerbycountry is None:
            from .dealerbycountry.client import DealerbycountryClient

            self._dealerbycountry = DealerbycountryClient(client_wrapper=self._client_wrapper)
        return self._dealerbycountry

    @property
    def dealers(self):
        if self._dealers is None:
            from .dealers.client import DealersClient

            self._dealers = DealersClient(client_wrapper=self._client_wrapper)
        return self._dealers

    @property
    def fileuploadindexfields(self):
        if self._fileuploadindexfields is None:
            from .fileuploadindexfields.client import FileuploadindexfieldsClient

            self._fileuploadindexfields = FileuploadindexfieldsClient(client_wrapper=self._client_wrapper)
        return self._fileuploadindexfields

    @property
    def fileuploadtypes(self):
        if self._fileuploadtypes is None:
            from .fileuploadtypes.client import FileuploadtypesClient

            self._fileuploadtypes = FileuploadtypesClient(client_wrapper=self._client_wrapper)
        return self._fileuploadtypes

    @property
    def fileuploads(self):
        if self._fileuploads is None:
            from .fileuploads.client import FileuploadsClient

            self._fileuploads = FileuploadsClient(client_wrapper=self._client_wrapper)
        return self._fileuploads

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def globalimagecategories(self):
        if self._globalimagecategories is None:
            from .globalimagecategories.client import GlobalimagecategoriesClient

            self._globalimagecategories = GlobalimagecategoriesClient(client_wrapper=self._client_wrapper)
        return self._globalimagecategories

    @property
    def globalimages(self):
        if self._globalimages is None:
            from .globalimages.client import GlobalimagesClient

            self._globalimages = GlobalimagesClient(client_wrapper=self._client_wrapper)
        return self._globalimages

    @property
    def languages(self):
        if self._languages is None:
            from .languages.client import LanguagesClient

            self._languages = LanguagesClient(client_wrapper=self._client_wrapper)
        return self._languages

    @property
    def licenseactivations(self):
        if self._licenseactivations is None:
            from .licenseactivations.client import LicenseactivationsClient

            self._licenseactivations = LicenseactivationsClient(client_wrapper=self._client_wrapper)
        return self._licenseactivations

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import LicensesClient

            self._licenses = LicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import LogsClient

            self._logs = LogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def packagetypes(self):
        if self._packagetypes is None:
            from .packagetypes.client import PackagetypesClient

            self._packagetypes = PackagetypesClient(client_wrapper=self._client_wrapper)
        return self._packagetypes

    @property
    def packagetypetobundles(self):
        if self._packagetypetobundles is None:
            from .packagetypetobundles.client import PackagetypetobundlesClient

            self._packagetypetobundles = PackagetypetobundlesClient(client_wrapper=self._client_wrapper)
        return self._packagetypetobundles

    @property
    def packages(self):
        if self._packages is None:
            from .packages.client import PackagesClient

            self._packages = PackagesClient(client_wrapper=self._client_wrapper)
        return self._packages

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import PermissionsClient

            self._permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def prioritypackages(self):
        if self._prioritypackages is None:
            from .prioritypackages.client import PrioritypackagesClient

            self._prioritypackages = PrioritypackagesClient(client_wrapper=self._client_wrapper)
        return self._prioritypackages

    @property
    def release(self):
        if self._release is None:
            from .release.client import ReleaseClient

            self._release = ReleaseClient(client_wrapper=self._client_wrapper)
        return self._release

    @property
    def reporting(self):
        if self._reporting is None:
            from .reporting.client import ReportingClient

            self._reporting = ReportingClient(client_wrapper=self._client_wrapper)
        return self._reporting

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def userpermissions(self):
        if self._userpermissions is None:
            from .userpermissions.client import UserpermissionsClient

            self._userpermissions = UserpermissionsClient(client_wrapper=self._client_wrapper)
        return self._userpermissions

    @property
    def stringdefinitions(self):
        if self._stringdefinitions is None:
            from .stringdefinitions.client import StringdefinitionsClient

            self._stringdefinitions = StringdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._stringdefinitions

    @property
    def stringtranslations(self):
        if self._stringtranslations is None:
            from .stringtranslations.client import StringtranslationsClient

            self._stringtranslations = StringtranslationsClient(client_wrapper=self._client_wrapper)
        return self._stringtranslations

    @property
    def translationkeys(self):
        if self._translationkeys is None:
            from .translationkeys.client import TranslationkeysClient

            self._translationkeys = TranslationkeysClient(client_wrapper=self._client_wrapper)
        return self._translationkeys

    @property
    def translationrequests(self):
        if self._translationrequests is None:
            from .translationrequests.client import TranslationrequestsClient

            self._translationrequests = TranslationrequestsClient(client_wrapper=self._client_wrapper)
        return self._translationrequests

    @property
    def translationsets(self):
        if self._translationsets is None:
            from .translationsets.client import TranslationsetsClient

            self._translationsets = TranslationsetsClient(client_wrapper=self._client_wrapper)
        return self._translationsets

    @property
    def updategroupclientrelationships(self):
        if self._updategroupclientrelationships is None:
            from .updategroupclientrelationships.client import UpdategroupclientrelationshipsClient

            self._updategroupclientrelationships = UpdategroupclientrelationshipsClient(
                client_wrapper=self._client_wrapper
            )
        return self._updategroupclientrelationships

    @property
    def updategroupsubscriptions(self):
        if self._updategroupsubscriptions is None:
            from .updategroupsubscriptions.client import UpdategroupsubscriptionsClient

            self._updategroupsubscriptions = UpdategroupsubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._updategroupsubscriptions

    @property
    def updategroups(self):
        if self._updategroups is None:
            from .updategroups.client import UpdategroupsClient

            self._updategroups = UpdategroupsClient(client_wrapper=self._client_wrapper)
        return self._updategroups

    @property
    def usercontentdefinitions(self):
        if self._usercontentdefinitions is None:
            from .usercontentdefinitions.client import UsercontentdefinitionsClient

            self._usercontentdefinitions = UsercontentdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._usercontentdefinitions

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def voucherhistory(self):
        if self._voucherhistory is None:
            from .voucherhistory.client import VoucherhistoryClient

            self._voucherhistory = VoucherhistoryClient(client_wrapper=self._client_wrapper)
        return self._voucherhistory

    @property
    def vouchers(self):
        if self._vouchers is None:
            from .vouchers.client import VouchersClient

            self._vouchers = VouchersClient(client_wrapper=self._client_wrapper)
        return self._vouchers

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import ActivitiesClient

            self._activities = ActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def activityruns(self):
        if self._activityruns is None:
            from .activityruns.client import ActivityrunsClient

            self._activityruns = ActivityrunsClient(client_wrapper=self._client_wrapper)
        return self._activityruns

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def jobruns(self):
        if self._jobruns is None:
            from .jobruns.client import JobrunsClient

            self._jobruns = JobrunsClient(client_wrapper=self._client_wrapper)
        return self._jobruns

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def steps(self):
        if self._steps is None:
            from .steps.client import StepsClient

            self._steps = StepsClient(client_wrapper=self._client_wrapper)
        return self._steps


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

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
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
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._aftermarketservices: typing.Optional[AsyncAftermarketservicesClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._authorizationcategories: typing.Optional[AsyncAuthorizationcategoriesClient] = None
        self._authorizationcodedefinitions: typing.Optional[AsyncAuthorizationcodedefinitionsClient] = None
        self._authorizationcodes: typing.Optional[AsyncAuthorizationcodesClient] = None
        self._authorizationcontactinformation: typing.Optional[AsyncAuthorizationcontactinformationClient] = None
        self._brands: typing.Optional[AsyncBrandsClient] = None
        self._bundles: typing.Optional[AsyncBundlesClient] = None
        self._clients: typing.Optional[AsyncClientsClient] = None
        self._updatesystem: typing.Optional[AsyncUpdatesystemClient] = None
        self._packagereports: typing.Optional[AsyncPackagereportsClient] = None
        self._contentdefinitions: typing.Optional[AsyncContentdefinitionsClient] = None
        self._contentrelease: typing.Optional[AsyncContentreleaseClient] = None
        self._contentsubmissions: typing.Optional[AsyncContentsubmissionsClient] = None
        self._contentsubmissiontypes: typing.Optional[AsyncContentsubmissiontypesClient] = None
        self._dealerbycountry: typing.Optional[AsyncDealerbycountryClient] = None
        self._dealers: typing.Optional[AsyncDealersClient] = None
        self._fileuploadindexfields: typing.Optional[AsyncFileuploadindexfieldsClient] = None
        self._fileuploadtypes: typing.Optional[AsyncFileuploadtypesClient] = None
        self._fileuploads: typing.Optional[AsyncFileuploadsClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._globalimagecategories: typing.Optional[AsyncGlobalimagecategoriesClient] = None
        self._globalimages: typing.Optional[AsyncGlobalimagesClient] = None
        self._languages: typing.Optional[AsyncLanguagesClient] = None
        self._licenseactivations: typing.Optional[AsyncLicenseactivationsClient] = None
        self._licenses: typing.Optional[AsyncLicensesClient] = None
        self._logs: typing.Optional[AsyncLogsClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._packagetypes: typing.Optional[AsyncPackagetypesClient] = None
        self._packagetypetobundles: typing.Optional[AsyncPackagetypetobundlesClient] = None
        self._packages: typing.Optional[AsyncPackagesClient] = None
        self._permissions: typing.Optional[AsyncPermissionsClient] = None
        self._prioritypackages: typing.Optional[AsyncPrioritypackagesClient] = None
        self._release: typing.Optional[AsyncReleaseClient] = None
        self._reporting: typing.Optional[AsyncReportingClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._userpermissions: typing.Optional[AsyncUserpermissionsClient] = None
        self._stringdefinitions: typing.Optional[AsyncStringdefinitionsClient] = None
        self._stringtranslations: typing.Optional[AsyncStringtranslationsClient] = None
        self._translationkeys: typing.Optional[AsyncTranslationkeysClient] = None
        self._translationrequests: typing.Optional[AsyncTranslationrequestsClient] = None
        self._translationsets: typing.Optional[AsyncTranslationsetsClient] = None
        self._updategroupclientrelationships: typing.Optional[AsyncUpdategroupclientrelationshipsClient] = None
        self._updategroupsubscriptions: typing.Optional[AsyncUpdategroupsubscriptionsClient] = None
        self._updategroups: typing.Optional[AsyncUpdategroupsClient] = None
        self._usercontentdefinitions: typing.Optional[AsyncUsercontentdefinitionsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._voucherhistory: typing.Optional[AsyncVoucherhistoryClient] = None
        self._vouchers: typing.Optional[AsyncVouchersClient] = None
        self._activities: typing.Optional[AsyncActivitiesClient] = None
        self._activityruns: typing.Optional[AsyncActivityrunsClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None
        self._jobruns: typing.Optional[AsyncJobrunsClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._steps: typing.Optional[AsyncStepsClient] = None

    @property
    def aftermarketservices(self):
        if self._aftermarketservices is None:
            from .aftermarketservices.client import AsyncAftermarketservicesClient

            self._aftermarketservices = AsyncAftermarketservicesClient(client_wrapper=self._client_wrapper)
        return self._aftermarketservices

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def authorizationcategories(self):
        if self._authorizationcategories is None:
            from .authorizationcategories.client import AsyncAuthorizationcategoriesClient

            self._authorizationcategories = AsyncAuthorizationcategoriesClient(client_wrapper=self._client_wrapper)
        return self._authorizationcategories

    @property
    def authorizationcodedefinitions(self):
        if self._authorizationcodedefinitions is None:
            from .authorizationcodedefinitions.client import AsyncAuthorizationcodedefinitionsClient

            self._authorizationcodedefinitions = AsyncAuthorizationcodedefinitionsClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorizationcodedefinitions

    @property
    def authorizationcodes(self):
        if self._authorizationcodes is None:
            from .authorizationcodes.client import AsyncAuthorizationcodesClient

            self._authorizationcodes = AsyncAuthorizationcodesClient(client_wrapper=self._client_wrapper)
        return self._authorizationcodes

    @property
    def authorizationcontactinformation(self):
        if self._authorizationcontactinformation is None:
            from .authorizationcontactinformation.client import AsyncAuthorizationcontactinformationClient

            self._authorizationcontactinformation = AsyncAuthorizationcontactinformationClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorizationcontactinformation

    @property
    def brands(self):
        if self._brands is None:
            from .brands.client import AsyncBrandsClient

            self._brands = AsyncBrandsClient(client_wrapper=self._client_wrapper)
        return self._brands

    @property
    def bundles(self):
        if self._bundles is None:
            from .bundles.client import AsyncBundlesClient

            self._bundles = AsyncBundlesClient(client_wrapper=self._client_wrapper)
        return self._bundles

    @property
    def clients(self):
        if self._clients is None:
            from .clients.client import AsyncClientsClient

            self._clients = AsyncClientsClient(client_wrapper=self._client_wrapper)
        return self._clients

    @property
    def updatesystem(self):
        if self._updatesystem is None:
            from .updatesystem.client import AsyncUpdatesystemClient

            self._updatesystem = AsyncUpdatesystemClient(client_wrapper=self._client_wrapper)
        return self._updatesystem

    @property
    def packagereports(self):
        if self._packagereports is None:
            from .packagereports.client import AsyncPackagereportsClient

            self._packagereports = AsyncPackagereportsClient(client_wrapper=self._client_wrapper)
        return self._packagereports

    @property
    def contentdefinitions(self):
        if self._contentdefinitions is None:
            from .contentdefinitions.client import AsyncContentdefinitionsClient

            self._contentdefinitions = AsyncContentdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._contentdefinitions

    @property
    def contentrelease(self):
        if self._contentrelease is None:
            from .contentrelease.client import AsyncContentreleaseClient

            self._contentrelease = AsyncContentreleaseClient(client_wrapper=self._client_wrapper)
        return self._contentrelease

    @property
    def contentsubmissions(self):
        if self._contentsubmissions is None:
            from .contentsubmissions.client import AsyncContentsubmissionsClient

            self._contentsubmissions = AsyncContentsubmissionsClient(client_wrapper=self._client_wrapper)
        return self._contentsubmissions

    @property
    def contentsubmissiontypes(self):
        if self._contentsubmissiontypes is None:
            from .contentsubmissiontypes.client import AsyncContentsubmissiontypesClient

            self._contentsubmissiontypes = AsyncContentsubmissiontypesClient(client_wrapper=self._client_wrapper)
        return self._contentsubmissiontypes

    @property
    def dealerbycountry(self):
        if self._dealerbycountry is None:
            from .dealerbycountry.client import AsyncDealerbycountryClient

            self._dealerbycountry = AsyncDealerbycountryClient(client_wrapper=self._client_wrapper)
        return self._dealerbycountry

    @property
    def dealers(self):
        if self._dealers is None:
            from .dealers.client import AsyncDealersClient

            self._dealers = AsyncDealersClient(client_wrapper=self._client_wrapper)
        return self._dealers

    @property
    def fileuploadindexfields(self):
        if self._fileuploadindexfields is None:
            from .fileuploadindexfields.client import AsyncFileuploadindexfieldsClient

            self._fileuploadindexfields = AsyncFileuploadindexfieldsClient(client_wrapper=self._client_wrapper)
        return self._fileuploadindexfields

    @property
    def fileuploadtypes(self):
        if self._fileuploadtypes is None:
            from .fileuploadtypes.client import AsyncFileuploadtypesClient

            self._fileuploadtypes = AsyncFileuploadtypesClient(client_wrapper=self._client_wrapper)
        return self._fileuploadtypes

    @property
    def fileuploads(self):
        if self._fileuploads is None:
            from .fileuploads.client import AsyncFileuploadsClient

            self._fileuploads = AsyncFileuploadsClient(client_wrapper=self._client_wrapper)
        return self._fileuploads

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def globalimagecategories(self):
        if self._globalimagecategories is None:
            from .globalimagecategories.client import AsyncGlobalimagecategoriesClient

            self._globalimagecategories = AsyncGlobalimagecategoriesClient(client_wrapper=self._client_wrapper)
        return self._globalimagecategories

    @property
    def globalimages(self):
        if self._globalimages is None:
            from .globalimages.client import AsyncGlobalimagesClient

            self._globalimages = AsyncGlobalimagesClient(client_wrapper=self._client_wrapper)
        return self._globalimages

    @property
    def languages(self):
        if self._languages is None:
            from .languages.client import AsyncLanguagesClient

            self._languages = AsyncLanguagesClient(client_wrapper=self._client_wrapper)
        return self._languages

    @property
    def licenseactivations(self):
        if self._licenseactivations is None:
            from .licenseactivations.client import AsyncLicenseactivationsClient

            self._licenseactivations = AsyncLicenseactivationsClient(client_wrapper=self._client_wrapper)
        return self._licenseactivations

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import AsyncLicensesClient

            self._licenses = AsyncLicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import AsyncLogsClient

            self._logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def packagetypes(self):
        if self._packagetypes is None:
            from .packagetypes.client import AsyncPackagetypesClient

            self._packagetypes = AsyncPackagetypesClient(client_wrapper=self._client_wrapper)
        return self._packagetypes

    @property
    def packagetypetobundles(self):
        if self._packagetypetobundles is None:
            from .packagetypetobundles.client import AsyncPackagetypetobundlesClient

            self._packagetypetobundles = AsyncPackagetypetobundlesClient(client_wrapper=self._client_wrapper)
        return self._packagetypetobundles

    @property
    def packages(self):
        if self._packages is None:
            from .packages.client import AsyncPackagesClient

            self._packages = AsyncPackagesClient(client_wrapper=self._client_wrapper)
        return self._packages

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import AsyncPermissionsClient

            self._permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def prioritypackages(self):
        if self._prioritypackages is None:
            from .prioritypackages.client import AsyncPrioritypackagesClient

            self._prioritypackages = AsyncPrioritypackagesClient(client_wrapper=self._client_wrapper)
        return self._prioritypackages

    @property
    def release(self):
        if self._release is None:
            from .release.client import AsyncReleaseClient

            self._release = AsyncReleaseClient(client_wrapper=self._client_wrapper)
        return self._release

    @property
    def reporting(self):
        if self._reporting is None:
            from .reporting.client import AsyncReportingClient

            self._reporting = AsyncReportingClient(client_wrapper=self._client_wrapper)
        return self._reporting

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def userpermissions(self):
        if self._userpermissions is None:
            from .userpermissions.client import AsyncUserpermissionsClient

            self._userpermissions = AsyncUserpermissionsClient(client_wrapper=self._client_wrapper)
        return self._userpermissions

    @property
    def stringdefinitions(self):
        if self._stringdefinitions is None:
            from .stringdefinitions.client import AsyncStringdefinitionsClient

            self._stringdefinitions = AsyncStringdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._stringdefinitions

    @property
    def stringtranslations(self):
        if self._stringtranslations is None:
            from .stringtranslations.client import AsyncStringtranslationsClient

            self._stringtranslations = AsyncStringtranslationsClient(client_wrapper=self._client_wrapper)
        return self._stringtranslations

    @property
    def translationkeys(self):
        if self._translationkeys is None:
            from .translationkeys.client import AsyncTranslationkeysClient

            self._translationkeys = AsyncTranslationkeysClient(client_wrapper=self._client_wrapper)
        return self._translationkeys

    @property
    def translationrequests(self):
        if self._translationrequests is None:
            from .translationrequests.client import AsyncTranslationrequestsClient

            self._translationrequests = AsyncTranslationrequestsClient(client_wrapper=self._client_wrapper)
        return self._translationrequests

    @property
    def translationsets(self):
        if self._translationsets is None:
            from .translationsets.client import AsyncTranslationsetsClient

            self._translationsets = AsyncTranslationsetsClient(client_wrapper=self._client_wrapper)
        return self._translationsets

    @property
    def updategroupclientrelationships(self):
        if self._updategroupclientrelationships is None:
            from .updategroupclientrelationships.client import AsyncUpdategroupclientrelationshipsClient

            self._updategroupclientrelationships = AsyncUpdategroupclientrelationshipsClient(
                client_wrapper=self._client_wrapper
            )
        return self._updategroupclientrelationships

    @property
    def updategroupsubscriptions(self):
        if self._updategroupsubscriptions is None:
            from .updategroupsubscriptions.client import AsyncUpdategroupsubscriptionsClient

            self._updategroupsubscriptions = AsyncUpdategroupsubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._updategroupsubscriptions

    @property
    def updategroups(self):
        if self._updategroups is None:
            from .updategroups.client import AsyncUpdategroupsClient

            self._updategroups = AsyncUpdategroupsClient(client_wrapper=self._client_wrapper)
        return self._updategroups

    @property
    def usercontentdefinitions(self):
        if self._usercontentdefinitions is None:
            from .usercontentdefinitions.client import AsyncUsercontentdefinitionsClient

            self._usercontentdefinitions = AsyncUsercontentdefinitionsClient(client_wrapper=self._client_wrapper)
        return self._usercontentdefinitions

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def voucherhistory(self):
        if self._voucherhistory is None:
            from .voucherhistory.client import AsyncVoucherhistoryClient

            self._voucherhistory = AsyncVoucherhistoryClient(client_wrapper=self._client_wrapper)
        return self._voucherhistory

    @property
    def vouchers(self):
        if self._vouchers is None:
            from .vouchers.client import AsyncVouchersClient

            self._vouchers = AsyncVouchersClient(client_wrapper=self._client_wrapper)
        return self._vouchers

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import AsyncActivitiesClient

            self._activities = AsyncActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def activityruns(self):
        if self._activityruns is None:
            from .activityruns.client import AsyncActivityrunsClient

            self._activityruns = AsyncActivityrunsClient(client_wrapper=self._client_wrapper)
        return self._activityruns

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def jobruns(self):
        if self._jobruns is None:
            from .jobruns.client import AsyncJobrunsClient

            self._jobruns = AsyncJobrunsClient(client_wrapper=self._client_wrapper)
        return self._jobruns

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def steps(self):
        if self._steps is None:
            from .steps.client import AsyncStepsClient

            self._steps = AsyncStepsClient(client_wrapper=self._client_wrapper)
        return self._steps


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
