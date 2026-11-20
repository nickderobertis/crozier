

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProbesClient, RawProbesClient


class ProbesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProbesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProbesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProbesClient
        """
        return self._raw_client

    def read_probe(
        self, probe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        probe_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            The probe's last reading, when it has taken one.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.probes.read_probe(
            probe_id="probeId",
        )
        """
        _response = self._raw_client.read_probe(probe_id, request_options=request_options)
        return _response.data

    def list_probe_labels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[str]]
            Each probe's label, where one is set.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.probes.list_probe_labels()
        """
        _response = self._raw_client.list_probe_labels(request_options=request_options)
        return _response.data


class AsyncProbesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProbesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProbesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProbesClient
        """
        return self._raw_client

    async def read_probe(
        self, probe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        probe_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            The probe's last reading, when it has taken one.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.probes.read_probe(
                probe_id="probeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_probe(probe_id, request_options=request_options)
        return _response.data

    async def list_probe_labels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[str]]
            Each probe's label, where one is set.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.probes.list_probe_labels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_probe_labels(request_options=request_options)
        return _response.data
