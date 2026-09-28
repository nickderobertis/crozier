

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
from ..types.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
from ..types.otoroshi_models_global_jwt_verifier_type import OtoroshiModelsGlobalJwtVerifierType
from .raw_client import AsyncRawJwtVerifiersClient, RawJwtVerifiersClient


OMIT = typing.cast(typing.Any, ...)


class JwtVerifiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJwtVerifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJwtVerifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJwtVerifiersClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsGlobalJwtVerifier],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsGlobalJwtVerifier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsGlobalJwtVerifier

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
            request=[OtoroshiModelsGlobalJwtVerifier()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsGlobalJwtVerifier],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsGlobalJwtVerifier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsGlobalJwtVerifier

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
            request=[OtoroshiModelsGlobalJwtVerifier()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action(
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
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
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
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
        self,
        id_: str,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
            id_,
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
        self,
        id_: str,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
            id_,
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsGlobalJwtVerifier]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsGlobalJwtVerifier]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(
        self,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data


class AsyncJwtVerifiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJwtVerifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJwtVerifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJwtVerifiersClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsGlobalJwtVerifier],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsGlobalJwtVerifier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsGlobalJwtVerifier

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
                request=[OtoroshiModelsGlobalJwtVerifier()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsGlobalJwtVerifier],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsGlobalJwtVerifier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsGlobalJwtVerifier

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
                request=[OtoroshiModelsGlobalJwtVerifier()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action(
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
        self,
        id_: str,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(
            id_,
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
        self,
        id_: str,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(
            id_,
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsGlobalJwtVerifier]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsGlobalJwtVerifier]
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(
        self,
        *,
        type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = OMIT,
        desc: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        source: typing.Optional[typing.Any] = OMIT,
        algo_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        strategy: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsGlobalJwtVerifier:
        """
        Parameters
        ----------
        type : typing.Optional[OtoroshiModelsGlobalJwtVerifierType]
            the kind of verifier

        desc : typing.Optional[str]
            Verifier description

        name : typing.Optional[str]
            Verifier name

        strict : typing.Optional[bool]
            Does it fail if JWT not found

        source : typing.Optional[typing.Any]

        algo_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            Algo settings of the verifier

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        id : typing.Optional[str]
            Verifier id

        loc : typing.Optional[typing.Any]

        strategy : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalJwtVerifier
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
            await client.jwt_verifiers.otoroshi_controllers_adminapi_jwt_verifier_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(
            type=type,
            desc=desc,
            name=name,
            strict=strict,
            source=source,
            algo_settings=algo_settings,
            tags=tags,
            id=id,
            loc=loc,
            strategy=strategy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data
