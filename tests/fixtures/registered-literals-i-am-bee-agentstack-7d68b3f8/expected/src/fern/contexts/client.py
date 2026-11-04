

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output12 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output13 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output14 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output15 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
)
from ..types.context_history_item_create_request import ContextHistoryItemCreateRequest
from ..types.context_permissions_grant import ContextPermissionsGrant
from ..types.context_token_response import ContextTokenResponse
from ..types.global_permission_grant import GlobalPermissionGrant
from ..types.paginated_result_context import PaginatedResultContext
from ..types.paginated_result_context_history_item import PaginatedResultContextHistoryItem
from .raw_client import AsyncRawContextsClient, RawContextsClient


OMIT = typing.cast(typing.Any, ...)


class ContextsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContextsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContextsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContextsClient
        """
        return self._raw_client

    def list_context(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        include_empty: typing.Optional[bool] = None,
        provider_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultContext:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        include_empty : typing.Optional[bool]

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultContext
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.list_context()
        """
        _response = self._raw_client.list_context(
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            include_empty=include_empty,
            provider_id=provider_id,
            request_options=request_options,
        )
        return _response.data

    def create_context(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.create_context()
        """
        _response = self._raw_client.create_context(
            metadata=metadata, provider_id=provider_id, request_options=request_options
        )
        return _response.data

    def get_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.get_context(
            context_id="context_id",
        )
        """
        _response = self._raw_client.get_context(context_id, request_options=request_options)
        return _response.data

    def update_context(
        self,
        context_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.update_context(
            context_id="context_id",
        )
        """
        _response = self._raw_client.update_context(context_id, metadata=metadata, request_options=request_options)
        return _response.data

    def delete_context(self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.delete_context(
            context_id="context_id",
        )
        """
        _response = self._raw_client.delete_context(context_id, request_options=request_options)
        return _response.data

    def patch_context_metadata(
        self,
        context_id: str,
        *,
        metadata: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Dict[str, typing.Optional[str]]
            Metadata update, will add or overwrite existing keys, None will delete the key from metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.patch_context_metadata(
            context_id="context_id",
            metadata={},
        )
        """
        _response = self._raw_client.patch_context_metadata(
            context_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    def generate_context_token(
        self,
        context_id: str,
        *,
        grant_global_permissions: typing.Optional[GlobalPermissionGrant] = OMIT,
        grant_context_permissions: typing.Optional[ContextPermissionsGrant] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextTokenResponse:
        """
        Parameters
        ----------
        context_id : str

        grant_global_permissions : typing.Optional[GlobalPermissionGrant]
            Global permissions granted by the token. Must be subset of the users permissions

        grant_context_permissions : typing.Optional[ContextPermissionsGrant]
            Context permissions granted by the token. Must be subset of the users permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextTokenResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.generate_context_token(
            context_id="context_id",
        )
        """
        _response = self._raw_client.generate_context_token(
            context_id,
            grant_global_permissions=grant_global_permissions,
            grant_context_permissions=grant_context_permissions,
            request_options=request_options,
        )
        return _response.data

    def list_context_history(
        self,
        context_id: str,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultContextHistoryItem:
        """
        Parameters
        ----------
        context_id : str

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultContextHistoryItem
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.list_context_history(
            context_id="context_id",
        )
        """
        _response = self._raw_client.list_context_history(
            context_id,
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def add_context_history_item(
        self,
        context_id: str,
        *,
        request: ContextHistoryItemCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        context_id : str

        request : ContextHistoryItemCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ArtifactInput, FernApi, PartInput_Text

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.add_context_history_item(
            context_id="context_id",
            request=ArtifactInput(
                artifact_id="artifactId",
                parts=[
                    PartInput_Text(
                        text="text",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.add_context_history_item(
            context_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_context_history_from_id(
        self, context_id: str, *, from_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        context_id : str

        from_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.contexts.delete_context_history_from_id(
            context_id="context_id",
            from_id="from_id",
        )
        """
        _response = self._raw_client.delete_context_history_from_id(
            context_id, from_id=from_id, request_options=request_options
        )
        return _response.data


class AsyncContextsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContextsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContextsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContextsClient
        """
        return self._raw_client

    async def list_context(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        include_empty: typing.Optional[bool] = None,
        provider_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultContext:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        include_empty : typing.Optional[bool]

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultContext
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.list_context()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_context(
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            include_empty=include_empty,
            provider_id=provider_id,
            request_options=request_options,
        )
        return _response.data

    async def create_context(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.create_context()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_context(
            metadata=metadata, provider_id=provider_id, request_options=request_options
        )
        return _response.data

    async def get_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.get_context(
                context_id="context_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_context(context_id, request_options=request_options)
        return _response.data

    async def update_context(
        self,
        context_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.update_context(
                context_id="context_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_context(
            context_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def delete_context(self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        context_id : str

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.delete_context(
                context_id="context_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_context(context_id, request_options=request_options)
        return _response.data

    async def patch_context_metadata(
        self,
        context_id: str,
        *,
        metadata: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Dict[str, typing.Optional[str]]
            Metadata update, will add or overwrite existing keys, None will delete the key from metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.patch_context_metadata(
                context_id="context_id",
                metadata={},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_context_metadata(
            context_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def generate_context_token(
        self,
        context_id: str,
        *,
        grant_global_permissions: typing.Optional[GlobalPermissionGrant] = OMIT,
        grant_context_permissions: typing.Optional[ContextPermissionsGrant] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContextTokenResponse:
        """
        Parameters
        ----------
        context_id : str

        grant_global_permissions : typing.Optional[GlobalPermissionGrant]
            Global permissions granted by the token. Must be subset of the users permissions

        grant_context_permissions : typing.Optional[ContextPermissionsGrant]
            Context permissions granted by the token. Must be subset of the users permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextTokenResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.generate_context_token(
                context_id="context_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_context_token(
            context_id,
            grant_global_permissions=grant_global_permissions,
            grant_context_permissions=grant_context_permissions,
            request_options=request_options,
        )
        return _response.data

    async def list_context_history(
        self,
        context_id: str,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultContextHistoryItem:
        """
        Parameters
        ----------
        context_id : str

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultContextHistoryItem
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.list_context_history(
                context_id="context_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_context_history(
            context_id,
            limit=limit,
            page_token=page_token,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def add_context_history_item(
        self,
        context_id: str,
        *,
        request: ContextHistoryItemCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        context_id : str

        request : ContextHistoryItemCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import ArtifactInput, AsyncFernApi, PartInput_Text

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.add_context_history_item(
                context_id="context_id",
                request=ArtifactInput(
                    artifact_id="artifactId",
                    parts=[
                        PartInput_Text(
                            text="text",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_context_history_item(
            context_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_context_history_from_id(
        self, context_id: str, *, from_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        context_id : str

        from_id : str

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contexts.delete_context_history_from_id(
                context_id="context_id",
                from_id="from_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_context_history_from_id(
            context_id, from_id=from_id, request_options=request_options
        )
        return _response.data
