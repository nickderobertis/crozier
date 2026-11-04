

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountClient, RawAccountClient
from .types.get_account_response import GetAccountResponse
from .types.get_billing_usage_response import GetBillingUsageResponse
from .types.get_team_response import GetTeamResponse
from .types.get_teams_response import GetTeamsResponse


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAccountResponse:
        """
        Get account information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccountResponse
            Account details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.get_account()
        """
        _response = self._raw_client.get_account(request_options=request_options)
        return _response.data

    def get_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetTeamsResponse:
        """
        Get team information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamsResponse
            Team information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.get_teams()
        """
        _response = self._raw_client.get_teams(request_options=request_options)
        return _response.data

    def get_team(self, team_uuid: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetTeamResponse:
        """
        Get specific team information

        Parameters
        ----------
        team_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamResponse
            Team information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.get_team(
            team_uuid="team_uuid",
        )
        """
        _response = self._raw_client.get_team(team_uuid, request_options=request_options)
        return _response.data

    def get_billing_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetBillingUsageResponse:
        """
        Get billing and usage information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingUsageResponse
            Billing information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account.get_billing_usage()
        """
        _response = self._raw_client.get_billing_usage(request_options=request_options)
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAccountResponse:
        """
        Get account information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccountResponse
            Account details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(request_options=request_options)
        return _response.data

    async def get_teams(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetTeamsResponse:
        """
        Get team information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamsResponse
            Team information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_teams()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_teams(request_options=request_options)
        return _response.data

    async def get_team(
        self, team_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTeamResponse:
        """
        Get specific team information

        Parameters
        ----------
        team_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTeamResponse
            Team information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_team(
                team_uuid="team_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_team(team_uuid, request_options=request_options)
        return _response.data

    async def get_billing_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBillingUsageResponse:
        """
        Get billing and usage information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingUsageResponse
            Billing information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_billing_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_usage(request_options=request_options)
        return _response.data
