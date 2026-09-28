

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_implemented_error import NotImplementedError
from ..types.contract_test_report import ContractTestReport
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_an_open_api_spec_as_a_contract_test_against_a_live_service(
        self,
        *,
        spec: str,
        base_url: str,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        operation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContractTestReport]:
        """
        Runs each operation of an OpenAPI specification against a live service and validates that the actual responses conform to the spec. Supply the spec as a URL, file path or inline JSON/YAML ("spec", or its alias "specUrlOrPayload"), the base URL of the service under test ("baseUrl"), and optionally a single "operationId" to restrict the run. The target host is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). Returns a per-operation pass/fail report.

        Parameters
        ----------
        spec : str
            the OpenAPI spec as a URL, file path, or inline JSON/YAML (alias: specUrlOrPayload)

        base_url : str
            base URL of the live service under test; any path prefix is prepended to each operation path

        spec_url_or_payload : typing.Optional[str]
            alias for spec

        operation_id : typing.Optional[str]
            optional — restrict the run to a single operation; when absent all operations are tested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContractTestReport]
            contract test completed (inspect allPassed and per-operation results)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/contractTest",
            method="PUT",
            json={
                "spec": spec,
                "specUrlOrPayload": spec_url_or_payload,
                "baseUrl": base_url,
                "operationId": operation_id,
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
                    ContractTestReport,
                    parse_obj_as(
                        type_=ContractTestReport,
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
            if _response.status_code == 501:
                raise NotImplementedError(
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


class AsyncRawContractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_an_open_api_spec_as_a_contract_test_against_a_live_service(
        self,
        *,
        spec: str,
        base_url: str,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        operation_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContractTestReport]:
        """
        Runs each operation of an OpenAPI specification against a live service and validates that the actual responses conform to the spec. Supply the spec as a URL, file path or inline JSON/YAML ("spec", or its alias "specUrlOrPayload"), the base URL of the service under test ("baseUrl"), and optionally a single "operationId" to restrict the run. The target host is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). Returns a per-operation pass/fail report.

        Parameters
        ----------
        spec : str
            the OpenAPI spec as a URL, file path, or inline JSON/YAML (alias: specUrlOrPayload)

        base_url : str
            base URL of the live service under test; any path prefix is prepended to each operation path

        spec_url_or_payload : typing.Optional[str]
            alias for spec

        operation_id : typing.Optional[str]
            optional — restrict the run to a single operation; when absent all operations are tested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContractTestReport]
            contract test completed (inspect allPassed and per-operation results)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/contractTest",
            method="PUT",
            json={
                "spec": spec,
                "specUrlOrPayload": spec_url_or_payload,
                "baseUrl": base_url,
                "operationId": operation_id,
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
                    ContractTestReport,
                    parse_obj_as(
                        type_=ContractTestReport,
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
            if _response.status_code == 501:
                raise NotImplementedError(
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
