

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.error_bad_request import ErrorBadRequest
from ..types.error_internal_server_error import ErrorInternalServerError
from ..types.error_not_found import ErrorNotFound
from .types.review_get_mac_config_by_id_response import ReviewGetMacConfigByIdResponse
from .types.review_get_mac_configs_response_item import ReviewGetMacConfigsResponseItem
from pydantic import ValidationError


class RawMacConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def review_get_mac_configs(
        self,
        *,
        search: typing.Optional[str] = None,
        selected_config_identifier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ReviewGetMacConfigsResponseItem]]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        selected_config_identifier : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ReviewGetMacConfigsResponseItem]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "mac-configs",
            method="GET",
            params={
                "search": search,
                "selectedConfigIdentifier": selected_config_identifier,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReviewGetMacConfigsResponseItem],
                    parse_obj_as(
                        type_=typing.List[ReviewGetMacConfigsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def review_get_mac_config_by_id(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[ReviewGetMacConfigByIdResponse]]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ReviewGetMacConfigByIdResponse]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mac-configs/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ReviewGetMacConfigByIdResponse],
                    parse_obj_as(
                        type_=typing.Optional[ReviewGetMacConfigByIdResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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


class AsyncRawMacConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def review_get_mac_configs(
        self,
        *,
        search: typing.Optional[str] = None,
        selected_config_identifier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ReviewGetMacConfigsResponseItem]]:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        selected_config_identifier : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ReviewGetMacConfigsResponseItem]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mac-configs",
            method="GET",
            params={
                "search": search,
                "selectedConfigIdentifier": selected_config_identifier,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReviewGetMacConfigsResponseItem],
                    parse_obj_as(
                        type_=typing.List[ReviewGetMacConfigsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def review_get_mac_config_by_id(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[ReviewGetMacConfigByIdResponse]]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ReviewGetMacConfigByIdResponse]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mac-configs/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ReviewGetMacConfigByIdResponse],
                    parse_obj_as(
                        type_=typing.Optional[ReviewGetMacConfigByIdResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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
