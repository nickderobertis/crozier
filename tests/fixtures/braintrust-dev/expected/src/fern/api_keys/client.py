

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.api_key_id_param import ApiKeyIdParam
from ..types.api_key_name import ApiKeyName
from ..types.app_limit_param import AppLimitParam
from ..types.create_api_key_output import CreateApiKeyOutput
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawApiKeysClient, RawApiKeysClient
from .types.get_api_key_response import GetApiKeyResponse


OMIT = typing.cast(typing.Any, ...)


class ApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiKeysClient
        """
        return self._raw_client

    def get_api_key(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        api_key_name: typing.Optional[ApiKeyName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiKeyResponse:
        """
        List out all api_keys. The api_keys are sorted by creation date, with the most recently-created api_keys coming first

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

        api_key_name : typing.Optional[ApiKeyName]
            Name of the api_key to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiKeyResponse
            Returns a list of api_key objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.get_api_key()
        """
        _response = self._raw_client.get_api_key(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            api_key_name=api_key_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_api_key(
        self,
        *,
        name: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApiKeyOutput:
        """
        Create a new api_key. It is possible to have multiple API keys with the same name. There is no de-duplication

        Parameters
        ----------
        name : str
            Name of the api key. Does not have to be unique

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the API key belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApiKeyOutput
            Returns an object containing the raw API key. This is the only time the raw API key will be exposed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.post_api_key(
            name="name",
        )
        """
        _response = self._raw_client.post_api_key(name=name, org_name=org_name, request_options=request_options)
        return _response.data

    def get_api_key_id(
        self, api_key_id: ApiKeyIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api_key object by its id

        Parameters
        ----------
        api_key_id : ApiKeyIdParam
            ApiKey id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Returns the api_key object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.get_api_key_id(
            api_key_id="api_key_id",
        )
        """
        _response = self._raw_client.get_api_key_id(api_key_id, request_options=request_options)
        return _response.data

    def delete_api_key_id(
        self, api_key_id: ApiKeyIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Delete an api_key object by its id

        Parameters
        ----------
        api_key_id : ApiKeyIdParam
            ApiKey id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Returns the deleted api_key object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.delete_api_key_id(
            api_key_id="api_key_id",
        )
        """
        _response = self._raw_client.delete_api_key_id(api_key_id, request_options=request_options)
        return _response.data


class AsyncApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiKeysClient
        """
        return self._raw_client

    async def get_api_key(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        api_key_name: typing.Optional[ApiKeyName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiKeyResponse:
        """
        List out all api_keys. The api_keys are sorted by creation date, with the most recently-created api_keys coming first

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

        api_key_name : typing.Optional[ApiKeyName]
            Name of the api_key to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiKeyResponse
            Returns a list of api_key objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.get_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            api_key_name=api_key_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_api_key(
        self,
        *,
        name: str,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApiKeyOutput:
        """
        Create a new api_key. It is possible to have multiple API keys with the same name. There is no de-duplication

        Parameters
        ----------
        name : str
            Name of the api key. Does not have to be unique

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the API key belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApiKeyOutput
            Returns an object containing the raw API key. This is the only time the raw API key will be exposed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.post_api_key(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_key(name=name, org_name=org_name, request_options=request_options)
        return _response.data

    async def get_api_key_id(
        self, api_key_id: ApiKeyIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api_key object by its id

        Parameters
        ----------
        api_key_id : ApiKeyIdParam
            ApiKey id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Returns the api_key object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.get_api_key_id(
                api_key_id="api_key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key_id(api_key_id, request_options=request_options)
        return _response.data

    async def delete_api_key_id(
        self, api_key_id: ApiKeyIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Delete an api_key object by its id

        Parameters
        ----------
        api_key_id : ApiKeyIdParam
            ApiKey id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Returns the deleted api_key object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key_id(
                api_key_id="api_key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key_id(api_key_id, request_options=request_options)
        return _response.data
