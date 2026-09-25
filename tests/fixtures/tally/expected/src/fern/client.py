

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.block import Block
from .types.form import Form
from .types.form_settings import FormSettings
from .types.form_status import FormStatus
from .types.get_current_user_response import GetCurrentUserResponse
from .types.get_form_response import GetFormResponse
from .types.list_forms_response import ListFormsResponse
from .types.list_workspaces_response import ListWorkspacesResponse
from .types.workspace import Workspace

if typing.TYPE_CHECKING:
    from .forms.client import AsyncFormsClient, FormsClient
    from .organization.client import AsyncOrganizationClient, OrganizationClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient

OMIT = typing.cast(typing.Any, ...)


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._organization: typing.Optional[OrganizationClient] = None
        self._forms: typing.Optional[FormsClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def list_forms(
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        workspace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormsResponse:
        """
        Returns a paginated array of form objects.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of forms per page (default: 50, max: 500)

        workspace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter forms by specific workspace IDs (encoded strings)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormsResponse
            A paginated list of forms

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_forms()
        """
        _response = self._raw_client.list_forms(
            page=page, limit=limit, workspace_ids=workspace_ids, request_options=request_options
        )
        return _response.data

    def create_form(
        self,
        *,
        status: FormStatus,
        blocks: typing.Sequence[Block],
        workspace_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[FormSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Creates a new form, optionally based on a template or within a specific workspace.

        Parameters
        ----------
        status : FormStatus
            Initial status of the form

        blocks : typing.Sequence[Block]

        workspace_id : typing.Optional[str]
            ID of the workspace to create the form in. If not provided, uses the user's default workspace

        template_id : typing.Optional[str]
            ID of the template to base the form on

        settings : typing.Optional[FormSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form created successfully

        Examples
        --------
        from fern import (
            Block_FormTitle,
            FernApi,
            FormStatus,
            FormTitleBlockGroupType,
            FormTitlePayload,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_form(
            status=FormStatus.BLANK,
            blocks=[
                Block_FormTitle(
                    uuid_="uuid",
                    group_uuid="groupUuid",
                    group_type=FormTitleBlockGroupType.FORM_TITLE,
                    payload=FormTitlePayload(),
                )
            ],
        )
        """
        _response = self._raw_client.create_form(
            status=status,
            blocks=blocks,
            workspace_id=workspace_id,
            template_id=template_id,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    def get_form(self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetFormResponse:
        """
        Returns a single form by its ID with all its blocks and settings.

        Parameters
        ----------
        form_id : str
            The ID of the form to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormResponse
            Form retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_form(
            form_id="formId",
        )
        """
        _response = self._raw_client.get_form(form_id, request_options=request_options)
        return _response.data

    def delete_form(self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a form by its ID and moves it to the trash.

        Parameters
        ----------
        form_id : str
            The ID of the form to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_form(
            form_id="formId",
        )
        """
        _response = self._raw_client.delete_form(form_id, request_options=request_options)
        return _response.data

    def update_form(
        self,
        form_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[FormStatus] = OMIT,
        blocks: typing.Optional[typing.Sequence[Block]] = OMIT,
        settings: typing.Optional[FormSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Updates a form's settings, blocks, or status.

        Parameters
        ----------
        form_id : str
            The ID of the form to update

        name : typing.Optional[str]
            New name for the form

        status : typing.Optional[FormStatus]
            New status for the form

        blocks : typing.Optional[typing.Sequence[Block]]
            Updated blocks for the form

        settings : typing.Optional[FormSettings]
            Updated settings for the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_form(
            form_id="formId",
        )
        """
        _response = self._raw_client.update_form(
            form_id, name=name, status=status, blocks=blocks, settings=settings, request_options=request_options
        )
        return _response.data

    def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetCurrentUserResponse:
        """
        Returns information about the current authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCurrentUserResponse
            User information retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_current_user()
        """
        _response = self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    def list_workspaces(
        self, *, page: typing.Optional[float] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListWorkspacesResponse:
        """
        Returns a paginated array of workspace objects with associated users and pending invites.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWorkspacesResponse
            A paginated list of workspaces

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_workspaces()
        """
        _response = self._raw_client.list_workspaces(page=page, request_options=request_options)
        return _response.data

    def create_workspace(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> Workspace:
        """
        Creates a new workspace and assigns the authenticated user as a member. Requires a Pro subscription.

        Parameters
        ----------
        name : str
            The name of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workspace
            Workspace created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_workspace(
            name="name",
        )
        """
        _response = self._raw_client.create_workspace(name=name, request_options=request_options)
        return _response.data

    def get_workspace(self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Workspace:
        """
        Returns a single workspace by its ID with associated members.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workspace
            Workspace retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_workspace(workspace_id, request_options=request_options)
        return _response.data

    def delete_workspace(self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a workspace and all its associated forms. The workspace and forms are moved to trash and can be restored later. Forms in DRAFT or PUBLISHED state will be marked as DELETED.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete_workspace(workspace_id, request_options=request_options)
        return _response.data

    def update_workspace(
        self, workspace_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a workspace's information by its ID.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to update

        name : str
            The new name for the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_workspace(
            workspace_id="workspaceId",
            name="name",
        )
        """
        _response = self._raw_client.update_workspace(workspace_id, name=name, request_options=request_options)
        return _response.data

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import OrganizationClient

            self._organization = OrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._organization: typing.Optional[AsyncOrganizationClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def list_forms(
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        workspace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormsResponse:
        """
        Returns a paginated array of form objects.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of forms per page (default: 50, max: 500)

        workspace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter forms by specific workspace IDs (encoded strings)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormsResponse
            A paginated list of forms

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_forms()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_forms(
            page=page, limit=limit, workspace_ids=workspace_ids, request_options=request_options
        )
        return _response.data

    async def create_form(
        self,
        *,
        status: FormStatus,
        blocks: typing.Sequence[Block],
        workspace_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[FormSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Creates a new form, optionally based on a template or within a specific workspace.

        Parameters
        ----------
        status : FormStatus
            Initial status of the form

        blocks : typing.Sequence[Block]

        workspace_id : typing.Optional[str]
            ID of the workspace to create the form in. If not provided, uses the user's default workspace

        template_id : typing.Optional[str]
            ID of the template to base the form on

        settings : typing.Optional[FormSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form created successfully

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Block_FormTitle,
            FormStatus,
            FormTitleBlockGroupType,
            FormTitlePayload,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_form(
                status=FormStatus.BLANK,
                blocks=[
                    Block_FormTitle(
                        uuid_="uuid",
                        group_uuid="groupUuid",
                        group_type=FormTitleBlockGroupType.FORM_TITLE,
                        payload=FormTitlePayload(),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_form(
            status=status,
            blocks=blocks,
            workspace_id=workspace_id,
            template_id=template_id,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    async def get_form(
        self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFormResponse:
        """
        Returns a single form by its ID with all its blocks and settings.

        Parameters
        ----------
        form_id : str
            The ID of the form to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormResponse
            Form retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_form(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form(form_id, request_options=request_options)
        return _response.data

    async def delete_form(self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a form by its ID and moves it to the trash.

        Parameters
        ----------
        form_id : str
            The ID of the form to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_form(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_form(form_id, request_options=request_options)
        return _response.data

    async def update_form(
        self,
        form_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        status: typing.Optional[FormStatus] = OMIT,
        blocks: typing.Optional[typing.Sequence[Block]] = OMIT,
        settings: typing.Optional[FormSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Updates a form's settings, blocks, or status.

        Parameters
        ----------
        form_id : str
            The ID of the form to update

        name : typing.Optional[str]
            New name for the form

        status : typing.Optional[FormStatus]
            New status for the form

        blocks : typing.Optional[typing.Sequence[Block]]
            Updated blocks for the form

        settings : typing.Optional[FormSettings]
            Updated settings for the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_form(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form(
            form_id, name=name, status=status, blocks=blocks, settings=settings, request_options=request_options
        )
        return _response.data

    async def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCurrentUserResponse:
        """
        Returns information about the current authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCurrentUserResponse
            User information retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    async def list_workspaces(
        self, *, page: typing.Optional[float] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListWorkspacesResponse:
        """
        Returns a paginated array of workspace objects with associated users and pending invites.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWorkspacesResponse
            A paginated list of workspaces

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_workspaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workspaces(page=page, request_options=request_options)
        return _response.data

    async def create_workspace(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Workspace:
        """
        Creates a new workspace and assigns the authenticated user as a member. Requires a Pro subscription.

        Parameters
        ----------
        name : str
            The name of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workspace
            Workspace created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_workspace(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace(name=name, request_options=request_options)
        return _response.data

    async def get_workspace(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Workspace:
        """
        Returns a single workspace by its ID with associated members.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workspace
            Workspace retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace(workspace_id, request_options=request_options)
        return _response.data

    async def delete_workspace(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a workspace and all its associated forms. The workspace and forms are moved to trash and can be restored later. Forms in DRAFT or PUBLISHED state will be marked as DELETED.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace(workspace_id, request_options=request_options)
        return _response.data

    async def update_workspace(
        self, workspace_id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a workspace's information by its ID.

        Parameters
        ----------
        workspace_id : str
            The ID of the workspace to update

        name : str
            The new name for the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_workspace(
                workspace_id="workspaceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workspace(workspace_id, name=name, request_options=request_options)
        return _response.data

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import AsyncOrganizationClient

            self._organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
