

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.http_sse._api import EventSource
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as, parse_sse_obj
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.conflict_error import ConflictError
from .errors.content_too_large_error import ContentTooLargeError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.method_not_allowed_error import MethodNotAllowedError
from .errors.not_found_error import NotFoundError
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.get_api_playback_motion_response import GetApiPlaybackMotionResponse
from .types.get_api_playback_response import GetApiPlaybackResponse
from .types.post_api_bridge_pose_request import PostApiBridgePoseRequest
from .types.post_api_playback_control_request_command import PostApiPlaybackControlRequestCommand
from .types.post_api_playback_control_request_mode import PostApiPlaybackControlRequestMode
from .types.post_api_playback_control_response import PostApiPlaybackControlResponse
from .types.post_api_playback_motion_request import PostApiPlaybackMotionRequest
from .types.post_api_playback_motion_response import PostApiPlaybackMotionResponse
from .types.post_api_playback_parameters_response import PostApiPlaybackParametersResponse
from .types.post_api_playback_reload_response import PostApiPlaybackReloadResponse
from .types.qa_check_request_motion_sweep import QaCheckRequestMotionSweep
from .types.qa_check_request_pose_samples_item import QaCheckRequestPoseSamplesItem
from .types.transaction_request import TransactionRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_context(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/context",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_parts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/parts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_deformers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/deformers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/params",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_modeling(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_modeling_audit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling/audit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_modeling_techniques(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling/techniques",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_modeling_role_suggestions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling/role-suggestions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_modeling_artmesh_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling/artmesh-presets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_rig_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/rig/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_rig_validate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/rig/validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_rig_inspect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/rig/inspect",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_reference(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/reference",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_qa_golden(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/qa/golden",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bundle",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/schema",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_changes(
        self, *, since: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        since : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/changes",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_parts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/parts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_deformers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/deformers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_rig(
        self, *, include_assets: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/rig",
            method="GET",
            params={
                "includeAssets": include_assets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def put_api_rig(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        include_assets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/rig",
            method="PUT",
            params={
                "includeAssets": include_assets,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_qa_check(
        self,
        *,
        poses: typing.Optional[typing.Sequence[str]] = OMIT,
        pose_samples: typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]] = OMIT,
        regions: typing.Optional[typing.Sequence[str]] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[float] = OMIT,
        min_coverage: typing.Optional[float] = OMIT,
        fail_on_edge_contact: typing.Optional[bool] = OMIT,
        expected_hashes: typing.Optional[typing.Dict[str, str]] = OMIT,
        check_triangle_distortion: typing.Optional[bool] = OMIT,
        max_triangle_stretch_ratio: typing.Optional[float] = OMIT,
        max_triangle_compression_ratio: typing.Optional[float] = OMIT,
        max_triangle_anisotropy: typing.Optional[float] = OMIT,
        motion_sweep: typing.Optional[QaCheckRequestMotionSweep] = OMIT,
        supersample: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        poses : typing.Optional[typing.Sequence[str]]

        pose_samples : typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]]

        regions : typing.Optional[typing.Sequence[str]]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[float]

        min_coverage : typing.Optional[float]

        fail_on_edge_contact : typing.Optional[bool]

        expected_hashes : typing.Optional[typing.Dict[str, str]]

        check_triangle_distortion : typing.Optional[bool]

        max_triangle_stretch_ratio : typing.Optional[float]

        max_triangle_compression_ratio : typing.Optional[float]

        max_triangle_anisotropy : typing.Optional[float]

        motion_sweep : typing.Optional[QaCheckRequestMotionSweep]

        supersample : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/qa/check",
            method="POST",
            json={
                "poses": poses,
                "poseSamples": convert_and_respect_annotation_metadata(
                    object_=pose_samples, annotation=typing.Sequence[QaCheckRequestPoseSamplesItem], direction="write"
                ),
                "regions": regions,
                "width": width,
                "height": height,
                "physics": physics,
                "physicsTime": physics_time,
                "physicsSteps": physics_steps,
                "minCoverage": min_coverage,
                "failOnEdgeContact": fail_on_edge_contact,
                "expectedHashes": expected_hashes,
                "checkTriangleDistortion": check_triangle_distortion,
                "maxTriangleStretchRatio": max_triangle_stretch_ratio,
                "maxTriangleCompressionRatio": max_triangle_compression_ratio,
                "maxTriangleAnisotropy": max_triangle_anisotropy,
                "motionSweep": convert_and_respect_annotation_metadata(
                    object_=motion_sweep, annotation=QaCheckRequestMotionSweep, direction="write"
                ),
                "supersample": supersample,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_modeling_transaction(
        self, *, request: TransactionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : TransactionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/modeling/transaction",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TransactionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_assets_externalize(
        self,
        *,
        rig: typing.Dict[str, typing.Any],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        rig : typing.Dict[str, typing.Any]

        dry_run : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/assets/externalize",
            method="POST",
            json={
                "rig": rig,
                "dryRun": dry_run,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    @contextlib.contextmanager
    def get_api_screenshot(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            PNG image
        """
        with self._client_wrapper.httpx_client.stream(
            "api/screenshot",
            method="GET",
            params={
                "set": set_,
                "detail": detail,
                "partIds": part_ids,
                "physics": physics,
                "ParamAngleX": param_angle_x,
                "ParamAngleY": param_angle_y,
                "ParamAngleZ": param_angle_z,
                "width": width,
                "height": height,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    @contextlib.contextmanager
    def get_api_reference_sheet(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            PNG image
        """
        with self._client_wrapper.httpx_client.stream(
            "api/reference/sheet",
            method="GET",
            params={
                "set": set_,
                "detail": detail,
                "partIds": part_ids,
                "physics": physics,
                "ParamAngleX": param_angle_x,
                "ParamAngleY": param_angle_y,
                "ParamAngleZ": param_angle_z,
                "width": width,
                "height": height,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    @contextlib.contextmanager
    def post_api_qa_failure_image(
        self,
        *,
        pose_id: str,
        region: str,
        before_pose_id: typing.Optional[str] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        values: typing.Optional[typing.Dict[str, float]] = OMIT,
        before_values: typing.Optional[typing.Dict[str, float]] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[int] = OMIT,
        supersample: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        pose_id : str

        region : str

        before_pose_id : typing.Optional[str]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        before_values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[int]

        supersample : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            PNG image
        """
        with self._client_wrapper.httpx_client.stream(
            "api/qa/failure-image",
            method="POST",
            json={
                "poseId": pose_id,
                "region": region,
                "beforePoseId": before_pose_id,
                "width": width,
                "height": height,
                "physics": physics,
                "values": values,
                "beforeValues": before_values,
                "physicsTime": physics_time,
                "physicsSteps": physics_steps,
                "supersample": supersample,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def optional_bridge_connection_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bridge/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def optional_cubism_bridge_requires_idle_api110server(
        self, *, request: PostApiBridgePoseRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : PostApiBridgePoseRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bridge/pose",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostApiBridgePoseRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_api_sample(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/sample",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_exports_bundle(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/exports/bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_playback_motion(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiPlaybackMotionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiPlaybackMotionResponse]
            Motion state; GET also returns the loaded native clip or null.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback/motion",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiPlaybackMotionResponse,
                    parse_obj_as(
                        type_=GetApiPlaybackMotionResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_playback_motion(
        self, *, request: PostApiPlaybackMotionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostApiPlaybackMotionResponse]:
        """
        Parameters
        ----------
        request : PostApiPlaybackMotionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiPlaybackMotionResponse]
            Motion state; GET also returns the loaded native clip or null.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback/motion",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostApiPlaybackMotionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiPlaybackMotionResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackMotionResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    @contextlib.contextmanager
    def get_api_playback_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            SSE latest playback state
        """
        with self._client_wrapper.httpx_client.stream(
            "api/playback/events",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_api_playback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiPlaybackResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiPlaybackResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiPlaybackResponse,
                    parse_obj_as(
                        type_=GetApiPlaybackResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_playback_parameters(
        self,
        *,
        source: str,
        sequence: int,
        values: typing.Dict[str, float],
        expected_session_id: typing.Optional[str] = OMIT,
        expected_model_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiPlaybackParametersResponse]:
        """
        Parameters
        ----------
        source : str

        sequence : int
            Strictly increasing per source. Use a new source ID for a new input session.

        values : typing.Dict[str, float]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        expected_session_id : typing.Optional[str]
            Reject when the service session differs.

        expected_model_version : typing.Optional[int]
            Reject when the loaded model version differs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiPlaybackParametersResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback/parameters",
            method="POST",
            json={
                "expectedSessionId": expected_session_id,
                "expectedModelVersion": expected_model_version,
                "source": source,
                "sequence": sequence,
                "values": values,
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
                    PostApiPlaybackParametersResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackParametersResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_playback_control(
        self,
        *,
        command: PostApiPlaybackControlRequestCommand,
        mode: typing.Optional[PostApiPlaybackControlRequestMode] = OMIT,
        x: typing.Optional[float] = OMIT,
        y: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiPlaybackControlResponse]:
        """
        Parameters
        ----------
        command : PostApiPlaybackControlRequestCommand

        mode : typing.Optional[PostApiPlaybackControlRequestMode]

        x : typing.Optional[float]

        y : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiPlaybackControlResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback/control",
            method="POST",
            json={
                "command": command,
                "mode": mode,
                "x": x,
                "y": y,
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
                    PostApiPlaybackControlResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackControlResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_playback_reload(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostApiPlaybackReloadResponse]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiPlaybackReloadResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/playback/reload",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiPlaybackReloadResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackReloadResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_api_checkpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/checkpoints",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_checkpoints(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/checkpoints",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def post_api_checkpoints_restore(
        self, *, id: str, expected_revision: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        expected_revision : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/checkpoints/restore",
            method="POST",
            json={
                "id": id,
                "expectedRevision": expected_revision,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_context(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/context",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_parts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/parts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_deformers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/deformers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/params",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_modeling(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_modeling_audit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling/audit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_modeling_techniques(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling/techniques",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_modeling_role_suggestions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling/role-suggestions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_modeling_artmesh_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling/artmesh-presets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_rig_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/rig/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_rig_validate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/rig/validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_rig_inspect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/rig/inspect",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_reference(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/reference",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_qa_golden(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/qa/golden",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_bundle(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bundle",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/schema",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_changes(
        self, *, since: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        since : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/changes",
            method="GET",
            params={
                "since": since,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_parts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/parts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_deformers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/deformers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_rig(
        self, *, include_assets: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/rig",
            method="GET",
            params={
                "includeAssets": include_assets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def put_api_rig(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        include_assets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        include_assets : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/rig",
            method="PUT",
            params={
                "includeAssets": include_assets,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_qa_check(
        self,
        *,
        poses: typing.Optional[typing.Sequence[str]] = OMIT,
        pose_samples: typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]] = OMIT,
        regions: typing.Optional[typing.Sequence[str]] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[float] = OMIT,
        min_coverage: typing.Optional[float] = OMIT,
        fail_on_edge_contact: typing.Optional[bool] = OMIT,
        expected_hashes: typing.Optional[typing.Dict[str, str]] = OMIT,
        check_triangle_distortion: typing.Optional[bool] = OMIT,
        max_triangle_stretch_ratio: typing.Optional[float] = OMIT,
        max_triangle_compression_ratio: typing.Optional[float] = OMIT,
        max_triangle_anisotropy: typing.Optional[float] = OMIT,
        motion_sweep: typing.Optional[QaCheckRequestMotionSweep] = OMIT,
        supersample: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        poses : typing.Optional[typing.Sequence[str]]

        pose_samples : typing.Optional[typing.Sequence[QaCheckRequestPoseSamplesItem]]

        regions : typing.Optional[typing.Sequence[str]]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[float]

        min_coverage : typing.Optional[float]

        fail_on_edge_contact : typing.Optional[bool]

        expected_hashes : typing.Optional[typing.Dict[str, str]]

        check_triangle_distortion : typing.Optional[bool]

        max_triangle_stretch_ratio : typing.Optional[float]

        max_triangle_compression_ratio : typing.Optional[float]

        max_triangle_anisotropy : typing.Optional[float]

        motion_sweep : typing.Optional[QaCheckRequestMotionSweep]

        supersample : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/qa/check",
            method="POST",
            json={
                "poses": poses,
                "poseSamples": convert_and_respect_annotation_metadata(
                    object_=pose_samples, annotation=typing.Sequence[QaCheckRequestPoseSamplesItem], direction="write"
                ),
                "regions": regions,
                "width": width,
                "height": height,
                "physics": physics,
                "physicsTime": physics_time,
                "physicsSteps": physics_steps,
                "minCoverage": min_coverage,
                "failOnEdgeContact": fail_on_edge_contact,
                "expectedHashes": expected_hashes,
                "checkTriangleDistortion": check_triangle_distortion,
                "maxTriangleStretchRatio": max_triangle_stretch_ratio,
                "maxTriangleCompressionRatio": max_triangle_compression_ratio,
                "maxTriangleAnisotropy": max_triangle_anisotropy,
                "motionSweep": convert_and_respect_annotation_metadata(
                    object_=motion_sweep, annotation=QaCheckRequestMotionSweep, direction="write"
                ),
                "supersample": supersample,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_modeling_transaction(
        self, *, request: TransactionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : TransactionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/modeling/transaction",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TransactionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_assets_externalize(
        self,
        *,
        rig: typing.Dict[str, typing.Any],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Disabled by default (403 legacy_write_api_disabled). Prefer /api/modeling/transaction. Explicit --allow-legacy-writes enables the legacy bypass.

        Parameters
        ----------
        rig : typing.Dict[str, typing.Any]

        dry_run : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/assets/externalize",
            method="POST",
            json={
                "rig": rig,
                "dryRun": dry_run,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    @contextlib.asynccontextmanager
    async def get_api_screenshot(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            PNG image
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/screenshot",
            method="GET",
            params={
                "set": set_,
                "detail": detail,
                "partIds": part_ids,
                "physics": physics,
                "ParamAngleX": param_angle_x,
                "ParamAngleY": param_angle_y,
                "ParamAngleZ": param_angle_z,
                "width": width,
                "height": height,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    @contextlib.asynccontextmanager
    async def get_api_reference_sheet(
        self,
        *,
        set_: typing.Optional[str] = None,
        detail: typing.Optional[str] = None,
        part_ids: typing.Optional[str] = None,
        physics: typing.Optional[str] = None,
        param_angle_x: typing.Optional[str] = None,
        param_angle_y: typing.Optional[str] = None,
        param_angle_z: typing.Optional[str] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        set_ : typing.Optional[str]

        detail : typing.Optional[str]

        part_ids : typing.Optional[str]

        physics : typing.Optional[str]

        param_angle_x : typing.Optional[str]

        param_angle_y : typing.Optional[str]

        param_angle_z : typing.Optional[str]

        width : typing.Optional[str]

        height : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            PNG image
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/reference/sheet",
            method="GET",
            params={
                "set": set_,
                "detail": detail,
                "partIds": part_ids,
                "physics": physics,
                "ParamAngleX": param_angle_x,
                "ParamAngleY": param_angle_y,
                "ParamAngleZ": param_angle_z,
                "width": width,
                "height": height,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    @contextlib.asynccontextmanager
    async def post_api_qa_failure_image(
        self,
        *,
        pose_id: str,
        region: str,
        before_pose_id: typing.Optional[str] = OMIT,
        width: typing.Optional[float] = OMIT,
        height: typing.Optional[float] = OMIT,
        physics: typing.Optional[bool] = OMIT,
        values: typing.Optional[typing.Dict[str, float]] = OMIT,
        before_values: typing.Optional[typing.Dict[str, float]] = OMIT,
        physics_time: typing.Optional[float] = OMIT,
        physics_steps: typing.Optional[int] = OMIT,
        supersample: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        pose_id : str

        region : str

        before_pose_id : typing.Optional[str]

        width : typing.Optional[float]

        height : typing.Optional[float]

        physics : typing.Optional[bool]

        values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        before_values : typing.Optional[typing.Dict[str, float]]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        physics_time : typing.Optional[float]

        physics_steps : typing.Optional[int]

        supersample : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            PNG image
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/qa/failure-image",
            method="POST",
            json={
                "poseId": pose_id,
                "region": region,
                "beforePoseId": before_pose_id,
                "width": width,
                "height": height,
                "physics": physics,
                "values": values,
                "beforeValues": before_values,
                "physicsTime": physics_time,
                "physicsSteps": physics_steps,
                "supersample": supersample,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def optional_bridge_connection_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bridge/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def optional_cubism_bridge_requires_idle_api110server(
        self, *, request: PostApiBridgePoseRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : PostApiBridgePoseRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bridge/pose",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostApiBridgePoseRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_api_sample(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/sample",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_exports_bundle(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/exports/bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_playback_motion(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiPlaybackMotionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiPlaybackMotionResponse]
            Motion state; GET also returns the loaded native clip or null.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback/motion",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiPlaybackMotionResponse,
                    parse_obj_as(
                        type_=GetApiPlaybackMotionResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_playback_motion(
        self, *, request: PostApiPlaybackMotionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostApiPlaybackMotionResponse]:
        """
        Parameters
        ----------
        request : PostApiPlaybackMotionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiPlaybackMotionResponse]
            Motion state; GET also returns the loaded native clip or null.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback/motion",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostApiPlaybackMotionRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiPlaybackMotionResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackMotionResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    @contextlib.asynccontextmanager
    async def get_api_playback_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            SSE latest playback state
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/playback/events",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
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
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 409:
                        raise ConflictError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Dict[str, typing.Any],
                                parse_obj_as(
                                    type_=typing.Dict[str, typing.Any],
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_api_playback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiPlaybackResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiPlaybackResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiPlaybackResponse,
                    parse_obj_as(
                        type_=GetApiPlaybackResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_playback_parameters(
        self,
        *,
        source: str,
        sequence: int,
        values: typing.Dict[str, float],
        expected_session_id: typing.Optional[str] = OMIT,
        expected_model_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiPlaybackParametersResponse]:
        """
        Parameters
        ----------
        source : str

        sequence : int
            Strictly increasing per source. Use a new source ID for a new input session.

        values : typing.Dict[str, float]
            Finite model parameter values. Playback also requires known IDs and values within their declared ranges.

        expected_session_id : typing.Optional[str]
            Reject when the service session differs.

        expected_model_version : typing.Optional[int]
            Reject when the loaded model version differs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiPlaybackParametersResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback/parameters",
            method="POST",
            json={
                "expectedSessionId": expected_session_id,
                "expectedModelVersion": expected_model_version,
                "source": source,
                "sequence": sequence,
                "values": values,
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
                    PostApiPlaybackParametersResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackParametersResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_playback_control(
        self,
        *,
        command: PostApiPlaybackControlRequestCommand,
        mode: typing.Optional[PostApiPlaybackControlRequestMode] = OMIT,
        x: typing.Optional[float] = OMIT,
        y: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiPlaybackControlResponse]:
        """
        Parameters
        ----------
        command : PostApiPlaybackControlRequestCommand

        mode : typing.Optional[PostApiPlaybackControlRequestMode]

        x : typing.Optional[float]

        y : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiPlaybackControlResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback/control",
            method="POST",
            json={
                "command": command,
                "mode": mode,
                "x": x,
                "y": y,
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
                    PostApiPlaybackControlResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackControlResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_playback_reload(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostApiPlaybackReloadResponse]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiPlaybackReloadResponse]
            Transient playback state; not a render acknowledgment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/playback/reload",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiPlaybackReloadResponse,
                    parse_obj_as(
                        type_=PostApiPlaybackReloadResponse,
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_api_checkpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/checkpoints",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_checkpoints(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/checkpoints",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def post_api_checkpoints_restore(
        self, *, id: str, expected_revision: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        expected_revision : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON result. Inspect ok, errors and commit/QA fields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/checkpoints/restore",
            method="POST",
            json={
                "id": id,
                "expectedRevision": expected_revision,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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
