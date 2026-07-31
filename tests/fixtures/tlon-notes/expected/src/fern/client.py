

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.action import Action
from .types.folder import Folder
from .types.invite_record import InviteRecord
from .types.member_record import MemberRecord
from .types.note import Note
from .types.note_revision import NoteRevision
from .types.notebook_summary import NotebookSummary
from .types.request_id import RequestId
from .types.response import Response


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



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def submit_action(
        self,
        *,
        action: Action,
        request_id: typing.Optional[RequestId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parses the body as a `RequestEnvelope`, registers the
        `requestId` in the agent's `requests` map with this Eyre
        request's id as the held HTTP slot, then dispatches the
        wrapped action. Returns when a terminal response-update
        arrives (typical), the host nacks (error), or the 20 s
        per-request behn timer fires (pending).

        Parameters
        ----------
        action : Action

        request_id : typing.Optional[RequestId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Terminal or pending response from the agent

        Examples
        --------
        from fern import Action_CreateNotebook, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.submit_action(
            request_id="0v1.ab2cd.ef3gh.ij4kl",
            action=Action_CreateNotebook(
                title="title",
            ),
        )
        """
        _response = self._raw_client.submit_action(
            action=action, request_id=request_id, request_options=request_options
        )
        return _response.data

    def get_request(
        self, request_id: RequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Response:
        """
        Returns the same `Response` shape as the original POST. If the
        request is still in flight (or the POST timed out with a
        `pending` body), this returns the current state. Marks the
        request as fetched so the agent's cleanup pass can evict it
        sooner.

        Parameters
        ----------
        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Current request state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_request(
            request_id="0v3.1k7gh.j5b2m.r8nq9",
        )
        """
        _response = self._raw_client.get_request(request_id, request_options=request_options)
        return _response.data

    def list_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotebookSummary]:
        """
        All notebooks the authenticated identity can view (hosted or
        subscribed). Same data as the `/x/v0/notebooks` scry, but
        honors `X-Api-Key` so a bot can read without a session cookie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotebookSummary]
            Notebook summaries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_notebooks()
        """
        _response = self._raw_client.list_notebooks(request_options=request_options)
        return _response.data

    def create_notebook(self, *, title: str, request_options: typing.Optional[RequestOptions] = None) -> Response:
        """
        First-class convenience endpoint — flat body, no discriminated
        union. Equivalent to submitAction with a create-notebook action.
        Returns the new notebook's summary (incl. the slugified flag).

        Parameters
        ----------
        title : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response body is type `notebook`

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_notebook(
            title="title",
        )
        """
        _response = self._raw_client.create_notebook(title=title, request_options=request_options)
        return _response.data

    def get_notebook(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotebookSummary:
        """
        Parameters
        ----------
        host : str
            Host ship (~-prefixed @p)

        name : str
            Notebook slug (@tas)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotebookSummary
            Notebook detail

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_notebook(
            host="host",
            name="name",
        )
        """
        _response = self._raw_client.get_notebook(host, name, request_options=request_options)
        return _response.data

    def list_folders(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            Folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_folders(
            host="host",
            name="name",
        )
        """
        _response = self._raw_client.list_folders(host, name, request_options=request_options)
        return _response.data

    def create_folder(
        self,
        host: str,
        name: str,
        *,
        folder_name: str,
        parent: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        folder_name : str
            Name of the new folder. (Distinct from the path's `{name}` which is the notebook slug — when mcp-proxy flattens path + body fields into a single tool input, a colliding name would conflate the two.)

        parent : int
            Parent folder id (required). To create a top-level folder, pass the notebook's root folder id (`notebook.rootFolderId`). An id that doesn't exist in the notebook is rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response carries the folder-created update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_folder(
            host="host",
            name="name",
            folder_name="folderName",
            parent=1,
        )
        """
        _response = self._raw_client.create_folder(
            host, name, folder_name=folder_name, parent=parent, request_options=request_options
        )
        return _response.data

    def get_folder(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Folder:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_folder(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.get_folder(host, name, id, request_options=request_options)
        return _response.data

    def update_folder(
        self,
        host: str,
        name: str,
        id: int,
        *,
        folder_name: typing.Optional[str] = OMIT,
        parent: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Provide `name`, `parent`, or both. Fields left out (or null) are unchanged. An explicit `parent` that doesn't exist in the notebook, or that would move the folder into its own subtree, is rejected.

        Parameters
        ----------
        host : str

        name : str

        id : int

        folder_name : typing.Optional[str]

        parent : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Updated — response carries the folder-updated update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_folder(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.update_folder(
            host, name, id, folder_name=folder_name, parent=parent, request_options=request_options
        )
        return _response.data

    def delete_folder(
        self,
        host: str,
        name: str,
        id: int,
        *,
        recursive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Default refuses if the folder has children; pass `?recursive=true` to delete the folder and everything beneath it.

        Parameters
        ----------
        host : str

        name : str

        id : int

        recursive : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Deleted — response carries the folder-deleted update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_folder(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.delete_folder(host, name, id, recursive=recursive, request_options=request_options)
        return _response.data

    def list_notes(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Note]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Note]
            Notes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_notes(
            host="host",
            name="name",
        )
        """
        _response = self._raw_client.list_notes(host, name, request_options=request_options)
        return _response.data

    def create_note(
        self,
        host: str,
        name: str,
        *,
        folder: int,
        title: str,
        body: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        folder : int
            Containing folder id

        title : str

        body : typing.Optional[str]
            Markdown body; defaults to empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response carries the note-created update with the new id

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_note(
            host="host",
            name="name",
            folder=1,
            title="title",
        )
        """
        _response = self._raw_client.create_note(
            host, name, folder=folder, title=title, body=body, request_options=request_options
        )
        return _response.data

    def get_note(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Note:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Note
            Note

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_note(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.get_note(host, name, id, request_options=request_options)
        return _response.data

    def update_note(
        self,
        host: str,
        name: str,
        id: int,
        *,
        body: typing.Optional[str] = OMIT,
        expected_revision: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        folder: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Updates a note. Two distinct modes based on what's in the body:

        - **Content edit**: provide `body` (with optional `expectedRevision`
          for optimistic-concurrency, exactly like the UI's autosave;
          omit it for last-write-wins). Bumps the note's revision.
        - **Metadata edit**: provide `title` and/or `folder` (rename
          and/or move). Does *not* bump revision.

        If `body` is present, the call is treated as a content edit and
        `title` / `folder` are ignored. To rename or move alongside a
        content edit, send two requests.

        Uses PUT, not PATCH — vere's runtime HTTP server rejects PATCH
        before it reaches the agent.

        Parameters
        ----------
        host : str

        name : str

        id : int

        body : typing.Optional[str]

        expected_revision : typing.Optional[int]
            Optional content-edit guard

        title : typing.Optional[str]
            New title (metadata-edit mode)

        folder : typing.Optional[int]
            New parent folder id (metadata-edit mode)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Updated — response carries the note-updated update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_note(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.update_note(
            host,
            name,
            id,
            body=body,
            expected_revision=expected_revision,
            title=title,
            folder=folder,
            request_options=request_options,
        )
        return _response.data

    def delete_note(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Deleted — response carries the note-deleted update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_note(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.delete_note(host, name, id, request_options=request_options)
        return _response.data

    def get_note_history(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NoteRevision]:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteRevision]
            Archived revisions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_note_history(
            host="host",
            name="name",
            id=1,
        )
        """
        _response = self._raw_client.get_note_history(host, name, id, request_options=request_options)
        return _response.data

    def list_members(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MemberRecord]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MemberRecord]
            Members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_members(
            host="host",
            name="name",
        )
        """
        _response = self._raw_client.list_members(host, name, request_options=request_options)
        return _response.data

    def list_invites(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[InviteRecord]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InviteRecord]
            Invite records

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_invites()
        """
        _response = self._raw_client.list_invites(request_options=request_options)
        return _response.data


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



    api_key : str
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

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def submit_action(
        self,
        *,
        action: Action,
        request_id: typing.Optional[RequestId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parses the body as a `RequestEnvelope`, registers the
        `requestId` in the agent's `requests` map with this Eyre
        request's id as the held HTTP slot, then dispatches the
        wrapped action. Returns when a terminal response-update
        arrives (typical), the host nacks (error), or the 20 s
        per-request behn timer fires (pending).

        Parameters
        ----------
        action : Action

        request_id : typing.Optional[RequestId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Terminal or pending response from the agent

        Examples
        --------
        import asyncio

        from fern import Action_CreateNotebook, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.submit_action(
                request_id="0v1.ab2cd.ef3gh.ij4kl",
                action=Action_CreateNotebook(
                    title="title",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_action(
            action=action, request_id=request_id, request_options=request_options
        )
        return _response.data

    async def get_request(
        self, request_id: RequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Response:
        """
        Returns the same `Response` shape as the original POST. If the
        request is still in flight (or the POST timed out with a
        `pending` body), this returns the current state. Marks the
        request as fetched so the agent's cleanup pass can evict it
        sooner.

        Parameters
        ----------
        request_id : RequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Current request state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_request(
                request_id="0v3.1k7gh.j5b2m.r8nq9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_request(request_id, request_options=request_options)
        return _response.data

    async def list_notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotebookSummary]:
        """
        All notebooks the authenticated identity can view (hosted or
        subscribed). Same data as the `/x/v0/notebooks` scry, but
        honors `X-Api-Key` so a bot can read without a session cookie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotebookSummary]
            Notebook summaries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_notebooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notebooks(request_options=request_options)
        return _response.data

    async def create_notebook(self, *, title: str, request_options: typing.Optional[RequestOptions] = None) -> Response:
        """
        First-class convenience endpoint — flat body, no discriminated
        union. Equivalent to submitAction with a create-notebook action.
        Returns the new notebook's summary (incl. the slugified flag).

        Parameters
        ----------
        title : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response body is type `notebook`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_notebook(
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notebook(title=title, request_options=request_options)
        return _response.data

    async def get_notebook(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotebookSummary:
        """
        Parameters
        ----------
        host : str
            Host ship (~-prefixed @p)

        name : str
            Notebook slug (@tas)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotebookSummary
            Notebook detail

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_notebook(
                host="host",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notebook(host, name, request_options=request_options)
        return _response.data

    async def list_folders(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            Folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_folders(
                host="host",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folders(host, name, request_options=request_options)
        return _response.data

    async def create_folder(
        self,
        host: str,
        name: str,
        *,
        folder_name: str,
        parent: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        folder_name : str
            Name of the new folder. (Distinct from the path's `{name}` which is the notebook slug — when mcp-proxy flattens path + body fields into a single tool input, a colliding name would conflate the two.)

        parent : int
            Parent folder id (required). To create a top-level folder, pass the notebook's root folder id (`notebook.rootFolderId`). An id that doesn't exist in the notebook is rejected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response carries the folder-created update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_folder(
                host="host",
                name="name",
                folder_name="folderName",
                parent=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_folder(
            host, name, folder_name=folder_name, parent=parent, request_options=request_options
        )
        return _response.data

    async def get_folder(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Folder:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_folder(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder(host, name, id, request_options=request_options)
        return _response.data

    async def update_folder(
        self,
        host: str,
        name: str,
        id: int,
        *,
        folder_name: typing.Optional[str] = OMIT,
        parent: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Provide `name`, `parent`, or both. Fields left out (or null) are unchanged. An explicit `parent` that doesn't exist in the notebook, or that would move the folder into its own subtree, is rejected.

        Parameters
        ----------
        host : str

        name : str

        id : int

        folder_name : typing.Optional[str]

        parent : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Updated — response carries the folder-updated update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_folder(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_folder(
            host, name, id, folder_name=folder_name, parent=parent, request_options=request_options
        )
        return _response.data

    async def delete_folder(
        self,
        host: str,
        name: str,
        id: int,
        *,
        recursive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Default refuses if the folder has children; pass `?recursive=true` to delete the folder and everything beneath it.

        Parameters
        ----------
        host : str

        name : str

        id : int

        recursive : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Deleted — response carries the folder-deleted update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_folder(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder(
            host, name, id, recursive=recursive, request_options=request_options
        )
        return _response.data

    async def list_notes(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Note]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Note]
            Notes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_notes(
                host="host",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notes(host, name, request_options=request_options)
        return _response.data

    async def create_note(
        self,
        host: str,
        name: str,
        *,
        folder: int,
        title: str,
        body: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        folder : int
            Containing folder id

        title : str

        body : typing.Optional[str]
            Markdown body; defaults to empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Created — response carries the note-created update with the new id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_note(
                host="host",
                name="name",
                folder=1,
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_note(
            host, name, folder=folder, title=title, body=body, request_options=request_options
        )
        return _response.data

    async def get_note(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Note:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Note
            Note

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_note(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_note(host, name, id, request_options=request_options)
        return _response.data

    async def update_note(
        self,
        host: str,
        name: str,
        id: int,
        *,
        body: typing.Optional[str] = OMIT,
        expected_revision: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        folder: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Response:
        """
        Updates a note. Two distinct modes based on what's in the body:

        - **Content edit**: provide `body` (with optional `expectedRevision`
          for optimistic-concurrency, exactly like the UI's autosave;
          omit it for last-write-wins). Bumps the note's revision.
        - **Metadata edit**: provide `title` and/or `folder` (rename
          and/or move). Does *not* bump revision.

        If `body` is present, the call is treated as a content edit and
        `title` / `folder` are ignored. To rename or move alongside a
        content edit, send two requests.

        Uses PUT, not PATCH — vere's runtime HTTP server rejects PATCH
        before it reaches the agent.

        Parameters
        ----------
        host : str

        name : str

        id : int

        body : typing.Optional[str]

        expected_revision : typing.Optional[int]
            Optional content-edit guard

        title : typing.Optional[str]
            New title (metadata-edit mode)

        folder : typing.Optional[int]
            New parent folder id (metadata-edit mode)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Updated — response carries the note-updated update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_note(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_note(
            host,
            name,
            id,
            body=body,
            expected_revision=expected_revision,
            title=title,
            folder=folder,
            request_options=request_options,
        )
        return _response.data

    async def delete_note(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Response:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Response
            Deleted — response carries the note-deleted update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_note(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note(host, name, id, request_options=request_options)
        return _response.data

    async def get_note_history(
        self, host: str, name: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NoteRevision]:
        """
        Parameters
        ----------
        host : str

        name : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NoteRevision]
            Archived revisions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_note_history(
                host="host",
                name="name",
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_note_history(host, name, id, request_options=request_options)
        return _response.data

    async def list_members(
        self, host: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MemberRecord]:
        """
        Parameters
        ----------
        host : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MemberRecord]
            Members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_members(
                host="host",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_members(host, name, request_options=request_options)
        return _response.data

    async def list_invites(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InviteRecord]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InviteRecord]
            Invite records

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_invites()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_invites(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
