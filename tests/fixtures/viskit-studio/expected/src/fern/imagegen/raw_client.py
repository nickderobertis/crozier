

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.delete_kit_image_response import DeleteKitImageResponse
from ..types.generate_response import GenerateResponse
from ..types.http_validation_error import HttpValidationError
from ..types.kit_list_response import KitListResponse
from ..types.kit_meta_response import KitMetaResponse
from ..types.spec_in import SpecIn
from .types.generate_request_locale import GenerateRequestLocale
from .types.list_kits_api_kits_get_request_order import ListKitsApiKitsGetRequestOrder
from .types.list_kits_api_kits_get_request_sort import ListKitsApiKitsGetRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawImagegenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_kits(
        self,
        *,
        recent: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        min_score: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        sort: typing.Optional[ListKitsApiKitsGetRequestSort] = None,
        order: typing.Optional[ListKitsApiKitsGetRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KitListResponse]:
        """
        Return kits joined with their product catalog row, paginated & filtered.

        ``thumbs`` is the concatenation of up-to-5 hero png_paths (slot 1..5) and
        up-to-9 detail png_paths (M1..M9) — 14 slots total, NULL-padded for any
        missing rows.  Callers render placeholder cells for NULL entries.

        Standalone generated assets are also returned as catalog entries with
        ``source_type='asset'`` so non-kit generations remain visible in Catalog.

        ``recent=true`` preserves the Dashboard contract by returning kit rows
        only. Catalog calls leave ``recent`` false and receive kit plus asset rows.

        ``recent`` is otherwise advisory; sort defaults to ``created_at DESC`` to preserve
        the EPIC-7 Dashboard call shape (``?recent=true&limit=6``).  Catalog
        (EPIC-8) passes ``offset``, ``status``, ``locale``, ``min_score``,
        ``category``, ``sort``, ``order`` for filtered/paginated views.

        Parameters
        ----------
        recent : typing.Optional[bool]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]

        locale : typing.Optional[str]

        min_score : typing.Optional[int]

        category : typing.Optional[str]

        sku : typing.Optional[str]

        sort : typing.Optional[ListKitsApiKitsGetRequestSort]

        order : typing.Optional[ListKitsApiKitsGetRequestOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KitListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/kits",
            method="GET",
            params={
                "recent": recent,
                "limit": limit,
                "offset": offset,
                "status": status,
                "locale": locale,
                "min_score": min_score,
                "category": category,
                "sku": sku,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KitListResponse,
                    parse_obj_as(
                        type_=KitListResponse,
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

    def delete_generated_image(
        self, db_kit_id: int, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteKitImageResponse]:
        """
        Remove a generated image from a catalog kit slot and delete its PNG.

        Parameters
        ----------
        db_kit_id : int

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteKitImageResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(db_kit_id)}/images/{encode_path_param(image_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteKitImageResponse,
                    parse_obj_as(
                        type_=DeleteKitImageResponse,
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

    def get_kit_meta(
        self, db_kit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KitMetaResponse]:
        """
        Read result sidecars for *db_kit_id*; 404 if the kit root is unknown.

        Parameters
        ----------
        db_kit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KitMetaResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(db_kit_id)}/meta",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KitMetaResponse,
                    parse_obj_as(
                        type_=KitMetaResponse,
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

    def get_kit_events(
        self, kit_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Stream per-image status events for *kit_id* as text/event-stream.

        Returns 404 when the kit_id has never been published to the bus
        (callers can use this as a "kit not started" signal).  Each line
        conforms to the SSE wire format::

            data: {"image_id": "H1", "status": "color_locked", "progress": 0,
                   "brand_color_locked": true}

        Parameters
        ----------
        kit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def post_generate(
        self,
        kit_id: str,
        *,
        brand_color_hex: str,
        locale: GenerateRequestLocale,
        spec: SpecIn,
        retrieved_bestseller_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        template_scheme_ref: typing.Optional[str] = OMIT,
        template_slot_overrides: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GenerateResponse]:
        """
        Generate the 14-image kit for *kit_id*.

        Parameters
        ----------
        kit_id : str

        brand_color_hex : str

        locale : GenerateRequestLocale

        spec : SpecIn

        retrieved_bestseller_ids : typing.Optional[typing.Sequence[int]]

        style_prompt : typing.Optional[str]

        template_scheme_ref : typing.Optional[str]

        template_slot_overrides : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GenerateResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/generate",
            method="POST",
            json={
                "brand_color_hex": brand_color_hex,
                "locale": locale,
                "retrieved_bestseller_ids": retrieved_bestseller_ids,
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=SpecIn, direction="write"),
                "style_prompt": style_prompt,
                "template_scheme_ref": template_scheme_ref,
                "template_slot_overrides": template_slot_overrides,
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
                    GenerateResponse,
                    parse_obj_as(
                        type_=GenerateResponse,
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

    def get_generated_image(
        self, kit_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Serve a generated kit image by public kit id and slot id.

        Parameters
        ----------
        kit_id : str

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/images/{encode_path_param(image_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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


class AsyncRawImagegenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_kits(
        self,
        *,
        recent: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        locale: typing.Optional[str] = None,
        min_score: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        sort: typing.Optional[ListKitsApiKitsGetRequestSort] = None,
        order: typing.Optional[ListKitsApiKitsGetRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KitListResponse]:
        """
        Return kits joined with their product catalog row, paginated & filtered.

        ``thumbs`` is the concatenation of up-to-5 hero png_paths (slot 1..5) and
        up-to-9 detail png_paths (M1..M9) — 14 slots total, NULL-padded for any
        missing rows.  Callers render placeholder cells for NULL entries.

        Standalone generated assets are also returned as catalog entries with
        ``source_type='asset'`` so non-kit generations remain visible in Catalog.

        ``recent=true`` preserves the Dashboard contract by returning kit rows
        only. Catalog calls leave ``recent`` false and receive kit plus asset rows.

        ``recent`` is otherwise advisory; sort defaults to ``created_at DESC`` to preserve
        the EPIC-7 Dashboard call shape (``?recent=true&limit=6``).  Catalog
        (EPIC-8) passes ``offset``, ``status``, ``locale``, ``min_score``,
        ``category``, ``sort``, ``order`` for filtered/paginated views.

        Parameters
        ----------
        recent : typing.Optional[bool]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[str]

        locale : typing.Optional[str]

        min_score : typing.Optional[int]

        category : typing.Optional[str]

        sku : typing.Optional[str]

        sort : typing.Optional[ListKitsApiKitsGetRequestSort]

        order : typing.Optional[ListKitsApiKitsGetRequestOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KitListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/kits",
            method="GET",
            params={
                "recent": recent,
                "limit": limit,
                "offset": offset,
                "status": status,
                "locale": locale,
                "min_score": min_score,
                "category": category,
                "sku": sku,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KitListResponse,
                    parse_obj_as(
                        type_=KitListResponse,
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

    async def delete_generated_image(
        self, db_kit_id: int, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteKitImageResponse]:
        """
        Remove a generated image from a catalog kit slot and delete its PNG.

        Parameters
        ----------
        db_kit_id : int

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteKitImageResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(db_kit_id)}/images/{encode_path_param(image_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteKitImageResponse,
                    parse_obj_as(
                        type_=DeleteKitImageResponse,
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

    async def get_kit_meta(
        self, db_kit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KitMetaResponse]:
        """
        Read result sidecars for *db_kit_id*; 404 if the kit root is unknown.

        Parameters
        ----------
        db_kit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KitMetaResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(db_kit_id)}/meta",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KitMetaResponse,
                    parse_obj_as(
                        type_=KitMetaResponse,
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

    async def get_kit_events(
        self, kit_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Stream per-image status events for *kit_id* as text/event-stream.

        Returns 404 when the kit_id has never been published to the bus
        (callers can use this as a "kit not started" signal).  Each line
        conforms to the SSE wire format::

            data: {"image_id": "H1", "status": "color_locked", "progress": 0,
                   "brand_color_locked": true}

        Parameters
        ----------
        kit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def post_generate(
        self,
        kit_id: str,
        *,
        brand_color_hex: str,
        locale: GenerateRequestLocale,
        spec: SpecIn,
        retrieved_bestseller_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        template_scheme_ref: typing.Optional[str] = OMIT,
        template_slot_overrides: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GenerateResponse]:
        """
        Generate the 14-image kit for *kit_id*.

        Parameters
        ----------
        kit_id : str

        brand_color_hex : str

        locale : GenerateRequestLocale

        spec : SpecIn

        retrieved_bestseller_ids : typing.Optional[typing.Sequence[int]]

        style_prompt : typing.Optional[str]

        template_scheme_ref : typing.Optional[str]

        template_slot_overrides : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GenerateResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/generate",
            method="POST",
            json={
                "brand_color_hex": brand_color_hex,
                "locale": locale,
                "retrieved_bestseller_ids": retrieved_bestseller_ids,
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=SpecIn, direction="write"),
                "style_prompt": style_prompt,
                "template_scheme_ref": template_scheme_ref,
                "template_slot_overrides": template_slot_overrides,
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
                    GenerateResponse,
                    parse_obj_as(
                        type_=GenerateResponse,
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

    async def get_generated_image(
        self, kit_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Serve a generated kit image by public kit id and slot id.

        Parameters
        ----------
        kit_id : str

        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/kits/{encode_path_param(kit_id)}/images/{encode_path_param(image_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
