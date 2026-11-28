

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_policies_paginated_list import AccessPoliciesPaginatedList
from ..types.access_policy import AccessPolicy
from .raw_client import AsyncRawAccessPoliciesClient, RawAccessPoliciesClient


class AccessPoliciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccessPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccessPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccessPoliciesClient
        """
        return self._raw_client

    def list_general_access_policies(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessPoliciesPaginatedList:
        """
        Returns a list of general (project/registry) access policies.

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPoliciesPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access_policies.list_general_access_policies()
        """
        _response = self._raw_client.list_general_access_policies(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_general_access_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessPolicy:
        """
        Returns a general (project/registry) policy by ID.

        Parameters
        ----------
        policy_id : str
            ID of policy to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPolicy
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access_policies.get_general_access_policy(
            policy_id="policy_id",
        )
        """
        _response = self._raw_client.get_general_access_policy(policy_id, request_options=request_options)
        return _response.data

    def list_schema_access_policies(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessPoliciesPaginatedList:
        """
        Returns a list of schema access policies.

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPoliciesPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access_policies.list_schema_access_policies()
        """
        _response = self._raw_client.list_schema_access_policies(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_schema_access_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessPolicy:
        """
        Returns a schema access policy by ID.

        Parameters
        ----------
        policy_id : str
            ID of policy to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPolicy
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access_policies.get_schema_access_policy(
            policy_id="policy_id",
        )
        """
        _response = self._raw_client.get_schema_access_policy(policy_id, request_options=request_options)
        return _response.data


class AsyncAccessPoliciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccessPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccessPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccessPoliciesClient
        """
        return self._raw_client

    async def list_general_access_policies(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessPoliciesPaginatedList:
        """
        Returns a list of general (project/registry) access policies.

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPoliciesPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access_policies.list_general_access_policies()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_general_access_policies(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_general_access_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessPolicy:
        """
        Returns a general (project/registry) policy by ID.

        Parameters
        ----------
        policy_id : str
            ID of policy to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPolicy
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access_policies.get_general_access_policy(
                policy_id="policy_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_general_access_policy(policy_id, request_options=request_options)
        return _response.data

    async def list_schema_access_policies(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccessPoliciesPaginatedList:
        """
        Returns a list of schema access policies.

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPoliciesPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access_policies.list_schema_access_policies()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_schema_access_policies(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_schema_access_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessPolicy:
        """
        Returns a schema access policy by ID.

        Parameters
        ----------
        policy_id : str
            ID of policy to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessPolicy
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access_policies.get_schema_access_policy(
                policy_id="policy_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_access_policy(policy_id, request_options=request_options)
        return _response.data
