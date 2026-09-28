

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_api_key import OtoroshiModelsApiKey
from ..types.otoroshi_models_api_key_valid_until import OtoroshiModelsApiKeyValidUntil
from ..types.otoroshi_models_entity_identifier import OtoroshiModelsEntityIdentifier
from ..types.otoroshi_models_remaining_quotas import OtoroshiModelsRemainingQuotas
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

    def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsApiKey

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
            request=[OtoroshiModelsApiKey()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsApiKey

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
            request=[OtoroshiModelsApiKey()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsRemainingQuotas:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsRemainingQuotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsRemainingQuotas:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsRemainingQuotas
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
            id,
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
            id,
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsApiKey]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_api_keys_controller_create_action(
        self,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_create_action(
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
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

    async def otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsApiKey

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
                request=[OtoroshiModelsApiKey()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsApiKey], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsApiKey

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
                request=[OtoroshiModelsApiKey()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsRemainingQuotas:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsRemainingQuotas
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsRemainingQuotas:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsRemainingQuotas
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(
            id,
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
        self,
        id: str,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(
            id,
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsApiKey]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsApiKey]
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_api_keys_controller_create_action(
        self,
        *,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        constrained_services_only: typing.Optional[bool] = OMIT,
        allow_client_id_only: typing.Optional[bool] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[OtoroshiModelsApiKeyValidUntil] = OMIT,
        client_name: typing.Optional[str] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        rotation: typing.Optional[typing.Any] = OMIT,
        authorized_entities: typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsApiKey:
        """
        Parameters
        ----------
        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window

        constrained_services_only : typing.Optional[bool]
            This apikey can only be used on services that constrained their apikey routing

        allow_client_id_only : typing.Optional[bool]
            This apikey can be used juste with the client_id value

        loc : typing.Optional[typing.Any]

        restrictions : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Apikey tags

        enabled : typing.Optional[bool]
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        read_only : typing.Optional[bool]
            The apikey only allow access for GET, HEAD and OPTIONS verbs

        client_secret : typing.Optional[str]
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        valid_until : typing.Optional[OtoroshiModelsApiKeyValidUntil]
            Date until when the apikey is valid

        client_name : typing.Optional[str]
            The name of the api key, for humans ;-)

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        description : typing.Optional[str]
            Description of this apikey

        rotation : typing.Optional[typing.Any]

        authorized_entities : typing.Optional[typing.Sequence[OtoroshiModelsEntityIdentifier]]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : typing.Optional[str]
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsApiKey
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
            await client.apikeys.otoroshi_controllers_adminapi_api_keys_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_api_keys_controller_create_action(
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            loc=loc,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
            request_options=request_options,
        )
        return _response.data
