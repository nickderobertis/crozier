

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.claim_status import ClaimStatus
from ..types.user_dto import UserDto
from .raw_client import AsyncRawClaimClient, RawClaimClient


class ClaimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClaimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClaimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClaimClient
        """
        return self._raw_client

    def get_claim_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ClaimStatus:
        """
        Check whether this server has already been claimed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimStatus
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.claim.get_claim_status()
        """
        _response = self._raw_client.get_claim_status(request_options=request_options)
        return _response.data

    def server(
        self, *, komga_email: str, komga_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserDto:
        """
        Creates an admin user with the provided credentials.

        Parameters
        ----------
        komga_email : str

        komga_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.claim.server(
            komga_email="X-Komga-Email",
            komga_password="X-Komga-Password",
        )
        """
        _response = self._raw_client.server(
            komga_email=komga_email, komga_password=komga_password, request_options=request_options
        )
        return _response.data


class AsyncClaimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClaimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClaimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClaimClient
        """
        return self._raw_client

    async def get_claim_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ClaimStatus:
        """
        Check whether this server has already been claimed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimStatus
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.claim.get_claim_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_claim_status(request_options=request_options)
        return _response.data

    async def server(
        self, *, komga_email: str, komga_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserDto:
        """
        Creates an admin user with the provided credentials.

        Parameters
        ----------
        komga_email : str

        komga_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.claim.server(
                komga_email="X-Komga-Email",
                komga_password="X-Komga-Password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.server(
            komga_email=komga_email, komga_password=komga_password, request_options=request_options
        )
        return _response.data
