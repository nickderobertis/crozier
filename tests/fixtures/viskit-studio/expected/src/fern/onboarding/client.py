

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.onboarding_needed_response import OnboardingNeededResponse
from .raw_client import AsyncRawOnboardingClient, RawOnboardingClient


class OnboardingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOnboardingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOnboardingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOnboardingClient
        """
        return self._raw_client

    def get_onboarding_needed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OnboardingNeededResponse:
        """
        Return whether onboarding is needed for this workspace.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OnboardingNeededResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.onboarding.get_onboarding_needed()
        """
        _response = self._raw_client.get_onboarding_needed(request_options=request_options)
        return _response.data


class AsyncOnboardingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOnboardingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOnboardingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOnboardingClient
        """
        return self._raw_client

    async def get_onboarding_needed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OnboardingNeededResponse:
        """
        Return whether onboarding is needed for this workspace.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OnboardingNeededResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.onboarding.get_onboarding_needed()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_onboarding_needed(request_options=request_options)
        return _response.data
