

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.profile import Profile
from .raw_client import AsyncRawKilnsClient, RawKilnsClient


class KilnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKilnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKilnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKilnsClient
        """
        return self._raw_client

    def get_reading(self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The reading, in whichever encoding was asked for.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.get_reading(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.get_reading(kiln_id, request_options=request_options)
        return _response.data

    def probe_kiln(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.probe_kiln(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.probe_kiln(kiln_id, request_options=request_options)
        return _response.headers

    def get_profile(self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Profile:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Profile
            The profile under any media type, or untyped JSON.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.get_profile(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.get_profile(kiln_id, request_options=request_options)
        return _response.data


class AsyncKilnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKilnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKilnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKilnsClient
        """
        return self._raw_client

    async def get_reading(self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The reading, in whichever encoding was asked for.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.get_reading(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reading(kiln_id, request_options=request_options)
        return _response.data

    async def probe_kiln(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.probe_kiln(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.probe_kiln(kiln_id, request_options=request_options)
        return _response.headers

    async def get_profile(self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Profile:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Profile
            The profile under any media type, or untyped JSON.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.get_profile(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_profile(kiln_id, request_options=request_options)
        return _response.data
