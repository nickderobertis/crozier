

import contextlib
import typing
from json.decoder import JSONDecodeError

from ... import core
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from ...types.doc_pages_delete200response import DocPagesDelete200Response
from ...types.doc_pages_delete_request import DocPagesDeleteRequest
from ...types.doc_pages_extract_request import DocPagesExtractRequest
from ...types.doc_pages_flatten200response import DocPagesFlatten200Response
from ...types.doc_pages_flatten_request import DocPagesFlattenRequest
from ...types.doc_pages_insert200response import DocPagesInsert200Response
from ...types.doc_pages_insert_blank200response import DocPagesInsertBlank200Response
from ...types.doc_pages_insert_blank_request import DocPagesInsertBlankRequest
from ...types.doc_pages_move200response import DocPagesMove200Response
from ...types.doc_pages_move_request import DocPagesMoveRequest
from ...types.doc_pages_remove_name200response import DocPagesRemoveName200Response
from ...types.doc_pages_remove_name_request import DocPagesRemoveNameRequest
from ...types.doc_pages_rotate200response import DocPagesRotate200Response
from ...types.doc_pages_rotate_request import DocPagesRotateRequest
from ...types.doc_pages_set_name200response import DocPagesSetName200Response
from ...types.doc_pages_set_name_request import DocPagesSetNameRequest
from ...types.doc_pages_set_scale200response import DocPagesSetScale200Response
from ...types.doc_pages_viewports200response import DocPagesViewports200Response
from .types.doc_pages_set_scale_request_measure import DocPagesSetScaleRequestMeasure
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_scale(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        measure: typing.Optional[DocPagesSetScaleRequestMeasure] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesSetScale200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        measure : typing.Optional[DocPagesSetScaleRequestMeasure]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesSetScale200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/{encode_path_param(page_key)}/scale",
            method="PUT",
            json={
                "measure": convert_and_respect_annotation_metadata(
                    object_=measure, annotation=typing.Optional[DocPagesSetScaleRequestMeasure], direction="write"
                ),
            },
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
                    DocPagesSetScale200Response,
                    parse_obj_as(
                        type_=DocPagesSetScale200Response,
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

    def viewports(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesViewports200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesViewports200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/{encode_path_param(page_key)}/viewports",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocPagesViewports200Response,
                    parse_obj_as(
                        type_=DocPagesViewports200Response,
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

    def delete(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesDeleteRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesDelete200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesDeleteRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesDelete200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/delete",
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
                    DocPagesDelete200Response,
                    parse_obj_as(
                        type_=DocPagesDelete200Response,
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

    @contextlib.contextmanager
    def extract(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesExtractRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        A read, not a mutation: the source document is untouched and no event is published. Body is `{"pageObjectNumbers": number[]}`; the response body is the new PDF.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesExtractRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/extract",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
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

    def flatten(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesFlatten200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesFlatten200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/flatten",
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
                    DocPagesFlatten200Response,
                    parse_obj_as(
                        type_=DocPagesFlatten200Response,
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

    def insert(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesInsert200Response]:
        """
        Multipart mutation envelope: a `body` field holding `{"destIndex"?: number}` (omitted → append) plus a `resource:source` file part carrying the standalone PDF whose pages are copied in. The inserted copies get fresh page object numbers, returned in insertion order.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesInsert200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/insert",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocPagesInsert200Response,
                    parse_obj_as(
                        type_=DocPagesInsert200Response,
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

    def insert_blank(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesInsertBlankRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesInsertBlank200Response]:
        """
        Body is `{"size": {"width", "height"}, "count"?, "destIndex"?}` — size in PDF points, count in [1, 100], destIndex omitted → append.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesInsertBlankRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesInsertBlank200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/insert-blank",
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
                    DocPagesInsertBlank200Response,
                    parse_obj_as(
                        type_=DocPagesInsertBlank200Response,
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

    def move(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesMoveRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesMove200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesMoveRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesMove200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/move",
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
                    DocPagesMove200Response,
                    parse_obj_as(
                        type_=DocPagesMove200Response,
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

    def set_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesSetNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesSetName200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesSetNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesSetName200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/names",
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
                    DocPagesSetName200Response,
                    parse_obj_as(
                        type_=DocPagesSetName200Response,
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

    def remove_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRemoveNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesRemoveName200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRemoveNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesRemoveName200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/names/delete",
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
                    DocPagesRemoveName200Response,
                    parse_obj_as(
                        type_=DocPagesRemoveName200Response,
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

    def rotate(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRotateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocPagesRotate200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRotateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocPagesRotate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/rotate",
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
                    DocPagesRotate200Response,
                    parse_obj_as(
                        type_=DocPagesRotate200Response,
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


class AsyncRawPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_scale(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        measure: typing.Optional[DocPagesSetScaleRequestMeasure] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesSetScale200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        measure : typing.Optional[DocPagesSetScaleRequestMeasure]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesSetScale200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/{encode_path_param(page_key)}/scale",
            method="PUT",
            json={
                "measure": convert_and_respect_annotation_metadata(
                    object_=measure, annotation=typing.Optional[DocPagesSetScaleRequestMeasure], direction="write"
                ),
            },
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
                    DocPagesSetScale200Response,
                    parse_obj_as(
                        type_=DocPagesSetScale200Response,
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

    async def viewports(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesViewports200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesViewports200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/{encode_path_param(page_key)}/viewports",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocPagesViewports200Response,
                    parse_obj_as(
                        type_=DocPagesViewports200Response,
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

    async def delete(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesDeleteRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesDelete200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesDeleteRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesDelete200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/delete",
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
                    DocPagesDelete200Response,
                    parse_obj_as(
                        type_=DocPagesDelete200Response,
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

    @contextlib.asynccontextmanager
    async def extract(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesExtractRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        A read, not a mutation: the source document is untouched and no event is published. Body is `{"pageObjectNumbers": number[]}`; the response body is the new PDF.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesExtractRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/extract",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
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

    async def flatten(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesFlatten200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesFlatten200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/flatten",
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
                    DocPagesFlatten200Response,
                    parse_obj_as(
                        type_=DocPagesFlatten200Response,
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

    async def insert(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesInsert200Response]:
        """
        Multipart mutation envelope: a `body` field holding `{"destIndex"?: number}` (omitted → append) plus a `resource:source` file part carrying the standalone PDF whose pages are copied in. The inserted copies get fresh page object numbers, returned in insertion order.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesInsert200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/insert",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocPagesInsert200Response,
                    parse_obj_as(
                        type_=DocPagesInsert200Response,
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

    async def insert_blank(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesInsertBlankRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesInsertBlank200Response]:
        """
        Body is `{"size": {"width", "height"}, "count"?, "destIndex"?}` — size in PDF points, count in [1, 100], destIndex omitted → append.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesInsertBlankRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesInsertBlank200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/insert-blank",
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
                    DocPagesInsertBlank200Response,
                    parse_obj_as(
                        type_=DocPagesInsertBlank200Response,
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

    async def move(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesMoveRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesMove200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesMoveRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesMove200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/move",
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
                    DocPagesMove200Response,
                    parse_obj_as(
                        type_=DocPagesMove200Response,
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

    async def set_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesSetNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesSetName200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesSetNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesSetName200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/names",
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
                    DocPagesSetName200Response,
                    parse_obj_as(
                        type_=DocPagesSetName200Response,
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

    async def remove_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRemoveNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesRemoveName200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRemoveNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesRemoveName200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/names/delete",
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
                    DocPagesRemoveName200Response,
                    parse_obj_as(
                        type_=DocPagesRemoveName200Response,
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

    async def rotate(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRotateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocPagesRotate200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRotateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocPagesRotate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/pages/rotate",
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
                    DocPagesRotate200Response,
                    parse_obj_as(
                        type_=DocPagesRotate200Response,
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
