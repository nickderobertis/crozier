

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contributor_out import ContributorOut
from .raw_client import AsyncRawContributorsClient, RawContributorsClient


OMIT = typing.cast(typing.Any, ...)


class ContributorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContributorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContributorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContributorsClient
        """
        return self._raw_client

    def create_contributor(
        self,
        *,
        country: str,
        mosaic: core.File,
        name: str,
        screenshot: core.File,
        series_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContributorOut:
        """
        Parameters
        ----------
        country : str

        mosaic : core.File
            See core.File for more documentation

        name : str

        screenshot : core.File
            See core.File for more documentation

        series_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.contributors.create_contributor(
            country="country",
            name="name",
        )
        """
        _response = self._raw_client.create_contributor(
            country=country,
            mosaic=mosaic,
            name=name,
            screenshot=screenshot,
            series_id=series_id,
            request_options=request_options,
        )
        return _response.data

    def get_contributor(
        self, contrib_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorOut:
        """
        Parameters
        ----------
        contrib_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.contributors.get_contributor(
            contrib_id=1,
        )
        """
        _response = self._raw_client.get_contributor(contrib_id, request_options=request_options)
        return _response.data


class AsyncContributorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContributorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContributorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContributorsClient
        """
        return self._raw_client

    async def create_contributor(
        self,
        *,
        country: str,
        mosaic: core.File,
        name: str,
        screenshot: core.File,
        series_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContributorOut:
        """
        Parameters
        ----------
        country : str

        mosaic : core.File
            See core.File for more documentation

        name : str

        screenshot : core.File
            See core.File for more documentation

        series_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contributors.create_contributor(
                country="country",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_contributor(
            country=country,
            mosaic=mosaic,
            name=name,
            screenshot=screenshot,
            series_id=series_id,
            request_options=request_options,
        )
        return _response.data

    async def get_contributor(
        self, contrib_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorOut:
        """
        Parameters
        ----------
        contrib_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contributors.get_contributor(
                contrib_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contributor(contrib_id, request_options=request_options)
        return _response.data
