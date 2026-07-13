

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sandbox_user_company import SandboxUserCompany
from ..types.sandbox_user_company_create import SandboxUserCompanyCreate
from .raw_client import AsyncRawSandboxUserCompanyClient, RawSandboxUserCompanyClient


OMIT = typing.cast(typing.Any, ...)


class SandboxUserCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSandboxUserCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSandboxUserCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSandboxUserCompanyClient
        """
        return self._raw_client

    def create_sandbox_user_company(
        self, *, request: SandboxUserCompany, request_options: typing.Optional[RequestOptions] = None
    ) -> SandboxUserCompanyCreate:
        """
        Used to create a sandbox userCompany.

        Parameters
        ----------
        request : SandboxUserCompany

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxUserCompanyCreate
            Used to create a sandbox userCompany.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.sandbox_user_company.create_sandbox_user_company(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_sandbox_user_company(request=request, request_options=request_options)
        return _response.data


class AsyncSandboxUserCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSandboxUserCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSandboxUserCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSandboxUserCompanyClient
        """
        return self._raw_client

    async def create_sandbox_user_company(
        self, *, request: SandboxUserCompany, request_options: typing.Optional[RequestOptions] = None
    ) -> SandboxUserCompanyCreate:
        """
        Used to create a sandbox userCompany.

        Parameters
        ----------
        request : SandboxUserCompany

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SandboxUserCompanyCreate
            Used to create a sandbox userCompany.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.sandbox_user_company.create_sandbox_user_company(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sandbox_user_company(request=request, request_options=request_options)
        return _response.data
