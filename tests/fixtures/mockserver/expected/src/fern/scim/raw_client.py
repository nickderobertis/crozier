

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.expectation import Expectation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def mock_scim_provider(
        self,
        *,
        base_path: typing.Optional[str] = OMIT,
        require_bearer_token: typing.Optional[bool] = OMIT,
        expected_bearer_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate a SCIM 2.0 provisioning provider (Users, Groups and ServiceProviderConfig endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        base_path : typing.Optional[str]
            base path the SCIM endpoints are served under

        require_bearer_token : typing.Optional[bool]
            whether requests must present a bearer token

        expected_bearer_token : typing.Optional[str]
            bearer token that incoming requests must present when required

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            SCIM provider expectations created
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/scim",
            method="PUT",
            json={
                "basePath": base_path,
                "requireBearerToken": require_bearer_token,
                "expectedBearerToken": expected_bearer_token,
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
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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


class AsyncRawScimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def mock_scim_provider(
        self,
        *,
        base_path: typing.Optional[str] = OMIT,
        require_bearer_token: typing.Optional[bool] = OMIT,
        expected_bearer_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate a SCIM 2.0 provisioning provider (Users, Groups and ServiceProviderConfig endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        base_path : typing.Optional[str]
            base path the SCIM endpoints are served under

        require_bearer_token : typing.Optional[bool]
            whether requests must present a bearer token

        expected_bearer_token : typing.Optional[str]
            bearer token that incoming requests must present when required

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            SCIM provider expectations created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/scim",
            method="PUT",
            json={
                "basePath": base_path,
                "requireBearerToken": require_bearer_token,
                "expectedBearerToken": expected_bearer_token,
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
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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
