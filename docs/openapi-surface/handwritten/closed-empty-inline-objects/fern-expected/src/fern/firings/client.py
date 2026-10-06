

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFiringsClient, RawFiringsClient


OMIT = typing.cast(typing.Any, ...)


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def schedule_firing(
        self,
        *,
        kiln: str,
        profile: typing.Dict[str, typing.Any],
        notes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ramp: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        kiln : str

        profile : typing.Dict[str, typing.Any]

        notes : typing.Optional[typing.Dict[str, typing.Any]]

        ramp : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The firing was scheduled.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.schedule_firing(
            kiln="kiln",
            profile={"key": "value"},
        )
        """
        _response = self._raw_client.schedule_firing(
            kiln=kiln, profile=profile, notes=notes, ramp=ramp, request_options=request_options
        )
        return _response.data

    def amend_firing(
        self,
        firing_id: str,
        *,
        glaze: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        firing_id : str

        glaze : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The firing was amended.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.firings.amend_firing(
            firing_id="firingId",
        )
        """
        _response = self._raw_client.amend_firing(firing_id, glaze=glaze, request_options=request_options)
        return _response.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def schedule_firing(
        self,
        *,
        kiln: str,
        profile: typing.Dict[str, typing.Any],
        notes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ramp: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        kiln : str

        profile : typing.Dict[str, typing.Any]

        notes : typing.Optional[typing.Dict[str, typing.Any]]

        ramp : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The firing was scheduled.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.schedule_firing(
                kiln="kiln",
                profile={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_firing(
            kiln=kiln, profile=profile, notes=notes, ramp=ramp, request_options=request_options
        )
        return _response.data

    async def amend_firing(
        self,
        firing_id: str,
        *,
        glaze: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        firing_id : str

        glaze : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The firing was amended.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.firings.amend_firing(
                firing_id="firingId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.amend_firing(firing_id, glaze=glaze, request_options=request_options)
        return _response.data
