

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.create_document_response import CreateDocumentResponse
from ..types.delete_document_request import DeleteDocumentRequest
from ..types.delete_document_response import DeleteDocumentResponse
from ..types.delete_documents_response import DeleteDocumentsResponse
from ..types.get_document_response import GetDocumentResponse
from ..types.get_documents_response import GetDocumentsResponse
from ..types.http_validation_error import HttpValidationError
from ..types.update_document_response import UpdateDocumentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_document(
        self,
        domain: str,
        *,
        request: typing.Any,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CreateDocumentResponse]]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CreateDocumentResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/create",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateDocumentResponse],
                    parse_obj_as(
                        type_=typing.List[CreateDocumentResponse],
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

    def batch_create_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CreateDocumentResponse]]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CreateDocumentResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/batch-create",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateDocumentResponse],
                    parse_obj_as(
                        type_=typing.List[CreateDocumentResponse],
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

    def get_document_by_id(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="GET",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDocumentResponse,
                    parse_obj_as(
                        type_=GetDocumentResponse,
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

    def delete_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="DELETE",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    def update_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        document: typing.Optional[str] = OMIT,
        chunk: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        authed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        document : typing.Optional[str]
            The updated content of the document that will be returned to Ask Fern during document retrieval. If not provided, this field will remain unchanged.

        chunk : typing.Optional[str]
            The updated textual content that should be vectorized when indexing the document. If not provided, this field will remain unchanged.

        title : typing.Optional[str]
            The updated title of the document. If not provided, this field will remain unchanged.

        url : typing.Optional[str]
            The updated url of the document. If not provided, this field will remain unchanged.

        version : typing.Optional[str]
            The updated version of the document. If not provided, this field will remain unchanged.

        product : typing.Optional[str]
            The updated product of the document. If not provided, this field will remain unchanged.

        keywords : typing.Optional[typing.Sequence[str]]
            The updated keywords of the document. If not provided, this field will remain unchanged.

        authed : typing.Optional[bool]
            The updated authed status of the document. If not provided, this field will remain unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="PATCH",
            json={
                "document": document,
                "chunk": chunk,
                "title": title,
                "url": url,
                "version": version,
                "product": product,
                "keywords": keywords,
                "authed": authed,
            },
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateDocumentResponse,
                    parse_obj_as(
                        type_=UpdateDocumentResponse,
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

    def delete_document_by_id(
        self,
        domain: str,
        *,
        document_id: str,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str
            The unique identifier of the document to delete

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/delete",
            method="DELETE",
            json={
                "document_id": document_id,
            },
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    def batch_delete_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[DeleteDocumentRequest],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[DeleteDocumentRequest]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/batch-delete",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[DeleteDocumentRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    def get_documents(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDocumentsResponse]:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of documents per page

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDocumentsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDocumentsResponse,
                    parse_obj_as(
                        type_=GetDocumentsResponse,
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

    def delete_documents(
        self,
        domain: str,
        *,
        product: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        url_prefix: typing.Optional[str] = None,
        all_: typing.Optional[bool] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDocumentsResponse]:
        """
        Delete the documents of a domain, narrowed by the provided filters. Filters are combined with AND, so a document is
        only deleted when it matches all of them. At least one filter is required, or pass `all=true` to delete every
        document. The `x-fern-basepath` header narrows the deletion to a single basepath.

        Parameters
        ----------
        domain : str

        product : typing.Optional[str]
            Only delete documents whose product matches this value exactly.

        version : typing.Optional[str]
            Only delete documents whose version matches this value exactly.

        url_prefix : typing.Optional[str]
            Only delete documents whose url starts with this value.

        all_ : typing.Optional[bool]
            Delete every document in the domain and basepath. Cannot be combined with the product, version or url_prefix filters.

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDocumentsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}",
            method="DELETE",
            params={
                "product": product,
                "version": version,
                "url_prefix": url_prefix,
                "all": all_,
            },
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentsResponse,
                    parse_obj_as(
                        type_=DeleteDocumentsResponse,
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

    def delete_all_documents(
        self,
        domain: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/delete-all",
            method="DELETE",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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


class AsyncRawDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_document(
        self,
        domain: str,
        *,
        request: typing.Any,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CreateDocumentResponse]]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CreateDocumentResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/create",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateDocumentResponse],
                    parse_obj_as(
                        type_=typing.List[CreateDocumentResponse],
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

    async def batch_create_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CreateDocumentResponse]]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CreateDocumentResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/batch-create",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CreateDocumentResponse],
                    parse_obj_as(
                        type_=typing.List[CreateDocumentResponse],
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

    async def get_document_by_id(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="GET",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDocumentResponse,
                    parse_obj_as(
                        type_=GetDocumentResponse,
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

    async def delete_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="DELETE",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    async def update_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        document: typing.Optional[str] = OMIT,
        chunk: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        authed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        document : typing.Optional[str]
            The updated content of the document that will be returned to Ask Fern during document retrieval. If not provided, this field will remain unchanged.

        chunk : typing.Optional[str]
            The updated textual content that should be vectorized when indexing the document. If not provided, this field will remain unchanged.

        title : typing.Optional[str]
            The updated title of the document. If not provided, this field will remain unchanged.

        url : typing.Optional[str]
            The updated url of the document. If not provided, this field will remain unchanged.

        version : typing.Optional[str]
            The updated version of the document. If not provided, this field will remain unchanged.

        product : typing.Optional[str]
            The updated product of the document. If not provided, this field will remain unchanged.

        keywords : typing.Optional[typing.Sequence[str]]
            The updated keywords of the document. If not provided, this field will remain unchanged.

        authed : typing.Optional[bool]
            The updated authed status of the document. If not provided, this field will remain unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/{encode_path_param(document_id)}",
            method="PATCH",
            json={
                "document": document,
                "chunk": chunk,
                "title": title,
                "url": url,
                "version": version,
                "product": product,
                "keywords": keywords,
                "authed": authed,
            },
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateDocumentResponse,
                    parse_obj_as(
                        type_=UpdateDocumentResponse,
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

    async def delete_document_by_id(
        self,
        domain: str,
        *,
        document_id: str,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        document_id : str
            The unique identifier of the document to delete

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/delete",
            method="DELETE",
            json={
                "document_id": document_id,
            },
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    async def batch_delete_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[DeleteDocumentRequest],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[DeleteDocumentRequest]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/batch-delete",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[DeleteDocumentRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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

    async def get_documents(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDocumentsResponse]:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of documents per page

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDocumentsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDocumentsResponse,
                    parse_obj_as(
                        type_=GetDocumentsResponse,
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

    async def delete_documents(
        self,
        domain: str,
        *,
        product: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        url_prefix: typing.Optional[str] = None,
        all_: typing.Optional[bool] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDocumentsResponse]:
        """
        Delete the documents of a domain, narrowed by the provided filters. Filters are combined with AND, so a document is
        only deleted when it matches all of them. At least one filter is required, or pass `all=true` to delete every
        document. The `x-fern-basepath` header narrows the deletion to a single basepath.

        Parameters
        ----------
        domain : str

        product : typing.Optional[str]
            Only delete documents whose product matches this value exactly.

        version : typing.Optional[str]
            Only delete documents whose version matches this value exactly.

        url_prefix : typing.Optional[str]
            Only delete documents whose url starts with this value.

        all_ : typing.Optional[bool]
            Delete every document in the domain and basepath. Cannot be combined with the product, version or url_prefix filters.

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDocumentsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}",
            method="DELETE",
            params={
                "product": product,
                "version": version,
                "url_prefix": url_prefix,
                "all": all_,
            },
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentsResponse,
                    parse_obj_as(
                        type_=DeleteDocumentsResponse,
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

    async def delete_all_documents(
        self,
        domain: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDocumentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"document/{encode_path_param(domain)}/delete-all",
            method="DELETE",
            headers={
                "x-fern-basepath": str(fern_basepath) if fern_basepath is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDocumentResponse,
                    parse_obj_as(
                        type_=DeleteDocumentResponse,
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
