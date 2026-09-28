

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_error_template import OtoroshiModelsErrorTemplate
from .raw_client import AsyncRawErrorTemplatesClient, RawErrorTemplatesClient


OMIT = typing.cast(typing.Any, ...)


class ErrorTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawErrorTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawErrorTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawErrorTemplatesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsErrorTemplate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsErrorTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsErrorTemplate

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
            request=[OtoroshiModelsErrorTemplate()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsErrorTemplate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsErrorTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsErrorTemplate

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
            request=[OtoroshiModelsErrorTemplate()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action(
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
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
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
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
        self,
        id: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
            id,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
        self,
        id: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
            id,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsErrorTemplate]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_error_templates_controller_create_action(
        self,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_create_action(
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncErrorTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawErrorTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawErrorTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawErrorTemplatesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsErrorTemplate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsErrorTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsErrorTemplate

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
                request=[OtoroshiModelsErrorTemplate()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsErrorTemplate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsErrorTemplate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsErrorTemplate

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
                request=[OtoroshiModelsErrorTemplate()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action(
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
        self,
        id: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_update_entity_action(
                id,
                template50x=template50x,
                template_maintenance=template_maintenance,
                template_build=template_build,
                service_id=service_id,
                loc=loc,
                metadata=metadata,
                messages=messages,
                name=name,
                template40x=template40x,
                tags=tags,
                description=description,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_delete_entity_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
        self,
        id: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_patch_entity_action(
            id,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsErrorTemplate]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsErrorTemplate]
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_error_templates_controller_create_action(
        self,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
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
            await client.error_templates.otoroshi_controllers_adminapi_error_templates_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_error_templates_controller_create_action(
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data
