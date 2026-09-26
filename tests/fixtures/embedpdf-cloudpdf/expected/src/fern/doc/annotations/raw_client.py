

import contextlib
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
from ...errors.conflict_error import ConflictError
from ...errors.not_found_error import NotFoundError
from ...types.doc_annotations_create200response import DocAnnotationsCreate200Response
from ...types.doc_annotations_create_request import DocAnnotationsCreateRequest
from ...types.doc_annotations_delete200response import DocAnnotationsDelete200Response
from ...types.doc_annotations_export_appearance_request import DocAnnotationsExportAppearanceRequest
from ...types.doc_annotations_flatten200response import DocAnnotationsFlatten200Response
from ...types.doc_annotations_flatten_request import DocAnnotationsFlattenRequest
from ...types.doc_annotations_list200response import DocAnnotationsList200Response
from ...types.doc_annotations_list_all200response import DocAnnotationsListAll200Response
from ...types.doc_annotations_update200response import DocAnnotationsUpdate200Response
from ...types.doc_annotations_update_request import DocAnnotationsUpdateRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAnnotationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsListAll200Response]:
        """
        Returns one entry per page plus the audit-log cursor for reconciling subsequent document events. Page order is unspecified; join by `pageState.pageObjectNumber` when display order matters.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocAnnotationsListAll200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/items",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsListAll200Response,
                    parse_obj_as(
                        type_=DocAnnotationsListAll200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def list(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsList200Response]:
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
        HttpResponse[DocAnnotationsList200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsList200Response,
                    parse_obj_as(
                        type_=DocAnnotationsList200Response,
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

    def create(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsCreateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsCreate200Response]:
        """
        Doc JWTs may instead carry collab scopes (annotations:create:self, …) that refine per-annotation authorship rules; the API token is exempt from both.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsCreateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocAnnotationsCreate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items",
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
                    DocAnnotationsCreate200Response,
                    parse_obj_as(
                        type_=DocAnnotationsCreate200Response,
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

    def delete(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsDelete200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocAnnotationsDelete200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/{encode_path_param(annot_key)}",
            method="DELETE",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsDelete200Response,
                    parse_obj_as(
                        type_=DocAnnotationsDelete200Response,
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

    def update(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        request: DocAnnotationsUpdateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsUpdate200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        request : DocAnnotationsUpdateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocAnnotationsUpdate200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/{encode_path_param(annot_key)}",
            method="PATCH",
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
                    DocAnnotationsUpdate200Response,
                    parse_obj_as(
                        type_=DocAnnotationsUpdate200Response,
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
    def export_appearance(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsExportAppearanceRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsExportAppearanceRequest

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
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/appearance",
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
        page_key: str,
        *,
        request: DocAnnotationsFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocAnnotationsFlatten200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocAnnotationsFlatten200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/flatten",
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
                    DocAnnotationsFlatten200Response,
                    parse_obj_as(
                        type_=DocAnnotationsFlatten200Response,
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


class AsyncRawAnnotationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsListAll200Response]:
        """
        Returns one entry per page plus the audit-log cursor for reconciling subsequent document events. Page order is unspecified; join by `pageState.pageObjectNumber` when display order matters.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocAnnotationsListAll200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/items",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsListAll200Response,
                    parse_obj_as(
                        type_=DocAnnotationsListAll200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def list(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsList200Response]:
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
        AsyncHttpResponse[DocAnnotationsList200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsList200Response,
                    parse_obj_as(
                        type_=DocAnnotationsList200Response,
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

    async def create(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsCreateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsCreate200Response]:
        """
        Doc JWTs may instead carry collab scopes (annotations:create:self, …) that refine per-annotation authorship rules; the API token is exempt from both.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsCreateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocAnnotationsCreate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items",
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
                    DocAnnotationsCreate200Response,
                    parse_obj_as(
                        type_=DocAnnotationsCreate200Response,
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

    async def delete(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsDelete200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocAnnotationsDelete200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/{encode_path_param(annot_key)}",
            method="DELETE",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocAnnotationsDelete200Response,
                    parse_obj_as(
                        type_=DocAnnotationsDelete200Response,
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

    async def update(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        request: DocAnnotationsUpdateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsUpdate200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        request : DocAnnotationsUpdateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocAnnotationsUpdate200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/{encode_path_param(annot_key)}",
            method="PATCH",
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
                    DocAnnotationsUpdate200Response,
                    parse_obj_as(
                        type_=DocAnnotationsUpdate200Response,
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
    async def export_appearance(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsExportAppearanceRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsExportAppearanceRequest

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
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/appearance",
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
        page_key: str,
        *,
        request: DocAnnotationsFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocAnnotationsFlatten200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocAnnotationsFlatten200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/annotations/pages/{encode_path_param(page_key)}/items/flatten",
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
                    DocAnnotationsFlatten200Response,
                    parse_obj_as(
                        type_=DocAnnotationsFlatten200Response,
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
