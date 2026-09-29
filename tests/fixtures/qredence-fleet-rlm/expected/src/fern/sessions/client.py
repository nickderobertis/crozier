

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session_detail_response import SessionDetailResponse
from ..types.session_list_response import SessionListResponse
from ..types.session_task_response import SessionTaskResponse
from ..types.session_turn_page_response import SessionTurnPageResponse
from .raw_client import AsyncRawSessionsClient, RawSessionsClient
from .types.list_sessions_request_status import ListSessionsRequestStatus
from .types.session_patch_request_status import SessionPatchRequestStatus


OMIT = typing.cast(typing.Any, ...)


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionsClient
        """
        return self._raw_client

    def list_session_turns(
        self,
        session_id: str,
        *,
        limit: typing.Optional[int] = None,
        after_sequence: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionTurnPageResponse:
        """
        Parameters
        ----------
        session_id : str

        limit : typing.Optional[int]

        after_sequence : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTurnPageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.list_session_turns(
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_session_turns(
            session_id, limit=limit, after_sequence=after_sequence, request_options=request_options
        )
        return _response.data

    def list_sessions(
        self,
        *,
        status: typing.Optional[ListSessionsRequestStatus] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionListResponse:
        """
        Parameters
        ----------
        status : typing.Optional[ListSessionsRequestStatus]

        search : typing.Optional[str]
            Title contains

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.list_sessions()
        """
        _response = self._raw_client.list_sessions(
            status=status, search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_session(
        self, *, title: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionDetailResponse:
        """
        Create a session for the local user in the current workspace.

        Parameters:
            body (SessionCreateRequest): Session creation data, including the optional title.
            identity (LocalScopeDep): The deterministic local User and Workspace scope.
            repo (SessionCatalogDep): Session repository used to create the session.
            prewarm (SessionPrewarmDep): Optional background Sandbox pre-warm trigger.

        Returns:
            SessionDetailResponse: The newly created session details.

        Parameters
        ----------
        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.create_session()
        """
        _response = self._raw_client.create_session(title=title, request_options=request_options)
        return _response.data

    def get_session(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionDetailResponse:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.get_session(
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_session(session_id, request_options=request_options)
        return _response.data

    def update_session(
        self,
        session_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[SessionPatchRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionDetailResponse:
        """
        Update the title or status of a session within the local user's workspace.

        Parameters:
            body (SessionPatchRequest): Fields to update; at least one field is required.

        Returns:
            SessionDetailResponse: The updated session details.

        Raises:
            HTTPException: If no fields are provided, the title is blank, the status is invalid, or the
                session cannot be updated.

        Parameters
        ----------
        session_id : str

        title : typing.Optional[str]

        status : typing.Optional[SessionPatchRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.update_session(
            session_id="session_id",
        )
        """
        _response = self._raw_client.update_session(
            session_id, title=title, status=status, request_options=request_options
        )
        return _response.data

    def get_session_task(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTaskResponse:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.get_session_task(
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_session_task(session_id, request_options=request_options)
        return _response.data


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionsClient
        """
        return self._raw_client

    async def list_session_turns(
        self,
        session_id: str,
        *,
        limit: typing.Optional[int] = None,
        after_sequence: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionTurnPageResponse:
        """
        Parameters
        ----------
        session_id : str

        limit : typing.Optional[int]

        after_sequence : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTurnPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.list_session_turns(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_session_turns(
            session_id, limit=limit, after_sequence=after_sequence, request_options=request_options
        )
        return _response.data

    async def list_sessions(
        self,
        *,
        status: typing.Optional[ListSessionsRequestStatus] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionListResponse:
        """
        Parameters
        ----------
        status : typing.Optional[ListSessionsRequestStatus]

        search : typing.Optional[str]
            Title contains

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.list_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sessions(
            status=status, search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_session(
        self, *, title: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionDetailResponse:
        """
        Create a session for the local user in the current workspace.

        Parameters:
            body (SessionCreateRequest): Session creation data, including the optional title.
            identity (LocalScopeDep): The deterministic local User and Workspace scope.
            repo (SessionCatalogDep): Session repository used to create the session.
            prewarm (SessionPrewarmDep): Optional background Sandbox pre-warm trigger.

        Returns:
            SessionDetailResponse: The newly created session details.

        Parameters
        ----------
        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.create_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_session(title=title, request_options=request_options)
        return _response.data

    async def get_session(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionDetailResponse:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.get_session(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_session(session_id, request_options=request_options)
        return _response.data

    async def update_session(
        self,
        session_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[SessionPatchRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionDetailResponse:
        """
        Update the title or status of a session within the local user's workspace.

        Parameters:
            body (SessionPatchRequest): Fields to update; at least one field is required.

        Returns:
            SessionDetailResponse: The updated session details.

        Raises:
            HTTPException: If no fields are provided, the title is blank, the status is invalid, or the
                session cannot be updated.

        Parameters
        ----------
        session_id : str

        title : typing.Optional[str]

        status : typing.Optional[SessionPatchRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDetailResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.update_session(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_session(
            session_id, title=title, status=status, request_options=request_options
        )
        return _response.data

    async def get_session_task(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionTaskResponse:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.get_session_task(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_session_task(session_id, request_options=request_options)
        return _response.data
