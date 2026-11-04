

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.model import Model
from ..types.model_list import ModelList
from pydantic import ValidationError


class RawModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ModelList]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelList]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "models",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelList,
                    parse_obj_as(
                        type_=ModelList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, model_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Model]:
        """
        Parameters
        ----------
        model_id : str
            The identifier of the model.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Model]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model_id)}",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Model,
                    parse_obj_as(
                        type_=Model,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ModelList]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelList]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "models",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelList,
                    parse_obj_as(
                        type_=ModelList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, model_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Model]:
        """
        Parameters
        ----------
        model_id : str
            The identifier of the model.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Model]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model_id)}",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Model,
                    parse_obj_as(
                        type_=Model,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
