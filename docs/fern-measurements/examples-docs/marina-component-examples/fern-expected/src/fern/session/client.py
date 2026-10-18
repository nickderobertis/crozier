

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session_form_grant import SessionFormGrant
from .raw_client import AsyncRawSessionClient, RawSessionClient


OMIT = typing.cast(typing.Any, ...)


class SessionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionClient
        """
        return self._raw_client

    def open_session(
        self,
        *,
        grant: typing.Optional[SessionFormGrant] = OMIT,
        skipper_id: typing.Optional[str] = OMIT,
        pin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        grant : typing.Optional[SessionFormGrant]

        skipper_id : typing.Optional[str]

        pin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, SessionFormGrant

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session.open_session(
            grant=SessionFormGrant.HARBOUR_PASS,
            skipper_id="SK-118",
            pin="4471",
        )
        """
        _response = self._raw_client.open_session(
            grant=grant, skipper_id=skipper_id, pin=pin, request_options=request_options
        )
        return _response.data


class AsyncSessionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionClient
        """
        return self._raw_client

    async def open_session(
        self,
        *,
        grant: typing.Optional[SessionFormGrant] = OMIT,
        skipper_id: typing.Optional[str] = OMIT,
        pin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        grant : typing.Optional[SessionFormGrant]

        skipper_id : typing.Optional[str]

        pin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SessionFormGrant

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session.open_session(
                grant=SessionFormGrant.HARBOUR_PASS,
                skipper_id="SK-118",
                pin="4471",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.open_session(
            grant=grant, skipper_id=skipper_id, pin=pin, request_options=request_options
        )
        return _response.data
