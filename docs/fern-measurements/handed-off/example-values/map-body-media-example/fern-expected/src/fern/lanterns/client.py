

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLanternsClient, RawLanternsClient


OMIT = typing.cast(typing.Any, ...)


class LanternsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLanternsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLanternsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLanternsClient
        """
        return self._raw_client

    def set_lantern_labels(
        self,
        lantern_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lantern_id : str

        request : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lanterns.set_lantern_labels(
            lantern_id="lanternId",
            request={"colour": "amber", "range": "long"},
        )
        """
        _response = self._raw_client.set_lantern_labels(lantern_id, request=request, request_options=request_options)
        return _response.data

    def add_lantern_note(
        self,
        lantern_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lantern_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lanterns.add_lantern_note(
            lantern_id="lanternId",
            request={"body": {"text": "lens cleaned"}, "file": "maintenance.log"},
        )
        """
        _response = self._raw_client.add_lantern_note(lantern_id, request=request, request_options=request_options)
        return _response.data


class AsyncLanternsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLanternsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLanternsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLanternsClient
        """
        return self._raw_client

    async def set_lantern_labels(
        self,
        lantern_id: str,
        *,
        request: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lantern_id : str

        request : typing.Dict[str, str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lanterns.set_lantern_labels(
                lantern_id="lanternId",
                request={"colour": "amber", "range": "long"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_lantern_labels(
            lantern_id, request=request, request_options=request_options
        )
        return _response.data

    async def add_lantern_note(
        self,
        lantern_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lantern_id : str

        request : typing.Dict[str, typing.Any]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lanterns.add_lantern_note(
                lantern_id="lanternId",
                request={"body": {"text": "lens cleaned"}, "file": "maintenance.log"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_lantern_note(
            lantern_id, request=request, request_options=request_options
        )
        return _response.data
