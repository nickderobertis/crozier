

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client import Client
from ..types.create_client_endpoint_output import CreateClientEndpointOutput
from ..types.get_clients_request_client_id import GetClientsRequestClientId
from ..types.get_clients_request_created_at import GetClientsRequestCreatedAt
from ..types.get_clients_request_display_name import GetClientsRequestDisplayName
from ..types.json_web_key_set import JsonWebKeySet
from ..types.query_clients_endpoint_paged_result_of_output import QueryClientsEndpointPagedResultOfOutput
from .raw_client import AsyncRawClientClient, RawClientClient
from .types.get_clients_request_logic import GetClientsRequestLogic
from .types.get_clients_request_sort_item import GetClientsRequestSortItem


OMIT = typing.cast(typing.Any, ...)


class ClientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientClient
        """
        return self._raw_client

    def creates_a_new_client_for_the_current_customer(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateClientEndpointOutput:
        """
        Parameters
        ----------
        display_name : typing.Optional[str]
            An optional display name for the client.

        organization_id : typing.Optional[str]
            The organization to authorize the client for. Defaults to the caller's active organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClientEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client.creates_a_new_client_for_the_current_customer()
        """
        _response = self._raw_client.creates_a_new_client_for_the_current_customer(
            display_name=display_name, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def identity_get_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Client:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Client
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client.identity_get_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.identity_get_client(client_id, request_options=request_options)
        return _response.data

    def deletes_a_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client.deletes_a_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.deletes_a_client(client_id, request_options=request_options)
        return _response.data

    def queries_clients_for_the_current_customer(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]
        ] = None,
        client_id: typing.Optional[GetClientsRequestClientId] = None,
        display_name: typing.Optional[GetClientsRequestDisplayName] = None,
        created_at: typing.Optional[GetClientsRequestCreatedAt] = None,
        logic: typing.Optional[GetClientsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryClientsEndpointPagedResultOfOutput:
        """
        Clients are service credentials that allow automated processes to authenticate against the API.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        client_id : typing.Optional[GetClientsRequestClientId]
            Filter by client_id.

        display_name : typing.Optional[GetClientsRequestDisplayName]
            Filter by display_name.

        created_at : typing.Optional[GetClientsRequestCreatedAt]
            Filter by created_at.

        logic : typing.Optional[GetClientsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryClientsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client.queries_clients_for_the_current_customer()
        """
        _response = self._raw_client.queries_clients_for_the_current_customer(
            page=page,
            page_size=page_size,
            sort=sort,
            client_id=client_id,
            display_name=display_name,
            created_at=created_at,
            logic=logic,
            request_options=request_options,
        )
        return _response.data

    def registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        logo_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        tos_uri: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        jwks: typing.Optional[JsonWebKeySet] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Follows RFC 7591.

        Parameters
        ----------
        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        client_id : typing.Optional[str]

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        logo_uri : typing.Optional[str]

        scope : typing.Optional[str]
            String containing a space-separated list of scope values
             that the client can use when requesting access tokens.

        contacts : typing.Optional[typing.Sequence[str]]
            Array of strings representing ways to contact people responsible for this client,
             typically email addresses.

        tos_uri : typing.Optional[str]

        policy_uri : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        jwks : typing.Optional[JsonWebKeySet]
            Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client.registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol()
        """
        _response = (
            self._raw_client.registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
                redirect_uris=redirect_uris,
                grant_types=grant_types,
                response_types=response_types,
                client_id=client_id,
                client_name=client_name,
                client_uri=client_uri,
                logo_uri=logo_uri,
                scope=scope,
                contacts=contacts,
                tos_uri=tos_uri,
                policy_uri=policy_uri,
                jwks_uri=jwks_uri,
                jwks=jwks,
                request_options=request_options,
            )
        )
        return _response.data


class AsyncClientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientClient
        """
        return self._raw_client

    async def creates_a_new_client_for_the_current_customer(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateClientEndpointOutput:
        """
        Parameters
        ----------
        display_name : typing.Optional[str]
            An optional display name for the client.

        organization_id : typing.Optional[str]
            The organization to authorize the client for. Defaults to the caller's active organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClientEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client.creates_a_new_client_for_the_current_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_client_for_the_current_customer(
            display_name=display_name, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def identity_get_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Client:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Client
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client.identity_get_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.identity_get_client(client_id, request_options=request_options)
        return _response.data

    async def deletes_a_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        client_id : str
            The id of the client to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client.deletes_a_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_a_client(client_id, request_options=request_options)
        return _response.data

    async def queries_clients_for_the_current_customer(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]
        ] = None,
        client_id: typing.Optional[GetClientsRequestClientId] = None,
        display_name: typing.Optional[GetClientsRequestDisplayName] = None,
        created_at: typing.Optional[GetClientsRequestCreatedAt] = None,
        logic: typing.Optional[GetClientsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryClientsEndpointPagedResultOfOutput:
        """
        Clients are service credentials that allow automated processes to authenticate against the API.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetClientsRequestSortItem, typing.Sequence[GetClientsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        client_id : typing.Optional[GetClientsRequestClientId]
            Filter by client_id.

        display_name : typing.Optional[GetClientsRequestDisplayName]
            Filter by display_name.

        created_at : typing.Optional[GetClientsRequestCreatedAt]
            Filter by created_at.

        logic : typing.Optional[GetClientsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryClientsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client.queries_clients_for_the_current_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.queries_clients_for_the_current_customer(
            page=page,
            page_size=page_size,
            sort=sort,
            client_id=client_id,
            display_name=display_name,
            created_at=created_at,
            logic=logic,
            request_options=request_options,
        )
        return _response.data

    async def registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
        self,
        *,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        logo_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        tos_uri: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        jwks: typing.Optional[JsonWebKeySet] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Follows RFC 7591.

        Parameters
        ----------
        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        client_id : typing.Optional[str]

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        logo_uri : typing.Optional[str]

        scope : typing.Optional[str]
            String containing a space-separated list of scope values
             that the client can use when requesting access tokens.

        contacts : typing.Optional[typing.Sequence[str]]
            Array of strings representing ways to contact people responsible for this client,
             typically email addresses.

        tos_uri : typing.Optional[str]

        policy_uri : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        jwks : typing.Optional[JsonWebKeySet]
            Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client.registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol()


        asyncio.run(main())
        """
        _response = await self._raw_client.registers_a_new_client_using_the_open_id_connect_dynamic_client_registration_protocol(
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            client_id=client_id,
            client_name=client_name,
            client_uri=client_uri,
            logo_uri=logo_uri,
            scope=scope,
            contacts=contacts,
            tos_uri=tos_uri,
            policy_uri=policy_uri,
            jwks_uri=jwks_uri,
            jwks=jwks,
            request_options=request_options,
        )
        return _response.data
