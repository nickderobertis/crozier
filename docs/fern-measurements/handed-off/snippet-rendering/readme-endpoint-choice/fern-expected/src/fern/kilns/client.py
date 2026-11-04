

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.firing import Firing
from ..types.kiln import Kiln
from .raw_client import AsyncRawKilnsClient, RawKilnsClient


OMIT = typing.cast(typing.Any, ...)


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

    def list_kilns(self, *, site: str, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Kiln]:
        """
        Parameters
        ----------
        site : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kiln]
            The kilns at the site.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.list_kilns(
            site="site",
        )
        """
        _response = self._raw_client.list_kilns(site=site, request_options=request_options)
        return _response.data

    def record_firing(
        self, *, controller_log: core.File, kiln: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Firing:
        """
        Parameters
        ----------
        controller_log : core.File
            See core.File for more documentation

        kiln : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Firing
            The recorded firing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.record_firing(
            kiln="kiln",
        )
        """
        _response = self._raw_client.record_firing(
            controller_log=controller_log, kiln=kiln, request_options=request_options
        )
        return _response.data

    def add_glaze(
        self, *, name: str, cone: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Firing:
        """
        Parameters
        ----------
        name : str

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Firing
            The added glaze.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kilns.add_glaze(
            name="name",
        )
        """
        _response = self._raw_client.add_glaze(name=name, cone=cone, request_options=request_options)
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

    async def list_kilns(
        self, *, site: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Kiln]:
        """
        Parameters
        ----------
        site : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Kiln]
            The kilns at the site.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.list_kilns(
                site="site",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_kilns(site=site, request_options=request_options)
        return _response.data

    async def record_firing(
        self, *, controller_log: core.File, kiln: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Firing:
        """
        Parameters
        ----------
        controller_log : core.File
            See core.File for more documentation

        kiln : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Firing
            The recorded firing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.record_firing(
                kiln="kiln",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_firing(
            controller_log=controller_log, kiln=kiln, request_options=request_options
        )
        return _response.data

    async def add_glaze(
        self, *, name: str, cone: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Firing:
        """
        Parameters
        ----------
        name : str

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Firing
            The added glaze.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kilns.add_glaze(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_glaze(name=name, cone=cone, request_options=request_options)
        return _response.data
