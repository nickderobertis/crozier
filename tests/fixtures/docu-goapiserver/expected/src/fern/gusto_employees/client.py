

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gusto_employee import GustoEmployee
from .raw_client import AsyncRawGustoEmployeesClient, RawGustoEmployeesClient


class GustoEmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGustoEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGustoEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGustoEmployeesClient
        """
        return self._raw_client

    def get_gusto_employees_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoEmployee]:
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
        typing.List[GustoEmployee]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_employees.get_gusto_employees_v3(
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_employees_v3(company_id=company_id, request_options=request_options)
        return _response.data

    def get_gusto_employees_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoEmployee:
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
        GustoEmployee
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gusto_employees.get_gusto_employees_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_gusto_employees_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data


class AsyncGustoEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGustoEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGustoEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGustoEmployeesClient
        """
        return self._raw_client

    async def get_gusto_employees_v3(
        self, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GustoEmployee]:
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
        typing.List[GustoEmployee]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_employees.get_gusto_employees_v3(
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_employees_v3(
            company_id=company_id, request_options=request_options
        )
        return _response.data

    async def get_gusto_employees_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GustoEmployee:
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
        GustoEmployee
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gusto_employees.get_gusto_employees_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gusto_employees_id_v3(
            id, company_id=company_id, request_options=request_options
        )
        return _response.data
