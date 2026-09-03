

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_configuration import ClientConfiguration
from ..types.client_registration_response import ClientRegistrationResponse
from .raw_client import AsyncRawClientManagementClient, RawClientManagementClient
from .types.client_registration_request_grant_types_item import ClientRegistrationRequestGrantTypesItem
from .types.client_registration_request_id_token_signed_response_alg import (
    ClientRegistrationRequestIdTokenSignedResponseAlg,
)
from .types.client_registration_request_industry_type import ClientRegistrationRequestIndustryType
from .types.client_registration_request_response_types_item import ClientRegistrationRequestResponseTypesItem
from .types.client_registration_request_token_endpoint_auth_method import (
    ClientRegistrationRequestTokenEndpointAuthMethod,
)
from .types.client_registration_request_token_endpoint_auth_signing_alg import (
    ClientRegistrationRequestTokenEndpointAuthSigningAlg,
)
from .types.client_update_request_industry_type import ClientUpdateRequestIndustryType


OMIT = typing.cast(typing.Any, ...)


class ClientManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientManagementClient
        """
        return self._raw_client

    def register_client(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        grant_types: typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]] = OMIT,
        response_types: typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        token_endpoint_auth_method: typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod] = OMIT,
        token_endpoint_auth_signing_alg: typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg] = OMIT,
        require_pushed_authorization_requests: typing.Optional[bool] = OMIT,
        require_signed_request_object: typing.Optional[bool] = OMIT,
        id_token_signed_response_alg: typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientRegistrationRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientRegistrationResponse:
        """
        RFC 7591 compliant dynamic client registration with FAPI 2.0 enhancements.

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]
            Authorized redirect URIs

        client_name : typing.Optional[str]
            Human-readable client name

        client_uri : typing.Optional[str]
            Client website URL

        grant_types : typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]]

        response_types : typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]]

        scope : typing.Optional[str]

        token_endpoint_auth_method : typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod]

        token_endpoint_auth_signing_alg : typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg]

        require_pushed_authorization_requests : typing.Optional[bool]

        require_signed_request_object : typing.Optional[bool]

        id_token_signed_response_alg : typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg]

        jwks_uri : typing.Optional[str]
            URL for client's JWK Set

        industry_type : typing.Optional[ClientRegistrationRequestIndustryType]

        finma_license : typing.Optional[str]
            FINMA license number if applicable

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientRegistrationResponse
            Client registered successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_management.register_client(
            redirect_uris=["redirect_uris"],
        )
        """
        _response = self._raw_client.register_client(
            redirect_uris=redirect_uris,
            client_name=client_name,
            client_uri=client_uri,
            grant_types=grant_types,
            response_types=response_types,
            scope=scope,
            token_endpoint_auth_method=token_endpoint_auth_method,
            token_endpoint_auth_signing_alg=token_endpoint_auth_signing_alg,
            require_pushed_authorization_requests=require_pushed_authorization_requests,
            require_signed_request_object=require_signed_request_object,
            id_token_signed_response_alg=id_token_signed_response_alg,
            jwks_uri=jwks_uri,
            industry_type=industry_type,
            finma_license=finma_license,
            swiss_qr_support=swiss_qr_support,
            request_options=request_options,
        )
        return _response.data

    def get_client_configuration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClientConfiguration:
        """
        Retrieve client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientConfiguration
            Client configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_management.get_client_configuration(
            client_id="client_id",
        )
        """
        _response = self._raw_client.get_client_configuration(client_id, request_options=request_options)
        return _response.data

    def update_client_configuration(
        self,
        client_id: str,
        *,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientUpdateRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientConfiguration:
        """
        Update client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        scope : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        industry_type : typing.Optional[ClientUpdateRequestIndustryType]

        finma_license : typing.Optional[str]

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientConfiguration
            Client updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_management.update_client_configuration(
            client_id="client_id",
        )
        """
        _response = self._raw_client.update_client_configuration(
            client_id,
            client_name=client_name,
            client_uri=client_uri,
            redirect_uris=redirect_uris,
            scope=scope,
            jwks_uri=jwks_uri,
            industry_type=industry_type,
            finma_license=finma_license,
            swiss_qr_support=swiss_qr_support,
            request_options=request_options,
        )
        return _response.data

    def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete client registration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

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
        client.client_management.delete_client(
            client_id="client_id",
        )
        """
        _response = self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data


class AsyncClientManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientManagementClient
        """
        return self._raw_client

    async def register_client(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        grant_types: typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]] = OMIT,
        response_types: typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        token_endpoint_auth_method: typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod] = OMIT,
        token_endpoint_auth_signing_alg: typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg] = OMIT,
        require_pushed_authorization_requests: typing.Optional[bool] = OMIT,
        require_signed_request_object: typing.Optional[bool] = OMIT,
        id_token_signed_response_alg: typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientRegistrationRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientRegistrationResponse:
        """
        RFC 7591 compliant dynamic client registration with FAPI 2.0 enhancements.

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]
            Authorized redirect URIs

        client_name : typing.Optional[str]
            Human-readable client name

        client_uri : typing.Optional[str]
            Client website URL

        grant_types : typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]]

        response_types : typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]]

        scope : typing.Optional[str]

        token_endpoint_auth_method : typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod]

        token_endpoint_auth_signing_alg : typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg]

        require_pushed_authorization_requests : typing.Optional[bool]

        require_signed_request_object : typing.Optional[bool]

        id_token_signed_response_alg : typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg]

        jwks_uri : typing.Optional[str]
            URL for client's JWK Set

        industry_type : typing.Optional[ClientRegistrationRequestIndustryType]

        finma_license : typing.Optional[str]
            FINMA license number if applicable

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientRegistrationResponse
            Client registered successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_management.register_client(
                redirect_uris=["redirect_uris"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_client(
            redirect_uris=redirect_uris,
            client_name=client_name,
            client_uri=client_uri,
            grant_types=grant_types,
            response_types=response_types,
            scope=scope,
            token_endpoint_auth_method=token_endpoint_auth_method,
            token_endpoint_auth_signing_alg=token_endpoint_auth_signing_alg,
            require_pushed_authorization_requests=require_pushed_authorization_requests,
            require_signed_request_object=require_signed_request_object,
            id_token_signed_response_alg=id_token_signed_response_alg,
            jwks_uri=jwks_uri,
            industry_type=industry_type,
            finma_license=finma_license,
            swiss_qr_support=swiss_qr_support,
            request_options=request_options,
        )
        return _response.data

    async def get_client_configuration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClientConfiguration:
        """
        Retrieve client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientConfiguration
            Client configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_management.get_client_configuration(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_client_configuration(client_id, request_options=request_options)
        return _response.data

    async def update_client_configuration(
        self,
        client_id: str,
        *,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientUpdateRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientConfiguration:
        """
        Update client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        scope : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        industry_type : typing.Optional[ClientUpdateRequestIndustryType]

        finma_license : typing.Optional[str]

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientConfiguration
            Client updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_management.update_client_configuration(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client_configuration(
            client_id,
            client_name=client_name,
            client_uri=client_uri,
            redirect_uris=redirect_uris,
            scope=scope,
            jwks_uri=jwks_uri,
            industry_type=industry_type,
            finma_license=finma_license,
            swiss_qr_support=swiss_qr_support,
            request_options=request_options,
        )
        return _response.data

    async def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete client registration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

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
            await client.client_management.delete_client(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data
