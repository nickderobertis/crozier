

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_test_response import ApiTestResponse
from ..types.http_validation_error import HttpValidationError
from .types.test_api_api_v1testapi_post_request_provider import TestApiApiV1TestapiPostRequestProvider
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApiTestingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test_api(
        self,
        *,
        base_url: str,
        output: typing.Optional[str] = OMIT,
        spec_file: typing.Optional[str] = OMIT,
        spec_upload: typing.Optional[core.File] = OMIT,
        provider: typing.Optional[TestApiApiV1TestapiPostRequestProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiTestResponse]:
        """
        Run API tests using either a spec file path or uploaded spec file

        Parameters
        ----------
        base_url : str
            Base URL for API testing

        output : typing.Optional[str]
            Output file path

        spec_file : typing.Optional[str]
            Path to OpenAPI spec file

        spec_upload : typing.Optional[core.File]
            See core.File for more documentation

        provider : typing.Optional[TestApiApiV1TestapiPostRequestProvider]
            LLM Provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiTestResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/testapi",
            method="POST",
            data={
                "base_url": base_url,
                "output": output,
                "spec_file": spec_file,
                "provider": provider,
            },
            files={
                **({"spec_upload": spec_upload} if spec_upload is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiTestResponse,
                    parse_obj_as(
                        type_=ApiTestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawApiTestingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def test_api(
        self,
        *,
        base_url: str,
        output: typing.Optional[str] = OMIT,
        spec_file: typing.Optional[str] = OMIT,
        spec_upload: typing.Optional[core.File] = OMIT,
        provider: typing.Optional[TestApiApiV1TestapiPostRequestProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiTestResponse]:
        """
        Run API tests using either a spec file path or uploaded spec file

        Parameters
        ----------
        base_url : str
            Base URL for API testing

        output : typing.Optional[str]
            Output file path

        spec_file : typing.Optional[str]
            Path to OpenAPI spec file

        spec_upload : typing.Optional[core.File]
            See core.File for more documentation

        provider : typing.Optional[TestApiApiV1TestapiPostRequestProvider]
            LLM Provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiTestResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/testapi",
            method="POST",
            data={
                "base_url": base_url,
                "output": output,
                "spec_file": spec_file,
                "provider": provider,
            },
            files={
                **({"spec_upload": spec_upload} if spec_upload is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiTestResponse,
                    parse_obj_as(
                        type_=ApiTestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
