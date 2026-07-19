

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.error import Error
from .types.search_index_operator import SearchIndexOperator
from .types.search_index_public_key import SearchIndexPublicKey
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIndexClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_index(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        operator: typing.Optional[SearchIndexOperator] = OMIT,
        public_key: typing.Optional[SearchIndexPublicKey] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Error]:
        """
        EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases.
        The results returned from this endpoint may be incomplete.

        Parameters
        ----------
        email : typing.Optional[str]

        hash : typing.Optional[str]

        operator : typing.Optional[SearchIndexOperator]

        public_key : typing.Optional[SearchIndexPublicKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/index/retrieve",
            method="POST",
            json={
                "email": email,
                "hash": hash,
                "operator": operator,
                "publicKey": convert_and_respect_annotation_metadata(
                    object_=public_key, annotation=SearchIndexPublicKey, direction="write"
                ),
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
                    Error,
                    parse_obj_as(
                        type_=Error,
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


class AsyncRawIndexClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_index(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        operator: typing.Optional[SearchIndexOperator] = OMIT,
        public_key: typing.Optional[SearchIndexPublicKey] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Error]:
        """
        EXPERIMENTAL - this endpoint is offered as best effort only and may be changed or removed in future releases.
        The results returned from this endpoint may be incomplete.

        Parameters
        ----------
        email : typing.Optional[str]

        hash : typing.Optional[str]

        operator : typing.Optional[SearchIndexOperator]

        public_key : typing.Optional[SearchIndexPublicKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/index/retrieve",
            method="POST",
            json={
                "email": email,
                "hash": hash,
                "operator": operator,
                "publicKey": convert_and_respect_annotation_metadata(
                    object_=public_key, annotation=SearchIndexPublicKey, direction="write"
                ),
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
                    Error,
                    parse_obj_as(
                        type_=Error,
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
