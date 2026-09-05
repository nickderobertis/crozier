

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.create_service_token_output import CreateServiceTokenOutput
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.service_token import ServiceToken
from ..types.service_token_id_param import ServiceTokenIdParam
from ..types.service_token_name import ServiceTokenName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawServiceTokensClient, RawServiceTokensClient
from .types.get_service_token_response import GetServiceTokenResponse


OMIT = typing.cast(typing.Any, ...)


class ServiceTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceTokensClient
        """
        return self._raw_client

    def get_service_token(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        service_token_name: typing.Optional[ServiceTokenName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetServiceTokenResponse:
        """
        List out all service_tokens. The service_tokens are sorted by creation date, with the most recently-created service_tokens coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        service_token_name : typing.Optional[ServiceTokenName]
            Name of the service_token to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServiceTokenResponse
            Returns a list of service_token objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.get_service_token()
        """
        _response = self._raw_client.get_service_token(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            service_token_name=service_token_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_service_token(
        self,
        *,
        name: str,
        service_account_id: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateServiceTokenOutput:
        """
        Create a new service_token. It is possible to have multiple API keys with the same name. There is no de-duplication

        Parameters
        ----------
        name : str
            Name of the service token. Does not have to be unique

        service_account_id : str
            The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateServiceTokenOutput
            Returns an object containing the raw service token. This is the only time the raw API key will be exposed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.post_service_token(
            name="name",
            service_account_id="service_account_id",
        )
        """
        _response = self._raw_client.post_service_token(
            name=name, service_account_id=service_account_id, org_name=org_name, request_options=request_options
        )
        return _response.data

    def put_service_token(
        self,
        *,
        name: str,
        service_account_id: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateServiceTokenOutput:
        """
        Create or replace service_token. If there is an existing service_token with the same name as the one specified in the request, will replace the existing service_token with the provided fields

        Parameters
        ----------
        name : str
            Name of the service token. Does not have to be unique

        service_account_id : str
            The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateServiceTokenOutput
            Returns an object containing the raw service token. This is the only time the raw API key will be exposed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.put_service_token(
            name="name",
            service_account_id="service_account_id",
        )
        """
        _response = self._raw_client.put_service_token(
            name=name, service_account_id=service_account_id, org_name=org_name, request_options=request_options
        )
        return _response.data

    def delete_service_token(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> ServiceToken:
        """
        Delete a single service_token

        Parameters
        ----------
        id : str
            Unique identifier for the service token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the deleted service_token object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.delete_service_token(
            id="id",
        )
        """
        _response = self._raw_client.delete_service_token(id=id, request_options=request_options)
        return _response.data

    def get_service_token_id(
        self, service_token_id: ServiceTokenIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceToken:
        """
        Get a service_token object by its id

        Parameters
        ----------
        service_token_id : ServiceTokenIdParam
            ServiceToken id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the service_token object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.get_service_token_id(
            service_token_id="service_token_id",
        )
        """
        _response = self._raw_client.get_service_token_id(service_token_id, request_options=request_options)
        return _response.data

    def delete_service_token_id(
        self, service_token_id: ServiceTokenIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceToken:
        """
        Delete a service_token object by its id

        Parameters
        ----------
        service_token_id : ServiceTokenIdParam
            ServiceToken id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the deleted service_token object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service_tokens.delete_service_token_id(
            service_token_id="service_token_id",
        )
        """
        _response = self._raw_client.delete_service_token_id(service_token_id, request_options=request_options)
        return _response.data


class AsyncServiceTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceTokensClient
        """
        return self._raw_client

    async def get_service_token(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        service_token_name: typing.Optional[ServiceTokenName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetServiceTokenResponse:
        """
        List out all service_tokens. The service_tokens are sorted by creation date, with the most recently-created service_tokens coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        service_token_name : typing.Optional[ServiceTokenName]
            Name of the service_token to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServiceTokenResponse
            Returns a list of service_token objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.get_service_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_token(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            service_token_name=service_token_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_service_token(
        self,
        *,
        name: str,
        service_account_id: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateServiceTokenOutput:
        """
        Create a new service_token. It is possible to have multiple API keys with the same name. There is no de-duplication

        Parameters
        ----------
        name : str
            Name of the service token. Does not have to be unique

        service_account_id : str
            The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateServiceTokenOutput
            Returns an object containing the raw service token. This is the only time the raw API key will be exposed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.post_service_token(
                name="name",
                service_account_id="service_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_service_token(
            name=name, service_account_id=service_account_id, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def put_service_token(
        self,
        *,
        name: str,
        service_account_id: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateServiceTokenOutput:
        """
        Create or replace service_token. If there is an existing service_token with the same name as the one specified in the request, will replace the existing service_token with the provided fields

        Parameters
        ----------
        name : str
            Name of the service token. Does not have to be unique

        service_account_id : str
            The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateServiceTokenOutput
            Returns an object containing the raw service token. This is the only time the raw API key will be exposed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.put_service_token(
                name="name",
                service_account_id="service_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_service_token(
            name=name, service_account_id=service_account_id, org_name=org_name, request_options=request_options
        )
        return _response.data

    async def delete_service_token(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceToken:
        """
        Delete a single service_token

        Parameters
        ----------
        id : str
            Unique identifier for the service token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the deleted service_token object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.delete_service_token(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service_token(id=id, request_options=request_options)
        return _response.data

    async def get_service_token_id(
        self, service_token_id: ServiceTokenIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceToken:
        """
        Get a service_token object by its id

        Parameters
        ----------
        service_token_id : ServiceTokenIdParam
            ServiceToken id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the service_token object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.get_service_token_id(
                service_token_id="service_token_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_token_id(service_token_id, request_options=request_options)
        return _response.data

    async def delete_service_token_id(
        self, service_token_id: ServiceTokenIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceToken:
        """
        Delete a service_token object by its id

        Parameters
        ----------
        service_token_id : ServiceTokenIdParam
            ServiceToken id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceToken
            Returns the deleted service_token object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service_tokens.delete_service_token_id(
                service_token_id="service_token_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service_token_id(service_token_id, request_options=request_options)
        return _response.data
