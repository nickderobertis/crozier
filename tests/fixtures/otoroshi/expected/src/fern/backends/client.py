

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_next_models_stored_ng_backend import OtoroshiNextModelsStoredNgBackend
from .raw_client import AsyncRawBackendsClient, RawBackendsClient


OMIT = typing.cast(typing.Any, ...)


class BackendsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBackendsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBackendsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBackendsClient
        """
        return self._raw_client

    def otoroshi_next_controllers_adminapi_ng_backends_controller_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_form()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_form(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend()
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend(
                request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsStoredNgBackend],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsStoredNgBackend]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsStoredNgBackend

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
            request=[OtoroshiNextModelsStoredNgBackend()],
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsStoredNgBackend],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsStoredNgBackend]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsStoredNgBackend

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
            request=[OtoroshiNextModelsStoredNgBackend()],
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action(
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
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
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
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
            id_,
            description=description,
            tags=tags,
            metadata=metadata,
            backend=backend,
            name=name,
            loc=loc,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
            id_,
            description=description,
            tags=tags,
            metadata=metadata,
            backend=backend,
            name=name,
            loc=loc,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsStoredNgBackend]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsStoredNgBackend]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_backends_controller_create_action(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_create_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_create_action(
            description=description,
            tags=tags,
            metadata=metadata,
            backend=backend,
            name=name,
            loc=loc,
            id=id,
            request_options=request_options,
        )
        return _response.data


class AsyncBackendsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBackendsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBackendsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBackendsClient
        """
        return self._raw_client

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_form(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_initiate_stored_ng_backend(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsStoredNgBackend],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsStoredNgBackend]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsStoredNgBackend

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
                request=[OtoroshiNextModelsStoredNgBackend()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsStoredNgBackend],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsStoredNgBackend]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsStoredNgBackend

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
                request=[OtoroshiNextModelsStoredNgBackend()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action(
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_update_entity_action(
                id_,
                description=description,
                tags=tags,
                metadata=metadata,
                backend=backend,
                name=name,
                loc=loc,
                id=id,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_delete_entity_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_patch_entity_action(
                id_,
                description=description,
                tags=tags,
                metadata=metadata,
                backend=backend,
                name=name,
                loc=loc,
                id=id,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsStoredNgBackend]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsStoredNgBackend]
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_backends_controller_create_action(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        backend: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsStoredNgBackend:
        """
        Parameters
        ----------
        description : typing.Optional[str]
            The description of the backend

        tags : typing.Optional[typing.Sequence[str]]
            The tags of the backend

        metadata : typing.Optional[typing.Dict[str, str]]
            The metadata of the backend

        backend : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of the backend

        loc : typing.Optional[typing.Any]

        id : typing.Optional[str]
            The id of the backend

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsStoredNgBackend
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
            await client.backends.otoroshi_next_controllers_adminapi_ng_backends_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_backends_controller_create_action(
            description=description,
            tags=tags,
            metadata=metadata,
            backend=backend,
            name=name,
            loc=loc,
            id=id,
            request_options=request_options,
        )
        return _response.data
