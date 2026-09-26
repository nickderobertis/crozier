

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.extract_response import ExtractResponse
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExtractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def warmup_extract_api_kits_warmup_extract_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Prime the vision provider connection so the first /extract call is warm.

        Deliberately uses probe(timeout=5) — a 5s deviation from the 30s default
        because this is a best-effort fire-and-forget warmup; we swallow all
        failures and always return 204 so the frontend never sees an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kits/_warmup/extract",
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

    def extract(
        self,
        kit_id: str,
        *,
        image_url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtractResponse]:
        """
        Extract per-field inferences from a product image.

        Uses the vision provider (registry role "vision"); falls back to "llm" if
        the vision role is unavailable (R2 mitigation).

        Reserved-prefix guard: POST to kit_id='_warmup' returns 404 — defensive
        against POST collision with the GET /_warmup/extract warmup endpoint.

        Parameters
        ----------
        kit_id : str

        image_url : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/extract",
            method="POST",
            json={
                "description": description,
                "image_url": image_url,
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
                    ExtractResponse,
                    parse_obj_as(
                        type_=ExtractResponse,
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


class AsyncRawExtractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def warmup_extract_api_kits_warmup_extract_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Prime the vision provider connection so the first /extract call is warm.

        Deliberately uses probe(timeout=5) — a 5s deviation from the 30s default
        because this is a best-effort fire-and-forget warmup; we swallow all
        failures and always return 204 so the frontend never sees an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kits/_warmup/extract",
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

    async def extract(
        self,
        kit_id: str,
        *,
        image_url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtractResponse]:
        """
        Extract per-field inferences from a product image.

        Uses the vision provider (registry role "vision"); falls back to "llm" if
        the vision role is unavailable (R2 mitigation).

        Reserved-prefix guard: POST to kit_id='_warmup' returns 404 — defensive
        against POST collision with the GET /_warmup/extract warmup endpoint.

        Parameters
        ----------
        kit_id : str

        image_url : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/extract",
            method="POST",
            json={
                "description": description,
                "image_url": image_url,
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
                    ExtractResponse,
                    parse_obj_as(
                        type_=ExtractResponse,
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
