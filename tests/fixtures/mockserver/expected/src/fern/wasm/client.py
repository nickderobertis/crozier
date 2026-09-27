

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWasmClient, RawWasmClient
from .types.post_mockserver_wasm_test_request_request import PostMockserverWasmTestRequestRequest
from .types.post_mockserver_wasm_test_response import PostMockserverWasmTestResponse
from .types.put_mockserver_wasm_modules_response import PutMockserverWasmModulesResponse


OMIT = typing.cast(typing.Any, ...)


class WasmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWasmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWasmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWasmClient
        """
        return self._raw_client

    def list_loaded_web_assembly_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        returns the names of all currently loaded WebAssembly custom rule modules

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            list of WASM module names returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wasm.list_loaded_web_assembly_modules()
        """
        _response = self._raw_client.list_loaded_web_assembly_modules(request_options=request_options)
        return _response.data

    def load_a_web_assembly_custom_rule_module(
        self,
        *,
        name: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverWasmModulesResponse:
        """
        stores a compiled WebAssembly module (raw .wasm bytes) under the name supplied in the query parameter

        Parameters
        ----------
        name : str
            name to register the WASM module under

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverWasmModulesResponse
            WASM module loaded
        """
        _response = self._raw_client.load_a_web_assembly_custom_rule_module(
            name=name, request=request, request_options=request_options
        )
        return _response.data

    def unload_a_web_assembly_custom_rule_module(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes the named WebAssembly custom rule module from the module store. Succeeds with an empty body; the module name is required as a query parameter.

        Parameters
        ----------
        name : str
            name of the WASM module to unload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wasm.unload_a_web_assembly_custom_rule_module(
            name="name",
        )
        """
        _response = self._raw_client.unload_a_web_assembly_custom_rule_module(
            name=name, request_options=request_options
        )
        return _response.data

    def evaluate_a_web_assembly_custom_rule_against_a_sample_request(
        self,
        *,
        module: typing.Optional[str] = OMIT,
        module_name: typing.Optional[str] = OMIT,
        request: typing.Optional[PostMockserverWasmTestRequestRequest] = OMIT,
        response: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostMockserverWasmTestResponse:
        """
        Runs a WebAssembly custom rule module against a sample request and reports whether it matched, without registering an expectation. Supply the module either inline as base64 ("module") or by the name of an already-loaded module ("moduleName"); when both are present "module" wins. When a "response" object is also supplied the ABI v3 `shape_response` hook runs and the shaped response is returned alongside the match result.

        Parameters
        ----------
        module : typing.Optional[str]
            base64-encoded compiled WebAssembly module bytes

        module_name : typing.Optional[str]
            name of an already-loaded WASM module to evaluate instead of an inline module

        request : typing.Optional[PostMockserverWasmTestRequestRequest]
            the sample request the rule is evaluated against

        response : typing.Optional[typing.Dict[str, typing.Any]]
            optional sample response; when present the ABI v3 shape_response hook runs and the shaped response is returned with the match result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMockserverWasmTestResponse
            module evaluated

        Examples
        --------
        from fern.wasm import PostMockserverWasmTestRequestRequest

        from fern import FernApi

        client = FernApi()
        client.wasm.evaluate_a_web_assembly_custom_rule_against_a_sample_request(
            module_name="header-rule",
            request=PostMockserverWasmTestRequestRequest(
                method="GET",
                path="/api/orders",
                headers={"x-tenant": ["acme"]},
            ),
        )
        """
        _response = self._raw_client.evaluate_a_web_assembly_custom_rule_against_a_sample_request(
            module=module, module_name=module_name, request=request, response=response, request_options=request_options
        )
        return _response.data


class AsyncWasmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWasmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWasmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWasmClient
        """
        return self._raw_client

    async def list_loaded_web_assembly_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        returns the names of all currently loaded WebAssembly custom rule modules

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            list of WASM module names returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wasm.list_loaded_web_assembly_modules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_loaded_web_assembly_modules(request_options=request_options)
        return _response.data

    async def load_a_web_assembly_custom_rule_module(
        self,
        *,
        name: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverWasmModulesResponse:
        """
        stores a compiled WebAssembly module (raw .wasm bytes) under the name supplied in the query parameter

        Parameters
        ----------
        name : str
            name to register the WASM module under

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverWasmModulesResponse
            WASM module loaded
        """
        _response = await self._raw_client.load_a_web_assembly_custom_rule_module(
            name=name, request=request, request_options=request_options
        )
        return _response.data

    async def unload_a_web_assembly_custom_rule_module(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes the named WebAssembly custom rule module from the module store. Succeeds with an empty body; the module name is required as a query parameter.

        Parameters
        ----------
        name : str
            name of the WASM module to unload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wasm.unload_a_web_assembly_custom_rule_module(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unload_a_web_assembly_custom_rule_module(
            name=name, request_options=request_options
        )
        return _response.data

    async def evaluate_a_web_assembly_custom_rule_against_a_sample_request(
        self,
        *,
        module: typing.Optional[str] = OMIT,
        module_name: typing.Optional[str] = OMIT,
        request: typing.Optional[PostMockserverWasmTestRequestRequest] = OMIT,
        response: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostMockserverWasmTestResponse:
        """
        Runs a WebAssembly custom rule module against a sample request and reports whether it matched, without registering an expectation. Supply the module either inline as base64 ("module") or by the name of an already-loaded module ("moduleName"); when both are present "module" wins. When a "response" object is also supplied the ABI v3 `shape_response` hook runs and the shaped response is returned alongside the match result.

        Parameters
        ----------
        module : typing.Optional[str]
            base64-encoded compiled WebAssembly module bytes

        module_name : typing.Optional[str]
            name of an already-loaded WASM module to evaluate instead of an inline module

        request : typing.Optional[PostMockserverWasmTestRequestRequest]
            the sample request the rule is evaluated against

        response : typing.Optional[typing.Dict[str, typing.Any]]
            optional sample response; when present the ABI v3 shape_response hook runs and the shaped response is returned with the match result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMockserverWasmTestResponse
            module evaluated

        Examples
        --------
        import asyncio

        from fern.wasm import PostMockserverWasmTestRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wasm.evaluate_a_web_assembly_custom_rule_against_a_sample_request(
                module_name="header-rule",
                request=PostMockserverWasmTestRequestRequest(
                    method="GET",
                    path="/api/orders",
                    headers={"x-tenant": ["acme"]},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.evaluate_a_web_assembly_custom_rule_against_a_sample_request(
            module=module, module_name=module_name, request=request, response=response, request_options=request_options
        )
        return _response.data
