

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.impersonation_token import ImpersonationToken
from ..types.resource import Resource
from .raw_client import AsyncRawImpersonationTokenObsoleteClient, RawImpersonationTokenObsoleteClient


OMIT = typing.cast(typing.Any, ...)


class ImpersonationTokenObsoleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImpersonationTokenObsoleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImpersonationTokenObsoleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImpersonationTokenObsoleteClient
        """
        return self._raw_client

    def imp_token(
        self,
        *,
        token: str,
        resources: typing.Sequence[Resource],
        refresh_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul>
        <li>Generate an impersonation credential token of a user for a set of subproject resources.</li>
        <li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token that was previously issued.

        resources : typing.Sequence[Resource]

        refresh_url : str
            A web service endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Generated a impersonation credentials token successfully.

        Examples
        --------
        from fern import FernApi, Resource

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.impersonation_token_obsolete.imp_token(
            token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
            resources=[
                Resource(
                    resource="sd://tnx01/spx01",
                    readonly=True,
                ),
                Resource(
                    resource="sd://tnx01/spx02",
                    readonly=False,
                ),
                Resource(
                    resource="sd://tnx01/spx03",
                ),
            ],
            refresh_url="https://httpstat.us/200",
        )
        """
        _response = self._raw_client.imp_token(
            token=token, resources=resources, refresh_url=refresh_url, request_options=request_options
        )
        return _response.data

    def imp_token_refresh(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImpersonationToken:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token

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
        client.impersonation_token_obsolete.imp_token_refresh(
            token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
        )
        """
        _response = self._raw_client.imp_token_refresh(token=token, request_options=request_options)
        return _response.data

    def imp_token_patch(
        self, *, token: str, refresh_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImpersonationToken:
        """
        <ul>
        <li>Patch an impersonation credential token's refresh url and generate a new impersonation token.</li>
        <li>Required roles: none</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token that was previously issued.

        refresh_url : str
            New endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Generated impersonation token successfully and its refresh url is updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.impersonation_token_obsolete.imp_token_patch(
            token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
            refresh_url="https://httpstat.us/200",
        )
        """
        _response = self._raw_client.imp_token_patch(
            token=token, refresh_url=refresh_url, request_options=request_options
        )
        return _response.data


class AsyncImpersonationTokenObsoleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImpersonationTokenObsoleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImpersonationTokenObsoleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImpersonationTokenObsoleteClient
        """
        return self._raw_client

    async def imp_token(
        self,
        *,
        token: str,
        resources: typing.Sequence[Resource],
        refresh_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImpersonationToken:
        """
        <ul>
        <li>Generate an impersonation credential token of a user for a set of subproject resources.</li>
        <li>Required roles: app.trusted</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token that was previously issued.

        resources : typing.Sequence[Resource]

        refresh_url : str
            A web service endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Generated a impersonation credentials token successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Resource

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.impersonation_token_obsolete.imp_token(
                token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
                resources=[
                    Resource(
                        resource="sd://tnx01/spx01",
                        readonly=True,
                    ),
                    Resource(
                        resource="sd://tnx01/spx02",
                        readonly=False,
                    ),
                    Resource(
                        resource="sd://tnx01/spx03",
                    ),
                ],
                refresh_url="https://httpstat.us/200",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imp_token(
            token=token, resources=resources, refresh_url=refresh_url, request_options=request_options
        )
        return _response.data

    async def imp_token_refresh(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImpersonationToken:
        """
        <ul><li>Refresh an impersonation credential token.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token

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
            await client.impersonation_token_obsolete.imp_token_refresh(
                token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imp_token_refresh(token=token, request_options=request_options)
        return _response.data

    async def imp_token_patch(
        self, *, token: str, refresh_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ImpersonationToken:
        """
        <ul>
        <li>Patch an impersonation credential token's refresh url and generate a new impersonation token.</li>
        <li>Required roles: none</li></ul>

        Parameters
        ----------
        token : str
            Impersonation token that was previously issued.

        refresh_url : str
            New endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImpersonationToken
            Generated impersonation token successfully and its refresh url is updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.impersonation_token_obsolete.imp_token_patch(
                token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
                refresh_url="https://httpstat.us/200",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imp_token_patch(
            token=token, refresh_url=refresh_url, request_options=request_options
        )
        return _response.data
