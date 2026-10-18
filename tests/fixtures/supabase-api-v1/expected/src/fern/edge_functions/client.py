

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_update_function_body import BulkUpdateFunctionBody
from ..types.bulk_update_function_response_output import BulkUpdateFunctionResponseOutput
from ..types.deploy_function_response_output import DeployFunctionResponseOutput
from ..types.function_response_output import FunctionResponseOutput
from ..types.function_slug_response_output import FunctionSlugResponseOutput
from ..types.streamable_file import StreamableFile
from .raw_client import AsyncRawEdgeFunctionsClient, RawEdgeFunctionsClient
from .types.v1deploy_a_function_request_metadata import V1DeployAFunctionRequestMetadata


OMIT = typing.cast(typing.Any, ...)


class EdgeFunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEdgeFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEdgeFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEdgeFunctionsClient
        """
        return self._raw_client

    def v1list_all_functions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FunctionResponseOutput]:
        """
        Returns all functions you've previously added to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FunctionResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1list_all_functions(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_functions(ref, request_options=request_options)
        return _response.data

    def v1create_a_function(
        self,
        ref: str,
        *,
        v1create_function_body_slug: str,
        v1create_function_body_name: str,
        body: str,
        slug: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        verify_jwt: typing.Optional[str] = None,
        import_map: typing.Optional[str] = None,
        entrypoint_path: typing.Optional[str] = None,
        import_map_path: typing.Optional[str] = None,
        ezbr_sha256: typing.Optional[str] = None,
        v1create_function_body_verify_jwt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionResponseOutput:
        """
        This endpoint is deprecated - use the deploy endpoint. Creates a function and adds it to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        v1create_function_body_slug : str

        v1create_function_body_name : str

        body : str

        slug : typing.Optional[str]

        name : typing.Optional[str]

        verify_jwt : typing.Optional[str]

        import_map : typing.Optional[str]

        entrypoint_path : typing.Optional[str]

        import_map_path : typing.Optional[str]

        ezbr_sha256 : typing.Optional[str]

        v1create_function_body_verify_jwt : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1create_a_function(
            ref="abcdefghijklmnopqrst",
            slug="hello-world",
            name="Hello World",
            entrypoint_path="index.ts",
            import_map_path="import_map.json",
            ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
            v1create_function_body_slug="hello-world",
            v1create_function_body_name="Hello World",
            body="Deno.serve(() => new Response('Hello, world!'))",
            v1create_function_body_verify_jwt=True,
        )
        """
        _response = self._raw_client.v1create_a_function(
            ref,
            v1create_function_body_slug=v1create_function_body_slug,
            v1create_function_body_name=v1create_function_body_name,
            body=body,
            slug=slug,
            name=name,
            verify_jwt=verify_jwt,
            import_map=import_map,
            entrypoint_path=entrypoint_path,
            import_map_path=import_map_path,
            ezbr_sha256=ezbr_sha256,
            v1create_function_body_verify_jwt=v1create_function_body_verify_jwt,
            request_options=request_options,
        )
        return _response.data

    def v1bulk_update_functions(
        self, ref: str, *, request: BulkUpdateFunctionBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkUpdateFunctionResponseOutput:
        """
        Bulk update functions. It will create a new function or replace existing. The operation is idempotent. NOTE: You will need to manually bump the version.

        Parameters
        ----------
        ref : str
            Project ref

        request : BulkUpdateFunctionBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkUpdateFunctionResponseOutput


        Examples
        --------
        from fern import (
            BulkUpdateFunctionBodyItem,
            BulkUpdateFunctionBodyItemStatus,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1bulk_update_functions(
            ref="abcdefghijklmnopqrst",
            request=[
                BulkUpdateFunctionBodyItem(
                    id="3c078cce-ad70-4148-9f37-4da362789053",
                    slug="hello-world",
                    name="Hello World",
                    status=BulkUpdateFunctionBodyItemStatus.ACTIVE,
                    version=2,
                    verify_jwt=True,
                    entrypoint_path="index.ts",
                )
            ],
        )
        """
        _response = self._raw_client.v1bulk_update_functions(ref, request=request, request_options=request_options)
        return _response.data

    def v1deploy_a_function(
        self,
        ref: str,
        *,
        file: typing.List[core.File],
        metadata: V1DeployAFunctionRequestMetadata,
        slug: typing.Optional[str] = None,
        bundle_only: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeployFunctionResponseOutput:
        """
        A new endpoint to deploy functions. It will create if function does not exist.

        Parameters
        ----------
        ref : str
            Project ref

        file : typing.List[core.File]
            See core.File for more documentation

        metadata : V1DeployAFunctionRequestMetadata

        slug : typing.Optional[str]

        bundle_only : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeployFunctionResponseOutput


        Examples
        --------
        from fern.edge_functions import V1DeployAFunctionRequestMetadata

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1deploy_a_function(
            ref="abcdefghijklmnopqrst",
            slug="hello-world",
            metadata=V1DeployAFunctionRequestMetadata(
                entrypoint_path="entrypoint_path",
            ),
        )
        """
        _response = self._raw_client.v1deploy_a_function(
            ref, file=file, metadata=metadata, slug=slug, bundle_only=bundle_only, request_options=request_options
        )
        return _response.data

    def v1get_a_function(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FunctionSlugResponseOutput:
        """
        Retrieves a function with the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionSlugResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1get_a_function(
            ref="abcdefghijklmnopqrst",
            function_slug="hello-world",
        )
        """
        _response = self._raw_client.v1get_a_function(ref, function_slug, request_options=request_options)
        return _response.data

    def v1delete_a_function(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a function with the specified slug from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1delete_a_function(
            ref="abcdefghijklmnopqrst",
            function_slug="hello-world",
        )
        """
        _response = self._raw_client.v1delete_a_function(ref, function_slug, request_options=request_options)
        return _response.data

    def v1update_a_function(
        self,
        ref: str,
        function_slug: str,
        *,
        slug: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        verify_jwt: typing.Optional[str] = None,
        import_map: typing.Optional[str] = None,
        entrypoint_path: typing.Optional[str] = None,
        import_map_path: typing.Optional[str] = None,
        ezbr_sha256: typing.Optional[str] = None,
        v1update_function_body_name: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        v1update_function_body_verify_jwt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionSlugResponseOutput:
        """
        Updates a function with the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        slug : typing.Optional[str]

        name : typing.Optional[str]

        verify_jwt : typing.Optional[str]

        import_map : typing.Optional[str]

        entrypoint_path : typing.Optional[str]

        import_map_path : typing.Optional[str]

        ezbr_sha256 : typing.Optional[str]

        v1update_function_body_name : typing.Optional[str]

        body : typing.Optional[str]

        v1update_function_body_verify_jwt : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionSlugResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1update_a_function(
            ref="abcdefghijklmnopqrst",
            function_slug="hello-world",
            slug="hello-world",
            name="Hello World",
            entrypoint_path="index.ts",
            import_map_path="import_map.json",
            ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
            v1update_function_body_name="Hello World",
            body="Deno.serve(() => new Response('Hello again!'))",
            v1update_function_body_verify_jwt=True,
        )
        """
        _response = self._raw_client.v1update_a_function(
            ref,
            function_slug,
            slug=slug,
            name=name,
            verify_jwt=verify_jwt,
            import_map=import_map,
            entrypoint_path=entrypoint_path,
            import_map_path=import_map_path,
            ezbr_sha256=ezbr_sha256,
            v1update_function_body_name=v1update_function_body_name,
            body=body,
            v1update_function_body_verify_jwt=v1update_function_body_verify_jwt,
            request_options=request_options,
        )
        return _response.data

    def v1get_a_function_body(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamableFile:
        """
        Retrieves a function body for the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamableFile


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_functions.v1get_a_function_body(
            ref="abcdefghijklmnopqrst",
            function_slug="hello-world",
        )
        """
        _response = self._raw_client.v1get_a_function_body(ref, function_slug, request_options=request_options)
        return _response.data


class AsyncEdgeFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEdgeFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEdgeFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEdgeFunctionsClient
        """
        return self._raw_client

    async def v1list_all_functions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FunctionResponseOutput]:
        """
        Returns all functions you've previously added to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FunctionResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1list_all_functions(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_functions(ref, request_options=request_options)
        return _response.data

    async def v1create_a_function(
        self,
        ref: str,
        *,
        v1create_function_body_slug: str,
        v1create_function_body_name: str,
        body: str,
        slug: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        verify_jwt: typing.Optional[str] = None,
        import_map: typing.Optional[str] = None,
        entrypoint_path: typing.Optional[str] = None,
        import_map_path: typing.Optional[str] = None,
        ezbr_sha256: typing.Optional[str] = None,
        v1create_function_body_verify_jwt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionResponseOutput:
        """
        This endpoint is deprecated - use the deploy endpoint. Creates a function and adds it to the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        v1create_function_body_slug : str

        v1create_function_body_name : str

        body : str

        slug : typing.Optional[str]

        name : typing.Optional[str]

        verify_jwt : typing.Optional[str]

        import_map : typing.Optional[str]

        entrypoint_path : typing.Optional[str]

        import_map_path : typing.Optional[str]

        ezbr_sha256 : typing.Optional[str]

        v1create_function_body_verify_jwt : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1create_a_function(
                ref="abcdefghijklmnopqrst",
                slug="hello-world",
                name="Hello World",
                entrypoint_path="index.ts",
                import_map_path="import_map.json",
                ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
                v1create_function_body_slug="hello-world",
                v1create_function_body_name="Hello World",
                body="Deno.serve(() => new Response('Hello, world!'))",
                v1create_function_body_verify_jwt=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_a_function(
            ref,
            v1create_function_body_slug=v1create_function_body_slug,
            v1create_function_body_name=v1create_function_body_name,
            body=body,
            slug=slug,
            name=name,
            verify_jwt=verify_jwt,
            import_map=import_map,
            entrypoint_path=entrypoint_path,
            import_map_path=import_map_path,
            ezbr_sha256=ezbr_sha256,
            v1create_function_body_verify_jwt=v1create_function_body_verify_jwt,
            request_options=request_options,
        )
        return _response.data

    async def v1bulk_update_functions(
        self, ref: str, *, request: BulkUpdateFunctionBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkUpdateFunctionResponseOutput:
        """
        Bulk update functions. It will create a new function or replace existing. The operation is idempotent. NOTE: You will need to manually bump the version.

        Parameters
        ----------
        ref : str
            Project ref

        request : BulkUpdateFunctionBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkUpdateFunctionResponseOutput


        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BulkUpdateFunctionBodyItem,
            BulkUpdateFunctionBodyItemStatus,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1bulk_update_functions(
                ref="abcdefghijklmnopqrst",
                request=[
                    BulkUpdateFunctionBodyItem(
                        id="3c078cce-ad70-4148-9f37-4da362789053",
                        slug="hello-world",
                        name="Hello World",
                        status=BulkUpdateFunctionBodyItemStatus.ACTIVE,
                        version=2,
                        verify_jwt=True,
                        entrypoint_path="index.ts",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1bulk_update_functions(
            ref, request=request, request_options=request_options
        )
        return _response.data

    async def v1deploy_a_function(
        self,
        ref: str,
        *,
        file: typing.List[core.File],
        metadata: V1DeployAFunctionRequestMetadata,
        slug: typing.Optional[str] = None,
        bundle_only: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeployFunctionResponseOutput:
        """
        A new endpoint to deploy functions. It will create if function does not exist.

        Parameters
        ----------
        ref : str
            Project ref

        file : typing.List[core.File]
            See core.File for more documentation

        metadata : V1DeployAFunctionRequestMetadata

        slug : typing.Optional[str]

        bundle_only : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeployFunctionResponseOutput


        Examples
        --------
        import asyncio

        from fern.edge_functions import V1DeployAFunctionRequestMetadata

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1deploy_a_function(
                ref="abcdefghijklmnopqrst",
                slug="hello-world",
                metadata=V1DeployAFunctionRequestMetadata(
                    entrypoint_path="entrypoint_path",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1deploy_a_function(
            ref, file=file, metadata=metadata, slug=slug, bundle_only=bundle_only, request_options=request_options
        )
        return _response.data

    async def v1get_a_function(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FunctionSlugResponseOutput:
        """
        Retrieves a function with the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionSlugResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1get_a_function(
                ref="abcdefghijklmnopqrst",
                function_slug="hello-world",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_function(ref, function_slug, request_options=request_options)
        return _response.data

    async def v1delete_a_function(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a function with the specified slug from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1delete_a_function(
                ref="abcdefghijklmnopqrst",
                function_slug="hello-world",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_a_function(ref, function_slug, request_options=request_options)
        return _response.data

    async def v1update_a_function(
        self,
        ref: str,
        function_slug: str,
        *,
        slug: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        verify_jwt: typing.Optional[str] = None,
        import_map: typing.Optional[str] = None,
        entrypoint_path: typing.Optional[str] = None,
        import_map_path: typing.Optional[str] = None,
        ezbr_sha256: typing.Optional[str] = None,
        v1update_function_body_name: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        v1update_function_body_verify_jwt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FunctionSlugResponseOutput:
        """
        Updates a function with the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        slug : typing.Optional[str]

        name : typing.Optional[str]

        verify_jwt : typing.Optional[str]

        import_map : typing.Optional[str]

        entrypoint_path : typing.Optional[str]

        import_map_path : typing.Optional[str]

        ezbr_sha256 : typing.Optional[str]

        v1update_function_body_name : typing.Optional[str]

        body : typing.Optional[str]

        v1update_function_body_verify_jwt : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FunctionSlugResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1update_a_function(
                ref="abcdefghijklmnopqrst",
                function_slug="hello-world",
                slug="hello-world",
                name="Hello World",
                entrypoint_path="index.ts",
                import_map_path="import_map.json",
                ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
                v1update_function_body_name="Hello World",
                body="Deno.serve(() => new Response('Hello again!'))",
                v1update_function_body_verify_jwt=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_a_function(
            ref,
            function_slug,
            slug=slug,
            name=name,
            verify_jwt=verify_jwt,
            import_map=import_map,
            entrypoint_path=entrypoint_path,
            import_map_path=import_map_path,
            ezbr_sha256=ezbr_sha256,
            v1update_function_body_name=v1update_function_body_name,
            body=body,
            v1update_function_body_verify_jwt=v1update_function_body_verify_jwt,
            request_options=request_options,
        )
        return _response.data

    async def v1get_a_function_body(
        self, ref: str, function_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamableFile:
        """
        Retrieves a function body for the specified slug and project.

        Parameters
        ----------
        ref : str
            Project ref

        function_slug : str
            Function slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamableFile


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_functions.v1get_a_function_body(
                ref="abcdefghijklmnopqrst",
                function_slug="hello-world",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_function_body(ref, function_slug, request_options=request_options)
        return _response.data
