

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from ..types.key_entry_v2 import KeyEntryV2
from .types.lookup_key_response import LookupKeyResponse
from .types.rotate_key_response import RotateKeyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def lookup_key(
        self, kid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LookupKeyResponse]:
        """
        Parameters
        ----------
        kid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LookupKeyResponse]
            Key found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/keys/{encode_path_param(kid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LookupKeyResponse,
                    parse_obj_as(
                        type_=LookupKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def rotate_key(
        self,
        *,
        old_kid: str,
        new_key: KeyEntryV2,
        proof_of_possession: typing.Dict[str, typing.Any],
        authorization_sig: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RotateKeyResponse]:
        """
        Parameters
        ----------
        old_kid : str

        new_key : KeyEntryV2

        proof_of_possession : typing.Dict[str, typing.Any]

        authorization_sig : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RotateKeyResponse]
            Key rotated
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/keys/rotate",
            method="POST",
            json={
                "old_kid": old_kid,
                "new_key": convert_and_respect_annotation_metadata(
                    object_=new_key, annotation=KeyEntryV2, direction="write"
                ),
                "proof_of_possession": proof_of_possession,
                "authorization_sig": authorization_sig,
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
                    RotateKeyResponse,
                    parse_obj_as(
                        type_=RotateKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def lookup_key(
        self, kid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LookupKeyResponse]:
        """
        Parameters
        ----------
        kid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LookupKeyResponse]
            Key found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/keys/{encode_path_param(kid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LookupKeyResponse,
                    parse_obj_as(
                        type_=LookupKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def rotate_key(
        self,
        *,
        old_kid: str,
        new_key: KeyEntryV2,
        proof_of_possession: typing.Dict[str, typing.Any],
        authorization_sig: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RotateKeyResponse]:
        """
        Parameters
        ----------
        old_kid : str

        new_key : KeyEntryV2

        proof_of_possession : typing.Dict[str, typing.Any]

        authorization_sig : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RotateKeyResponse]
            Key rotated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/keys/rotate",
            method="POST",
            json={
                "old_kid": old_kid,
                "new_key": convert_and_respect_annotation_metadata(
                    object_=new_key, annotation=KeyEntryV2, direction="write"
                ),
                "proof_of_possession": proof_of_possession,
                "authorization_sig": authorization_sig,
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
                    RotateKeyResponse,
                    parse_obj_as(
                        type_=RotateKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
