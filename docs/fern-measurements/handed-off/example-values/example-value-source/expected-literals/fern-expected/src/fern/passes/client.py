

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPassesClient, RawPassesClient
from .types.issue_form_pass_request_grant import IssueFormPassRequestGrant
from .types.issue_form_pass_request_tier import IssueFormPassRequestTier
from .types.issue_form_pass_response import IssueFormPassResponse
from .types.issue_pass_request_grant import IssuePassRequestGrant
from .types.issue_pass_response import IssuePassResponse


OMIT = typing.cast(typing.Any, ...)


class PassesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPassesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPassesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPassesClient
        """
        return self._raw_client

    def issue_pass(
        self, *, grant: IssuePassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IssuePassResponse:
        """
        A media type's named example for an enum field.

        Parameters
        ----------
        grant : IssuePassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssuePassResponse
            Issued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.passes.issue_pass(
            grant="overnight-stay",
            holder="Kerensa",
        )
        """
        _response = self._raw_client.issue_pass(grant=grant, holder=holder, request_options=request_options)
        return _response.data

    def issue_form_pass(
        self,
        *,
        grant: IssueFormPassRequestGrant,
        holder: str,
        tier: IssueFormPassRequestTier,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueFormPassResponse:
        """
        A form body's named example for an enum field.

        Parameters
        ----------
        grant : IssueFormPassRequestGrant

        holder : str

        tier : IssueFormPassRequestTier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssueFormPassResponse
            Issued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.passes.issue_form_pass(
            grant="overnight-stay",
            holder="Kerensa",
            tier="standard",
        )
        """
        _response = self._raw_client.issue_form_pass(
            grant=grant, holder=holder, tier=tier, request_options=request_options
        )
        return _response.data


class AsyncPassesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPassesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPassesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPassesClient
        """
        return self._raw_client

    async def issue_pass(
        self, *, grant: IssuePassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IssuePassResponse:
        """
        A media type's named example for an enum field.

        Parameters
        ----------
        grant : IssuePassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssuePassResponse
            Issued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.passes.issue_pass(
                grant="overnight-stay",
                holder="Kerensa",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_pass(grant=grant, holder=holder, request_options=request_options)
        return _response.data

    async def issue_form_pass(
        self,
        *,
        grant: IssueFormPassRequestGrant,
        holder: str,
        tier: IssueFormPassRequestTier,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueFormPassResponse:
        """
        A form body's named example for an enum field.

        Parameters
        ----------
        grant : IssueFormPassRequestGrant

        holder : str

        tier : IssueFormPassRequestTier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssueFormPassResponse
            Issued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.passes.issue_form_pass(
                grant="overnight-stay",
                holder="Kerensa",
                tier="standard",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_form_pass(
            grant=grant, holder=holder, tier=tier, request_options=request_options
        )
        return _response.data
