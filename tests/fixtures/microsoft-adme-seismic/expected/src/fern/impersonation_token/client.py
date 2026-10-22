

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.impersonation_token import ImpersonationToken
from ..types.resource import Resource
from .raw_client import AsyncRawImpersonationTokenClient, RawImpersonationTokenClient


OMIT = typing.cast(typing.Any, ...)


class ImpersonationTokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImpersonationTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImpersonationTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImpersonationTokenClient
        """
        return self._raw_client

    def generate(
        self,
        *,
        user_token: str,
        resources: typing.Sequence[Resource],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul><li>Generate a credential token to impersonate user access for a set of subproject resources.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        user_token : str
            The credential of the user to impersonate.

        resources : typing.Sequence[Resource]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            The impersonation token has been successfully created.

        Examples
        --------
        from fern import FernApi, Resource

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.impersonation_token.generate(
            user_token="user-token",
            resources=[
                Resource(
                    resource="sd://tnx01/spx01",
                    readonly=True,
                ),
                Resource(
                    resource="sd://tnx01/spx02",
                    readonly=False,
                ),
            ],
            metadata={"jobId": 1234},
        )
        """
        _response = self._raw_client.generate(
            user_token=user_token, resources=resources, metadata=metadata, request_options=request_options
        )
        return _response.data

    def refresh(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        impersonation_token : str
            The impersonation token to refresh.

        impersonation_token_context : str
            The impersonation token context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Refreshed impersonation credential token successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.impersonation_token.refresh(
            impersonation_token="impersonation-token",
            impersonation_token_context="impersonation-token-context",
        )
        """
        _response = self._raw_client.refresh(
            impersonation_token=impersonation_token,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data


class AsyncImpersonationTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImpersonationTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImpersonationTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImpersonationTokenClient
        """
        return self._raw_client

    async def generate(
        self,
        *,
        user_token: str,
        resources: typing.Sequence[Resource],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul><li>Generate a credential token to impersonate user access for a set of subproject resources.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        user_token : str
            The credential of the user to impersonate.

        resources : typing.Sequence[Resource]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            The impersonation token has been successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Resource

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.impersonation_token.generate(
                user_token="user-token",
                resources=[
                    Resource(
                        resource="sd://tnx01/spx01",
                        readonly=True,
                    ),
                    Resource(
                        resource="sd://tnx01/spx02",
                        readonly=False,
                    ),
                ],
                metadata={"jobId": 1234},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate(
            user_token=user_token, resources=resources, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def refresh(
        self,
        *,
        impersonation_token: str,
        impersonation_token_context: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        impersonation_token : str
            The impersonation token to refresh.

        impersonation_token_context : str
            The impersonation token context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Refreshed impersonation credential token successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.impersonation_token.refresh(
                impersonation_token="impersonation-token",
                impersonation_token_context="impersonation-token-context",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh(
            impersonation_token=impersonation_token,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data
