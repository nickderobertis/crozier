

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.api_key_scope import ApiKeyScope
from ..types.api_response import ApiResponse
from .raw_client import AsyncRawApiKeysClient, RawApiKeysClient
from .types.add_api_key_response import AddApiKeyResponse
from .types.get_api_keys_request_order import GetApiKeysRequestOrder


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

    def get_api_keys(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetApiKeysRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApiKey]:
        """
        Returns an array with one or more API keys. For security reasons hashed keys are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetApiKeysRequestOrder]
            Ordering API keys by id. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.api_keys.get_api_keys()
        """
        _response = self._raw_client.get_api_keys(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_api_key(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddApiKeyResponse:
        """
        Adds a new API key

        Parameters
        ----------
        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddApiKeyResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.api_keys.add_api_key()
        """
        _response = self._raw_client.add_api_key(
            id=id,
            name=name,
            key=key,
            scope=scope,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            description=description,
            user=user,
            admin=admin,
            request_options=request_options,
        )
        return _response.data

    def get_api_key_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKey:
        """
        Returns the API key with the given id, if it exists. For security reasons the hashed key is omitted in the response

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.api_keys.get_api_key_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_api_key_by_id(id, request_options=request_options)
        return _response.data

    def update_api_key(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing API key. You cannot update the key itself, the creation date and the last use

        Parameters
        ----------
        id_ : str
            the key id

        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.api_keys.update_api_key(
            id_="id",
        )
        """
        _response = self._raw_client.update_api_key(
            id_,
            id=id,
            name=name,
            key=key,
            scope=scope,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            description=description,
            user=user,
            admin=admin,
            request_options=request_options,
        )
        return _response.data

    def delete_api_key(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing API key

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.api_keys.delete_api_key(
            id="id",
        )
        """
        _response = self._raw_client.delete_api_key(id, request_options=request_options)
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

    async def get_api_keys(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetApiKeysRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ApiKey]:
        """
        Returns an array with one or more API keys. For security reasons hashed keys are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetApiKeysRequestOrder]
            Ordering API keys by id. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.api_keys.get_api_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_keys(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_api_key(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddApiKeyResponse:
        """
        Adds a new API key

        Parameters
        ----------
        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddApiKeyResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.api_keys.add_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_api_key(
            id=id,
            name=name,
            key=key,
            scope=scope,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            description=description,
            user=user,
            admin=admin,
            request_options=request_options,
        )
        return _response.data

    async def get_api_key_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKey:
        """
        Returns the API key with the given id, if it exists. For security reasons the hashed key is omitted in the response

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.api_keys.get_api_key_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key_by_id(id, request_options=request_options)
        return _response.data

    async def update_api_key(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        scope: typing.Optional[ApiKeyScope] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        admin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing API key. You cannot update the key itself, the creation date and the last use

        Parameters
        ----------
        id_ : str
            the key id

        id : typing.Optional[str]
            unique key identifier

        name : typing.Optional[str]
            User friendly key name

        key : typing.Optional[str]
            We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys

        scope : typing.Optional[ApiKeyScope]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        expires_at : typing.Optional[int]
            expiration time as unix timestamp in milliseconds

        description : typing.Optional[str]
            optional description

        user : typing.Optional[str]
            username associated with this API key. If empty and the scope is "user scope" the key can impersonate any user

        admin : typing.Optional[str]
            admin associated with this API key. If empty and the scope is "admin scope" the key can impersonate any admin

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.api_keys.update_api_key(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_api_key(
            id_,
            id=id,
            name=name,
            key=key,
            scope=scope,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            description=description,
            user=user,
            admin=admin,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_key(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing API key

        Parameters
        ----------
        id : str
            the key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(id, request_options=request_options)
        return _response.data
