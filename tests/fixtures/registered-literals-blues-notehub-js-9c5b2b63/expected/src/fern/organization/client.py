

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrganizationClient, RawOrganizationClient
from .types.get_organization_balance_history_response import GetOrganizationBalanceHistoryResponse
from .types.get_organization_response import GetOrganizationResponse
from .types.get_organizations_response import GetOrganizationsResponse


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationClient
        """
        return self._raw_client

    def get_organizations(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetOrganizationsResponse:
        """
        Get Organizations accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.get_organizations()
        """
        _response = self._raw_client.get_organizations(request_options=request_options)
        return _response.data

    def get_organization(
        self, organization_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationResponse:
        """
        Get Organization Information

        Parameters
        ----------
        organization_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.get_organization(
            organization_uid="00000000-0000-0000-000000000001",
        )
        """
        _response = self._raw_client.get_organization(organization_uid, request_options=request_options)
        return _response.data

    def get_organization_balance_history(
        self,
        organization_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetOrganizationBalanceHistoryResponse:
        """
        Get Organization Balance history

        Parameters
        ----------
        organization_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationBalanceHistoryResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.get_organization_balance_history(
            organization_uid="00000000-0000-0000-000000000001",
        )
        """
        _response = self._raw_client.get_organization_balance_history(
            organization_uid, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationClient
        """
        return self._raw_client

    async def get_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationsResponse:
        """
        Get Organizations accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.get_organizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organizations(request_options=request_options)
        return _response.data

    async def get_organization(
        self, organization_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationResponse:
        """
        Get Organization Information

        Parameters
        ----------
        organization_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.get_organization(
                organization_uid="00000000-0000-0000-000000000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organization(organization_uid, request_options=request_options)
        return _response.data

    async def get_organization_balance_history(
        self,
        organization_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetOrganizationBalanceHistoryResponse:
        """
        Get Organization Balance history

        Parameters
        ----------
        organization_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationBalanceHistoryResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.get_organization_balance_history(
                organization_uid="00000000-0000-0000-000000000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organization_balance_history(
            organization_uid, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data
