

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_org_token import CreatedOrgToken
from ..types.list_org_tokens import ListOrgTokens
from ..types.org_id import OrgId
from ..types.org_token_name import OrgTokenName
from .raw_client import AsyncRawOrgTokensV1Client, RawOrgTokensV1Client


OMIT = typing.cast(typing.Any, ...)


class OrgTokensV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrgTokensV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrgTokensV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrgTokensV1Client
        """
        return self._raw_client

    def get_org_tokens(
        self, org_id: OrgId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgTokens:
        """
        List all organization tokens for a given org.

        Parameters
        ----------
        org_id : OrgId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgTokens
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.org_tokens_v1.get_org_tokens(
            org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
        )
        """
        _response = self._raw_client.get_org_tokens(org_id, request_options=request_options)
        return _response.data

    def create_org_token(
        self, org_id: OrgId, *, name: OrgTokenName, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatedOrgToken:
        """
        Create a new organization token.

        Parameters
        ----------
        org_id : OrgId

        name : OrgTokenName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedOrgToken


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.org_tokens_v1.create_org_token(
            org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
            name="ci-token",
        )
        """
        _response = self._raw_client.create_org_token(org_id, name=name, request_options=request_options)
        return _response.data

    def revoke_org_token(
        self, org_id: OrgId, org_token_id: OrgId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Revoke an organization token.

        Parameters
        ----------
        org_id : OrgId

        org_token_id : OrgId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.org_tokens_v1.revoke_org_token(
            org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
            org_token_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
        )
        """
        _response = self._raw_client.revoke_org_token(org_id, org_token_id, request_options=request_options)
        return _response.data


class AsyncOrgTokensV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrgTokensV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrgTokensV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrgTokensV1Client
        """
        return self._raw_client

    async def get_org_tokens(
        self, org_id: OrgId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgTokens:
        """
        List all organization tokens for a given org.

        Parameters
        ----------
        org_id : OrgId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgTokens
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.org_tokens_v1.get_org_tokens(
                org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_org_tokens(org_id, request_options=request_options)
        return _response.data

    async def create_org_token(
        self, org_id: OrgId, *, name: OrgTokenName, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatedOrgToken:
        """
        Create a new organization token.

        Parameters
        ----------
        org_id : OrgId

        name : OrgTokenName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedOrgToken


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.org_tokens_v1.create_org_token(
                org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
                name="ci-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_org_token(org_id, name=name, request_options=request_options)
        return _response.data

    async def revoke_org_token(
        self, org_id: OrgId, org_token_id: OrgId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Revoke an organization token.

        Parameters
        ----------
        org_id : OrgId

        org_token_id : OrgId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.org_tokens_v1.revoke_org_token(
                org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
                org_token_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_org_token(org_id, org_token_id, request_options=request_options)
        return _response.data
