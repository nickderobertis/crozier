

import json
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.photo import Photo
from .types.proof_response import ProofResponse
from .types.retouch_photo_request_options import RetouchPhotoRequestOptions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPhotosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retouch_photo(
        self,
        *,
        brief: str,
        options: typing.Optional[RetouchPhotoRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Photo]:
        """
        Parameters
        ----------
        brief : str

        options : typing.Optional[RetouchPhotoRequestOptions]
            How to retouch the photo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Photo]
            The retouched photo
        """
        _response = self._client_wrapper.httpx_client.request(
            "photos/retouch",
            method="POST",
            data={
                "brief": brief,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Photo,
                    parse_obj_as(
                        type_=Photo,
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

    def get_proof(
        self, photo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProofResponse]:
        """
        Parameters
        ----------
        photo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProofResponse]
            The proof of the photo
        """
        _response = self._client_wrapper.httpx_client.request(
            f"photos/{encode_path_param(photo_id)}/proof",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProofResponse,
                    parse_obj_as(
                        type_=ProofResponse,
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


class AsyncRawPhotosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retouch_photo(
        self,
        *,
        brief: str,
        options: typing.Optional[RetouchPhotoRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Photo]:
        """
        Parameters
        ----------
        brief : str

        options : typing.Optional[RetouchPhotoRequestOptions]
            How to retouch the photo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Photo]
            The retouched photo
        """
        _response = await self._client_wrapper.httpx_client.request(
            "photos/retouch",
            method="POST",
            data={
                "brief": brief,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Photo,
                    parse_obj_as(
                        type_=Photo,
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

    async def get_proof(
        self, photo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProofResponse]:
        """
        Parameters
        ----------
        photo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProofResponse]
            The proof of the photo
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"photos/{encode_path_param(photo_id)}/proof",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProofResponse,
                    parse_obj_as(
                        type_=ProofResponse,
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
