

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from ...types.doc_redactions_apply200response import DocRedactionsApply200Response
from ...types.doc_redactions_apply_request import DocRedactionsApplyRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRedactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def apply(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocRedactionsApplyRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocRedactionsApply200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocRedactionsApplyRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocRedactionsApply200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/redactions/apply",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocRedactionsApply200Response,
                    parse_obj_as(
                        type_=DocRedactionsApply200Response,
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


class AsyncRawRedactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def apply(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocRedactionsApplyRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocRedactionsApply200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocRedactionsApplyRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocRedactionsApply200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/redactions/apply",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocRedactionsApply200Response,
                    parse_obj_as(
                        type_=DocRedactionsApply200Response,
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
