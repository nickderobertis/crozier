

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.conflict_error_body import ConflictErrorBody
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.id import Id
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.order import Order
from ..types.rate_limit_error import RateLimitError
from ..types.ro_crate import RoCrate
from ..types.tombstone import Tombstone
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.list_ro_crates_request_sort import ListRoCratesRequestSort
from .types.list_ro_crates_response import ListRoCratesResponse
from pydantic import ValidationError


class RawRoCratesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_ro_crates(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListRoCratesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListRoCratesResponse]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        List RO-Crates, paginated and sorted. The response contains whatever the caller is allowed to see under the implementation's visibility model: implementations choose whether RO-Crates are a public surface (listable by anyone, with per-object `access` governing metadata-document retrieval) or a depositor-only management surface (requiring the `write` scope).

        There are no content filters — catalog-side questions belong to `/entities` and `/search`.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListRoCratesRequestSort]
            Field to sort by.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRoCratesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "ro-crates",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRoCratesResponse,
                    parse_obj_as(
                        type_=ListRoCratesResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def get_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[RoCrate]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve an RO-Crate. The body is deliberately lean: identity, the entities materialised from the current version, timestamps, and access. The deposited metadata document — `GET /ro-crate/{id}/metadata` — is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.

        `entityIds` is the authoritative answer to "what did my deposit create". It is the inverse of the entity's `roCrateIds` and can change when later deposits (of this or other RO-Crates) alter the materialisation.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RoCrate]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RoCrate,
                    parse_obj_as(
                        type_=RoCrate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def delete_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an RO-Crate — its metadata document and files. Deletion is not a deposit session; it is already atomic. Implementations needing slow teardown MAY return `202 Accepted`.

        The spec mandates no preconditions; implementations MAY refuse per their own policy (curatorial holds, cross-references) with `409` and a reason. The effect on materialised entities is implementation-defined, mirroring re-deposit pruning: an entity no other RO-Crate contributes to MAY be removed, and deliberate retention is legitimate. An entity with other contributors survives — the deleted RO-Crate simply drops out of its `roCrateIds`.

        Open deposits do not block deletion: delete wins, and a subsequent finalise of such a deposit fails back to `open` with the failure recorded. Implementations MAY auto-abort open deposits against the deleted RO-Crate.

        After deletion, the RO-Crate's URIs (including `/ro-crate/{id}/metadata`) follow the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def get_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the RO-Crate's current RO-Crate metadata document, verbatim as deposited. Unlike `GET /entity/{id}/metadata`, which may return a derived view, this endpoint always returns the original deposited metadata document.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Returns the deposited RO-Crate JSON-LD metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def head_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposited metadata document's headers without downloading the content. Returns the same headers as GET but with no response body, useful for checking availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}/metadata",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawRoCratesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_ro_crates(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListRoCratesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListRoCratesResponse]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        List RO-Crates, paginated and sorted. The response contains whatever the caller is allowed to see under the implementation's visibility model: implementations choose whether RO-Crates are a public surface (listable by anyone, with per-object `access` governing metadata-document retrieval) or a depositor-only management surface (requiring the `write` scope).

        There are no content filters — catalog-side questions belong to `/entities` and `/search`.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListRoCratesRequestSort]
            Field to sort by.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRoCratesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ro-crates",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRoCratesResponse,
                    parse_obj_as(
                        type_=ListRoCratesResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def get_ro_crate(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RoCrate]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve an RO-Crate. The body is deliberately lean: identity, the entities materialised from the current version, timestamps, and access. The deposited metadata document — `GET /ro-crate/{id}/metadata` — is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.

        `entityIds` is the authoritative answer to "what did my deposit create". It is the inverse of the entity's `roCrateIds` and can change when later deposits (of this or other RO-Crates) alter the materialisation.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RoCrate]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RoCrate,
                    parse_obj_as(
                        type_=RoCrate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def delete_ro_crate(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an RO-Crate — its metadata document and files. Deletion is not a deposit session; it is already atomic. Implementations needing slow teardown MAY return `202 Accepted`.

        The spec mandates no preconditions; implementations MAY refuse per their own policy (curatorial holds, cross-references) with `409` and a reason. The effect on materialised entities is implementation-defined, mirroring re-deposit pruning: an entity no other RO-Crate contributes to MAY be removed, and deliberate retention is legitimate. An entity with other contributors survives — the deleted RO-Crate simply drops out of its `roCrateIds`.

        Open deposits do not block deletion: delete wins, and a subsequent finalise of such a deposit fails back to `open` with the failure recorded. Implementations MAY auto-abort open deposits against the deleted RO-Crate.

        After deletion, the RO-Crate's URIs (including `/ro-crate/{id}/metadata`) follow the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def get_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the RO-Crate's current RO-Crate metadata document, verbatim as deposited. Unlike `GET /entity/{id}/metadata`, which may return a derived view, this endpoint always returns the original deposited metadata document.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Returns the deposited RO-Crate JSON-LD metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def head_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposited metadata document's headers without downloading the content. Returns the same headers as GET but with no response body, useful for checking availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ro-crate/{encode_path_param(id)}/metadata",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Tombstone,
                        parse_obj_as(
                            type_=Tombstone,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
