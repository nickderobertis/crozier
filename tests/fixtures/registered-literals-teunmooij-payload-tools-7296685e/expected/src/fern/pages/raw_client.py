

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
from ..errors.not_found_error import NotFoundError
from ..types.error import Error
from ..types.pages import Pages
from ..types.pages_upsert_confirmation import PagesUpsertConfirmation
from ..types.pagess import Pagess
from ..types.shared_meta import SharedMeta
from ..types.where import Where
from .types.delete_pages_response import DeletePagesResponse
from .types.patch_pages_response import PatchPagesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_paginated_pages(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pagess]:
        """
        Find paginated Pages

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pagess]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "pages",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pagess,
                    parse_obj_as(
                        type_=Pagess,
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

    def create_a_new_page(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagesUpsertConfirmation]:
        """
        Create a new Page

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "pages",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
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

    def delete_multiple_pages(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeletePagesResponse]:
        """
        Delete all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletePagesResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "pages",
            method="DELETE",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePagesResponse,
                    parse_obj_as(
                        type_=DeletePagesResponse,
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

    def update_multiple_pages(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchPagesResponse]:
        """
        Update all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PatchPagesResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "pages",
            method="PATCH",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PatchPagesResponse,
                    parse_obj_as(
                        type_=PatchPagesResponse,
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

    def get_a_single_page_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pages]:
        """
        Get a single Page by its id

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pages]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id)}",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pages,
                    parse_obj_as(
                        type_=Pages,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def deletes_an_existing_page(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagesUpsertConfirmation]:
        """
        Deletes an existing Page

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id)}",
            method="DELETE",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def updates_a_page(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagesUpsertConfirmation]:
        """
        Updates a Page

        Parameters
        ----------
        id_ : str
            id of the Page

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def find_paginated_pages(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pagess]:
        """
        Find paginated Pages

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pagess]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pages",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pagess,
                    parse_obj_as(
                        type_=Pagess,
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

    async def create_a_new_page(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagesUpsertConfirmation]:
        """
        Create a new Page

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pages",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
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

    async def delete_multiple_pages(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeletePagesResponse]:
        """
        Delete all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletePagesResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pages",
            method="DELETE",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePagesResponse,
                    parse_obj_as(
                        type_=DeletePagesResponse,
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

    async def update_multiple_pages(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PatchPagesResponse]:
        """
        Update all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PatchPagesResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pages",
            method="PATCH",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PatchPagesResponse,
                    parse_obj_as(
                        type_=PatchPagesResponse,
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

    async def get_a_single_page_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pages]:
        """
        Get a single Page by its id

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pages]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id)}",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pages,
                    parse_obj_as(
                        type_=Pages,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def deletes_an_existing_page(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagesUpsertConfirmation]:
        """
        Deletes an existing Page

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id)}",
            method="DELETE",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def updates_a_page(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagesUpsertConfirmation]:
        """
        Updates a Page

        Parameters
        ----------
        id_ : str
            id of the Page

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagesUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pages/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "meta": convert_and_respect_annotation_metadata(object_=meta, annotation=SharedMeta, direction="write"),
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    PagesUpsertConfirmation,
                    parse_obj_as(
                        type_=PagesUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
