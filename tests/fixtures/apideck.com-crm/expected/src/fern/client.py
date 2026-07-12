

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .activities.client import ActivitiesClient, AsyncActivitiesClient
    from .companies.client import AsyncCompaniesClient, CompaniesClient
    from .contacts.client import AsyncContactsClient, ContactsClient
    from .leads.client import AsyncLeadsClient, LeadsClient
    from .notes.client import AsyncNotesClient, NotesClient
    from .opportunities.client import AsyncOpportunitiesClient, OpportunitiesClient
    from .pipelines.client import AsyncPipelinesClient, PipelinesClient
    from .users.client import AsyncUsersClient, UsersClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    apideck_service_id : typing.Optional[str]
    apideck_app_id : str
    apideck_consumer_id : str
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        apideck_service_id: typing.Optional[str] = None,
        apideck_app_id: str,
        apideck_consumer_id: str,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            apideck_service_id=apideck_service_id,
            apideck_app_id=apideck_app_id,
            apideck_consumer_id=apideck_consumer_id,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._activities: typing.Optional[ActivitiesClient] = None
        self._companies: typing.Optional[CompaniesClient] = None
        self._contacts: typing.Optional[ContactsClient] = None
        self._leads: typing.Optional[LeadsClient] = None
        self._notes: typing.Optional[NotesClient] = None
        self._opportunities: typing.Optional[OpportunitiesClient] = None
        self._pipelines: typing.Optional[PipelinesClient] = None
        self._users: typing.Optional[UsersClient] = None

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import ActivitiesClient

            self._activities = ActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import CompaniesClient

            self._companies = CompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import ContactsClient

            self._contacts = ContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def leads(self):
        if self._leads is None:
            from .leads.client import LeadsClient

            self._leads = LeadsClient(client_wrapper=self._client_wrapper)
        return self._leads

    @property
    def notes(self):
        if self._notes is None:
            from .notes.client import NotesClient

            self._notes = NotesClient(client_wrapper=self._client_wrapper)
        return self._notes

    @property
    def opportunities(self):
        if self._opportunities is None:
            from .opportunities.client import OpportunitiesClient

            self._opportunities = OpportunitiesClient(client_wrapper=self._client_wrapper)
        return self._opportunities

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import PipelinesClient

            self._pipelines = PipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    apideck_service_id : typing.Optional[str]
    apideck_app_id : str
    apideck_consumer_id : str
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        apideck_service_id: typing.Optional[str] = None,
        apideck_app_id: str,
        apideck_consumer_id: str,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            apideck_service_id=apideck_service_id,
            apideck_app_id=apideck_app_id,
            apideck_consumer_id=apideck_consumer_id,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._activities: typing.Optional[AsyncActivitiesClient] = None
        self._companies: typing.Optional[AsyncCompaniesClient] = None
        self._contacts: typing.Optional[AsyncContactsClient] = None
        self._leads: typing.Optional[AsyncLeadsClient] = None
        self._notes: typing.Optional[AsyncNotesClient] = None
        self._opportunities: typing.Optional[AsyncOpportunitiesClient] = None
        self._pipelines: typing.Optional[AsyncPipelinesClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import AsyncActivitiesClient

            self._activities = AsyncActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import AsyncCompaniesClient

            self._companies = AsyncCompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import AsyncContactsClient

            self._contacts = AsyncContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def leads(self):
        if self._leads is None:
            from .leads.client import AsyncLeadsClient

            self._leads = AsyncLeadsClient(client_wrapper=self._client_wrapper)
        return self._leads

    @property
    def notes(self):
        if self._notes is None:
            from .notes.client import AsyncNotesClient

            self._notes = AsyncNotesClient(client_wrapper=self._client_wrapper)
        return self._notes

    @property
    def opportunities(self):
        if self._opportunities is None:
            from .opportunities.client import AsyncOpportunitiesClient

            self._opportunities = AsyncOpportunitiesClient(client_wrapper=self._client_wrapper)
        return self._opportunities

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import AsyncPipelinesClient

            self._pipelines = AsyncPipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
