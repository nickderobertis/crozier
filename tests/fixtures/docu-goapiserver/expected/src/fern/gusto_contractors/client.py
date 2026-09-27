

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gusto_contractor import GustoContractor
from .raw_client import AsyncRawGustoContractorsClient, RawGustoContractorsClient


class GustoContractorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGustoContractorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGustoContractorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGustoContractorsClient
        """
        return self._raw_client

    def get_gusto_contractors_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoContractor]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GustoContractor]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_contractors.get_gusto_contractors_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_contractors_v3(company_id=company_id, request_options=request_options)
        return _response.data

    def get_gusto_contractors_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoContractor:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GustoContractor
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_contractors.get_gusto_contractors_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_contractors_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data


class AsyncGustoContractorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGustoContractorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGustoContractorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGustoContractorsClient
        """
        return self._raw_client

    async def get_gusto_contractors_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoContractor]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GustoContractor]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_contractors.get_gusto_contractors_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_contractors_v3(
            company_id=company_id, request_options=request_options
        )
        return _response.data

    async def get_gusto_contractors_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoContractor:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GustoContractor
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_contractors.get_gusto_contractors_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_contractors_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data
