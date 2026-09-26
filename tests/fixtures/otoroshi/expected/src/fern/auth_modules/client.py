

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
from ..types.unknown import Unknown
from ..types.web_authn_registration_finish_body import WebAuthnRegistrationFinishBody
from ..types.web_authn_registration_start_body import WebAuthnRegistrationStartBody
from .raw_client import AsyncRawAuthModulesClient, RawAuthModulesClient


OMIT = typing.cast(typing.Any, ...)


class AuthModulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthModulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthModulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthModulesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_auth_module(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_templates_controller_initiate_auth_module()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_auth_module(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_find_all_templates(
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
        client.auth_modules.otoroshi_controllers_adminapi_templates_controller_find_all_templates()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_find_all_templates(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
        self,
        id: str,
        *,
        request: WebAuthnRegistrationStartBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unknown:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : WebAuthnRegistrationStartBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
        self,
        id: str,
        *,
        request: WebAuthnRegistrationFinishBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unknown:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : WebAuthnRegistrationFinishBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiAuthAuthModuleConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiAuthAuthModuleConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiAuthBasicAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
            request=[OtoroshiAuthBasicAuthModuleConfig()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiAuthAuthModuleConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiAuthAuthModuleConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiAuthBasicAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
            request=[OtoroshiAuthBasicAuthModuleConfig()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action(
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
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
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
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
        self, id: str, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiAuthBasicAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
            id="id",
            request=OtoroshiAuthBasicAuthModuleConfig(),
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
        self, id: str, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiAuthBasicAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
            id="id",
            request=OtoroshiAuthBasicAuthModuleConfig(),
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiAuthAuthModuleConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiAuthAuthModuleConfig]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_auth_modules_controller_create_action(
        self, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiAuthBasicAuthModuleConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_create_action(
            request=OtoroshiAuthBasicAuthModuleConfig(),
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_create_action(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncAuthModulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthModulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthModulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthModulesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_auth_module(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
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
            await client.auth_modules.otoroshi_controllers_adminapi_templates_controller_initiate_auth_module()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_auth_module(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_find_all_templates(
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
            await client.auth_modules.otoroshi_controllers_adminapi_templates_controller_find_all_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_find_all_templates(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
        self,
        id: str,
        *,
        request: WebAuthnRegistrationStartBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unknown:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : WebAuthnRegistrationStartBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_start_registration(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
        self,
        id: str,
        *,
        request: WebAuthnRegistrationFinishBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unknown:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : WebAuthnRegistrationFinishBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiAuthAuthModuleConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiAuthAuthModuleConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiAuthBasicAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
                request=[OtoroshiAuthBasicAuthModuleConfig()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiAuthAuthModuleConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiAuthAuthModuleConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiAuthBasicAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
                request=[OtoroshiAuthBasicAuthModuleConfig()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action(
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
        self, id: str, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiAuthBasicAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
                id="id",
                request=OtoroshiAuthBasicAuthModuleConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
        self, id: str, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiAuthBasicAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
                id="id",
                request=OtoroshiAuthBasicAuthModuleConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiAuthAuthModuleConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiAuthAuthModuleConfig]
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
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_auth_modules_controller_create_action(
        self, *, request: OtoroshiAuthAuthModuleConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiAuthAuthModuleConfig:
        """
        Parameters
        ----------
        request : OtoroshiAuthAuthModuleConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiAuthAuthModuleConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiAuthBasicAuthModuleConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.auth_modules.otoroshi_controllers_adminapi_auth_modules_controller_create_action(
                request=OtoroshiAuthBasicAuthModuleConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_auth_modules_controller_create_action(
            request=request, request_options=request_options
        )
        return _response.data
