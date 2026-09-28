

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from .types.post_mockserver_wasm_test_request_request import PostMockserverWasmTestRequestRequest
from .types.post_mockserver_wasm_test_response import PostMockserverWasmTestResponse
from .types.put_mockserver_wasm_modules_response import PutMockserverWasmModulesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWasmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_loaded_web_assembly_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        returns the names of all currently loaded WebAssembly custom rule modules

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            list of WASM module names returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def load_a_web_assembly_custom_rule_module(
        self,
        *,
        name: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverWasmModulesResponse]:
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
        HttpResponse[PutMockserverWasmModulesResponse]
            WASM module loaded
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="PUT",
            params={
                "name": name,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverWasmModulesResponse,
                    parse_obj_as(
                        type_=PutMockserverWasmModulesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unload_a_web_assembly_custom_rule_module(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="DELETE",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def evaluate_a_web_assembly_custom_rule_against_a_sample_request(
        self,
        *,
        module: typing.Optional[str] = OMIT,
        module_name: typing.Optional[str] = OMIT,
        request: typing.Optional[PostMockserverWasmTestRequestRequest] = OMIT,
        response: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostMockserverWasmTestResponse]:
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
        HttpResponse[PostMockserverWasmTestResponse]
            module evaluated
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/wasm/test",
            method="POST",
            json={
                "module": module,
                "moduleName": module_name,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostMockserverWasmTestRequestRequest, direction="write"
                ),
                "response": response,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostMockserverWasmTestResponse,
                    parse_obj_as(
                        type_=PostMockserverWasmTestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWasmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_loaded_web_assembly_modules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        returns the names of all currently loaded WebAssembly custom rule modules

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            list of WASM module names returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def load_a_web_assembly_custom_rule_module(
        self,
        *,
        name: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverWasmModulesResponse]:
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
        AsyncHttpResponse[PutMockserverWasmModulesResponse]
            WASM module loaded
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="PUT",
            params={
                "name": name,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverWasmModulesResponse,
                    parse_obj_as(
                        type_=PutMockserverWasmModulesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unload_a_web_assembly_custom_rule_module(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/wasm/modules",
            method="DELETE",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def evaluate_a_web_assembly_custom_rule_against_a_sample_request(
        self,
        *,
        module: typing.Optional[str] = OMIT,
        module_name: typing.Optional[str] = OMIT,
        request: typing.Optional[PostMockserverWasmTestRequestRequest] = OMIT,
        response: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostMockserverWasmTestResponse]:
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
        AsyncHttpResponse[PostMockserverWasmTestResponse]
            module evaluated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/wasm/test",
            method="POST",
            json={
                "module": module,
                "moduleName": module_name,
                "request": convert_and_respect_annotation_metadata(
                    object_=request, annotation=PostMockserverWasmTestRequestRequest, direction="write"
                ),
                "response": response,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostMockserverWasmTestResponse,
                    parse_obj_as(
                        type_=PostMockserverWasmTestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
