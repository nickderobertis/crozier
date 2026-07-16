

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.deleted import Deleted
from ..types.group import Group
from ..types.patch import Patch
from ..types.quotas import Quotas
from .raw_client import AsyncRawApikeysClient, RawApikeysClient


OMIT = typing.cast(typing.Any, ...)


class ApikeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApikeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApikeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApikeysClient
        """
        return self._raw_client

    def all_api_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ApiKey]:
        """
        Get all api keys

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.all_api_keys()
        """
        _response = self._raw_client.all_api_keys(request_options=request_options)
        return _response.data

    def api_keys_from_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        group_id : str
            The api key group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_keys_from_group(
            group_id="groupId",
        )
        """
        _response = self._raw_client.api_keys_from_group(group_id, request_options=request_options)
        return _response.data

    def create_api_key_from_group(
        self,
        group_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Create a new api key for a group

        Parameters
        ----------
        group_id : str
            The api key group id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.create_api_key_from_group(
            group_id="groupId",
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
        """
        _response = self._raw_client.create_api_key_from_group(
            group_id,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    def api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_key_from_group(
            group_id="groupId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.api_key_from_group(group_id, client_id, request_options=request_options)
        return _response.data

    def update_api_key_from_group(
        self,
        group_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.update_api_key_from_group(
            group_id="groupId",
            client_id_="clientId",
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
        """
        _response = self._raw_client.update_api_key_from_group(
            group_id,
            client_id_,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    def delete_api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.delete_api_key_from_group(
            group_id="groupId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_api_key_from_group(group_id, client_id, request_options=request_options)
        return _response.data

    def patch_api_key_from_group(
        self, group_id: str, client_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.patch_api_key_from_group(
            group_id="groupId",
            client_id="clientId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_api_key_from_group(
            group_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    def api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Get the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_key_from_group_quotas(
            group_id="groupId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.api_key_from_group_quotas(group_id, client_id, request_options=request_options)
        return _response.data

    def reset_api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.reset_api_key_from_group_quotas(
            group_id="groupId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.reset_api_key_from_group_quotas(
            group_id, client_id, request_options=request_options
        )
        return _response.data

    def api_keys(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        service_id : str
            The api key service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_keys(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.api_keys(service_id, request_options=request_options)
        return _response.data

    def create_api_key(
        self,
        service_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """


        Parameters
        ----------
        service_id : str
            The api key service id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.create_api_key(
            service_id="serviceId",
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
        """
        _response = self._raw_client.create_api_key(
            service_id,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    def api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_key(
            service_id="serviceId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.api_key(service_id, client_id, request_options=request_options)
        return _response.data

    def update_api_key(
        self,
        service_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.update_api_key(
            service_id="serviceId",
            client_id_="clientId",
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
        """
        _response = self._raw_client.update_api_key(
            service_id,
            client_id_,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    def delete_api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.delete_api_key(
            service_id="serviceId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_api_key(service_id, client_id, request_options=request_options)
        return _response.data

    def patch_api_key(
        self,
        service_id: str,
        client_id: str,
        *,
        request: Patch,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.patch_api_key(
            service_id="serviceId",
            client_id="clientId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_api_key(
            service_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    def api_key_group(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Get the group of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_key_group(
            service_id="serviceId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.api_key_group(service_id, client_id, request_options=request_options)
        return _response.data

    def api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Get the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.api_key_quotas(
            service_id="serviceId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.api_key_quotas(service_id, client_id, request_options=request_options)
        return _response.data

    def reset_api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.reset_api_key_quotas(
            service_id="serviceId",
            client_id="clientId",
        )
        """
        _response = self._raw_client.reset_api_key_quotas(service_id, client_id, request_options=request_options)
        return _response.data


class AsyncApikeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApikeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApikeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApikeysClient
        """
        return self._raw_client

    async def all_api_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ApiKey]:
        """
        Get all api keys

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.all_api_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_api_keys(request_options=request_options)
        return _response.data

    async def api_keys_from_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        group_id : str
            The api key group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_keys_from_group(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_keys_from_group(group_id, request_options=request_options)
        return _response.data

    async def create_api_key_from_group(
        self,
        group_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Create a new api key for a group

        Parameters
        ----------
        group_id : str
            The api key group id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.create_api_key_from_group(
                group_id="groupId",
                authorized_entities=["a string value"],
                client_id="a string value",
                client_name="a string value",
                client_secret="a string value",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key_from_group(
            group_id,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    async def api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_key_from_group(
                group_id="groupId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_key_from_group(group_id, client_id, request_options=request_options)
        return _response.data

    async def update_api_key_from_group(
        self,
        group_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.update_api_key_from_group(
                group_id="groupId",
                client_id_="clientId",
                authorized_entities=["a string value"],
                client_id="a string value",
                client_name="a string value",
                client_secret="a string value",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_api_key_from_group(
            group_id,
            client_id_,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.delete_api_key_from_group(
                group_id="groupId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key_from_group(
            group_id, client_id, request_options=request_options
        )
        return _response.data

    async def patch_api_key_from_group(
        self, group_id: str, client_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.patch_api_key_from_group(
                group_id="groupId",
                client_id="clientId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_key_from_group(
            group_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    async def api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Get the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_key_from_group_quotas(
                group_id="groupId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_key_from_group_quotas(
            group_id, client_id, request_options=request_options
        )
        return _response.data

    async def reset_api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.reset_api_key_from_group_quotas(
                group_id="groupId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_api_key_from_group_quotas(
            group_id, client_id, request_options=request_options
        )
        return _response.data

    async def api_keys(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        service_id : str
            The api key service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_keys(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_keys(service_id, request_options=request_options)
        return _response.data

    async def create_api_key(
        self,
        service_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """


        Parameters
        ----------
        service_id : str
            The api key service id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.create_api_key(
                service_id="serviceId",
                authorized_entities=["a string value"],
                client_id="a string value",
                client_name="a string value",
                client_secret="a string value",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key(
            service_id,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    async def api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Get an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_key(
                service_id="serviceId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_key(service_id, client_id, request_options=request_options)
        return _response.data

    async def update_api_key(
        self,
        service_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.update_api_key(
                service_id="serviceId",
                client_id_="clientId",
                authorized_entities=["a string value"],
                client_id="a string value",
                client_name="a string value",
                client_secret="a string value",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_api_key(
            service_id,
            client_id_,
            authorized_entities=authorized_entities,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            enabled=enabled,
            daily_quota=daily_quota,
            metadata=metadata,
            monthly_quota=monthly_quota,
            throttling_quota=throttling_quota,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.delete_api_key(
                service_id="serviceId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(service_id, client_id, request_options=request_options)
        return _response.data

    async def patch_api_key(
        self,
        service_id: str,
        client_id: str,
        *,
        request: Patch,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.patch_api_key(
                service_id="serviceId",
                client_id="clientId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_key(
            service_id, client_id, request=request, request_options=request_options
        )
        return _response.data

    async def api_key_group(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Get the group of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_key_group(
                service_id="serviceId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_key_group(service_id, client_id, request_options=request_options)
        return _response.data

    async def api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Get the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.api_key_quotas(
                service_id="serviceId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_key_quotas(service_id, client_id, request_options=request_options)
        return _response.data

    async def reset_api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Quotas:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Quotas
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.reset_api_key_quotas(
                service_id="serviceId",
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_api_key_quotas(service_id, client_id, request_options=request_options)
        return _response.data
