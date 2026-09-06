

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.get_links_tweetbot_request_url_only import GetLinksTweetbotRequestUrlOnly
from .types.delete_links_delete_bulk_response import DeleteLinksDeleteBulkResponse
from .types.delete_links_link_id_response import DeleteLinksLinkIdResponse
from .types.delete_links_permissions_domain_id_link_id_user_id_response import (
    DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
)
from .types.get_links_permissions_domain_id_link_id_response_item import GetLinksPermissionsDomainIdLinkIdResponseItem
from .types.post_links_archive_bulk_response import PostLinksArchiveBulkResponse
from .types.post_links_archive_response import PostLinksArchiveResponse
from .types.post_links_bulk_request_links_item import PostLinksBulkRequestLinksItem
from .types.post_links_duplicate_link_id_response import PostLinksDuplicateLinkIdResponse
from .types.post_links_examples_response import PostLinksExamplesResponse
from .types.post_links_link_id_request_created_at import PostLinksLinkIdRequestCreatedAt
from .types.post_links_link_id_request_expires_at import PostLinksLinkIdRequestExpiresAt
from .types.post_links_link_id_request_split_urlv2item import PostLinksLinkIdRequestSplitUrlv2Item
from .types.post_links_link_id_request_ttl import PostLinksLinkIdRequestTtl
from .types.post_links_link_id_response import PostLinksLinkIdResponse
from .types.post_links_permissions_domain_id_link_id_user_id_response import (
    PostLinksPermissionsDomainIdLinkIdUserIdResponse,
)
from .types.post_links_public_request_created_at import PostLinksPublicRequestCreatedAt
from .types.post_links_public_request_expires_at import PostLinksPublicRequestExpiresAt
from .types.post_links_public_request_split_urlv2item import PostLinksPublicRequestSplitUrlv2Item
from .types.post_links_public_request_ttl import PostLinksPublicRequestTtl
from .types.post_links_public_response import PostLinksPublicResponse
from .types.post_links_qr_bulk_request_type import PostLinksQrBulkRequestType
from .types.post_links_qr_link_id_string_request_type import PostLinksQrLinkIdStringRequestType
from .types.post_links_request_created_at import PostLinksRequestCreatedAt
from .types.post_links_request_expires_at import PostLinksRequestExpiresAt
from .types.post_links_request_split_urlv2item import PostLinksRequestSplitUrlv2Item
from .types.post_links_request_ttl import PostLinksRequestTtl
from .types.post_links_response import PostLinksResponse
from .types.post_links_unarchive_bulk_response import PostLinksUnarchiveBulkResponse
from .types.post_links_unarchive_response import PostLinksUnarchiveResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLinkManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_link_opengraph_properties(
        self,
        domain_id: float,
        link_id: str,
        *,
        request: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request : typing.Sequence[typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/opengraph/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def get_link_permissions(
        self, domain_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def add_link_permission(
        self, domain_id: str, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostLinksPermissionsDomainIdLinkIdUserIdResponse]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str
            Link ID

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksPermissionsDomainIdLinkIdUserIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostLinksPermissionsDomainIdLinkIdUserIdResponse,
                    parse_obj_as(
                        type_=PostLinksPermissionsDomainIdLinkIdUserIdResponse,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def delete_link_permissions(
        self, domain_id: int, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteLinksPermissionsDomainIdLinkIdUserIdResponse]:
        """
        Parameters
        ----------
        domain_id : int

        link_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteLinksPermissionsDomainIdLinkIdUserIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
                    parse_obj_as(
                        type_=DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def generate_qr_code_for_the_link(
        self,
        link_id_string: str,
        *,
        use_domain_settings: bool,
        accept: typing.Optional[str] = None,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        type: typing.Optional[PostLinksQrLinkIdStringRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        link_id_string : str
            Link ID

        use_domain_settings : bool

        accept : typing.Optional[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        type : typing.Optional[PostLinksQrLinkIdStringRequestType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/qr/{encode_path_param(link_id_string)}",
            method="POST",
            json={
                "color": color,
                "backgroundColor": background_color,
                "size": size,
                "type": type,
                "useDomainSettings": use_domain_settings,
            },
            headers={
                "content-type": "application/json",
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
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

    def generate_qr_codes_for_the_link_in_bulk(
        self,
        *,
        type: PostLinksQrBulkRequestType,
        use_domain_settings: bool,
        link_ids: typing.Sequence[str],
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Generate QR codes for the link in bulk. Rate limit - 1 request per minute

        Parameters
        ----------
        type : PostLinksQrBulkRequestType

        use_domain_settings : bool

        link_ids : typing.Sequence[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        no_excavate : typing.Optional[bool]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            ZIP file containing QR codes
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/qr/bulk",
            method="POST",
            json={
                "color": color,
                "backgroundColor": background_color,
                "size": size,
                "type": type,
                "useDomainSettings": use_domain_settings,
                "noExcavate": no_excavate,
                "linkIds": link_ids,
                "domainId": domain_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_link(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteLinksLinkIdResponse]:
        """
        Delete link by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str
            Link ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteLinksLinkIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLinksLinkIdResponse,
                    parse_obj_as(
                        type_=DeleteLinksLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_links_in_bulk(
        self, *, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteLinksDeleteBulkResponse]:
        """
        Delete links in bulk by ids

        **Rate limit**: 1/s

        Parameters
        ----------
        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteLinksDeleteBulkResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/delete_bulk",
            method="DELETE",
            json={
                "link_ids": link_ids,
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
                    DeleteLinksDeleteBulkResponse,
                    parse_obj_as(
                        type_=DeleteLinksDeleteBulkResponse,
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

    def archive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksArchiveResponse]:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksArchiveResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/archive",
            method="POST",
            json={
                "link_id": link_id,
                "domain_id": domain_id,
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
                    PostLinksArchiveResponse,
                    parse_obj_as(
                        type_=PostLinksArchiveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def archive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksArchiveBulkResponse]:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksArchiveBulkResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/archive_bulk",
            method="POST",
            json={
                "link_ids": link_ids,
                "domain_id": domain_id,
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
                    PostLinksArchiveBulkResponse,
                    parse_obj_as(
                        type_=PostLinksArchiveBulkResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def unarchive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksUnarchiveResponse]:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksUnarchiveResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/unarchive",
            method="POST",
            json={
                "link_id": link_id,
                "domain_id": domain_id,
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
                    PostLinksUnarchiveResponse,
                    parse_obj_as(
                        type_=PostLinksUnarchiveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def unarchive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksUnarchiveBulkResponse]:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksUnarchiveBulkResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/unarchive_bulk",
            method="POST",
            json={
                "link_ids": link_ids,
                "domain_id": domain_id,
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
                    PostLinksUnarchiveBulkResponse,
                    parse_obj_as(
                        type_=PostLinksUnarchiveBulkResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update_existing_url(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksLinkIdRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksLinkIdRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksLinkIdRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        original_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksLinkIdResponse]:
        """
        Update original url, title or path for existing URL by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksLinkIdRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksLinkIdRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksLinkIdRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        original_url : typing.Optional[str]
            Original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksLinkIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="POST",
            params={
                "domain_id": domain_id,
            },
            json={
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksLinkIdRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksLinkIdRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksLinkIdRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "originalURL": original_url,
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
                    PostLinksLinkIdResponse,
                    parse_obj_as(
                        type_=PostLinksLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create_a_new_link(
        self,
        *,
        original_url: str,
        domain: str,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        post_links_request_skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksResponse]:
        """
        This method creates a new link. If parameter "path" is omitted, it
        generates path by algorithm, chosen in domain settings.

        Notes:

        1. If URL with a given path already exists and originalURL of the URL in database is equal to originalURL argument, it returns information about existing URL
        2. If URL with a given path already exists and originalURL is different from originalURL in database, it returns error with a status `409`
        3. If URL with a given originalURL exists, and no path is given, it returns information about existing URL and does not create anything
        4. If URL with a given originalURL exists, and custom path is given, it creates a new short URL

        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str
            Domain hostname

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        post_links_request_skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        allow_duplicates : typing.Optional[bool]
            Allow duplicates

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links",
            method="POST",
            json={
                "originalURL": original_url,
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": post_links_request_skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "domain": domain,
                "allowDuplicates": allow_duplicates,
                "folderId": folder_id,
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
                    PostLinksResponse,
                    parse_obj_as(
                        type_=PostLinksResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create_a_new_link_simple_version(
        self,
        *,
        domain: str,
        original_url: str,
        api_key: str,
        path: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        url_only: typing.Optional[GetLinksTweetbotRequestUrlOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """

                            Simple version of link create endpoint. You can use it if you can not use POST method
                            **Rate limit**: 50/s


        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        api_key : str
            API key

        path : typing.Optional[str]
            Link path

        title : typing.Optional[str]
            Link title

        url_only : typing.Optional[GetLinksTweetbotRequestUrlOnly]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/tweetbot",
            method="GET",
            params={
                "domain": domain,
                "path": path,
                "originalURL": original_url,
                "title": title,
                "urlOnly": url_only,
                "apiKey": api_key,
            },
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

    def create_a_new_link_using_public_api_key(
        self,
        *,
        original_url: str,
        domain: str,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksPublicRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksPublicRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksPublicRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksPublicResponse]:
        """
        This method creates a new link. Only this method should be used in client-side applications

        If parameter "path" is omitted, it generates path by algorithm, chosen in domain settings.

        You can use it with public API key in your frontend applications (client-side javascript, Android & iPhone apps)
        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksPublicRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksPublicRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksPublicRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksPublicResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/public",
            method="POST",
            json={
                "originalURL": original_url,
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksPublicRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksPublicRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksPublicRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "domain": domain,
                "folderId": folder_id,
            },
            headers={
                "content-type": "application/json",
                "type": str(type) if type is not None else None,
                "additionalProperties": str(additional_properties) if additional_properties is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostLinksPublicResponse,
                    parse_obj_as(
                        type_=PostLinksPublicResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create_up_to1000links_in_one_call(
        self,
        *,
        domain: str,
        links: typing.Sequence[PostLinksBulkRequestLinksItem],
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Please use this method if you need to create big packs of links. It
        accepts up to 1000 links in one API call.

        It works almost the same as single link creation endpoint, but accepts
        an array of URLs and returns an array of responses.

        Returns list of Link objects. If any URL is failed to insert, it returns
        error object instead as array element. Method is not transactional – it
        can insert some links from the list and return an error for others.

        **Rate limit**: 5 queries in 10 seconds

        Parameters
        ----------
        domain : str

        links : typing.Sequence[PostLinksBulkRequestLinksItem]

        allow_duplicates : typing.Optional[bool]

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/bulk",
            method="POST",
            json={
                "domain": domain,
                "allowDuplicates": allow_duplicates,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[PostLinksBulkRequestLinksItem], direction="write"
                ),
                "folderId": folder_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def generate_example_links_for_a_domain(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostLinksExamplesResponse]:
        """
        Creates a set of demo/example links to showcase various features of the short link service.

        Example links include:
        - A/B testing with split URLs
        - Mobile targeting (different URLs for Android/iPhone)
        - Expiring links with time limits
        - File download links
        - Password-protected links

        **Rate limit**: 5/10s

        Parameters
        ----------
        domain : str
            Domain hostname to create examples for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksExamplesResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/examples",
            method="POST",
            json={
                "domain": domain,
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
                    PostLinksExamplesResponse,
                    parse_obj_as(
                        type_=PostLinksExamplesResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def duplicate_an_existing_link(
        self,
        link_id: str,
        *,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLinksDuplicateLinkIdResponse]:
        """
        Duplicates an existing link with all its properties, targeting rules, and settings.
        The duplicated link will have a new random path (or custom if provided) and be fully independent.

        **Rate limit**: 50/s

        Parameters
        ----------
        link_id : str

        path : typing.Optional[str]
            Custom path for duplicated link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksDuplicateLinkIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/duplicate/{encode_path_param(link_id)}",
            method="POST",
            json={
                "path": path,
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
                    PostLinksDuplicateLinkIdResponse,
                    parse_obj_as(
                        type_=PostLinksDuplicateLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def append_a_single_tag_to_the_links_in_bulk(
        self, *, tag: str, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tag : str

        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tags/bulk",
            method="POST",
            json={
                "tag": tag,
                "link_ids": link_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncRawLinkManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_link_opengraph_properties(
        self,
        domain_id: float,
        link_id: str,
        *,
        request: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request : typing.Sequence[typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/opengraph/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def get_link_permissions(
        self, domain_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def add_link_permission(
        self, domain_id: str, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostLinksPermissionsDomainIdLinkIdUserIdResponse]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str
            Link ID

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksPermissionsDomainIdLinkIdUserIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostLinksPermissionsDomainIdLinkIdUserIdResponse,
                    parse_obj_as(
                        type_=PostLinksPermissionsDomainIdLinkIdUserIdResponse,
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def delete_link_permissions(
        self, domain_id: int, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteLinksPermissionsDomainIdLinkIdUserIdResponse]:
        """
        Parameters
        ----------
        domain_id : int

        link_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteLinksPermissionsDomainIdLinkIdUserIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/permissions/{encode_path_param(domain_id)}/{encode_path_param(link_id)}/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
                    parse_obj_as(
                        type_=DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def generate_qr_code_for_the_link(
        self,
        link_id_string: str,
        *,
        use_domain_settings: bool,
        accept: typing.Optional[str] = None,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        type: typing.Optional[PostLinksQrLinkIdStringRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        link_id_string : str
            Link ID

        use_domain_settings : bool

        accept : typing.Optional[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        type : typing.Optional[PostLinksQrLinkIdStringRequestType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/qr/{encode_path_param(link_id_string)}",
            method="POST",
            json={
                "color": color,
                "backgroundColor": background_color,
                "size": size,
                "type": type,
                "useDomainSettings": use_domain_settings,
            },
            headers={
                "content-type": "application/json",
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
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

    async def generate_qr_codes_for_the_link_in_bulk(
        self,
        *,
        type: PostLinksQrBulkRequestType,
        use_domain_settings: bool,
        link_ids: typing.Sequence[str],
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Generate QR codes for the link in bulk. Rate limit - 1 request per minute

        Parameters
        ----------
        type : PostLinksQrBulkRequestType

        use_domain_settings : bool

        link_ids : typing.Sequence[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        no_excavate : typing.Optional[bool]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            ZIP file containing QR codes
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/qr/bulk",
            method="POST",
            json={
                "color": color,
                "backgroundColor": background_color,
                "size": size,
                "type": type,
                "useDomainSettings": use_domain_settings,
                "noExcavate": no_excavate,
                "linkIds": link_ids,
                "domainId": domain_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_link(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteLinksLinkIdResponse]:
        """
        Delete link by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str
            Link ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteLinksLinkIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLinksLinkIdResponse,
                    parse_obj_as(
                        type_=DeleteLinksLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_links_in_bulk(
        self, *, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteLinksDeleteBulkResponse]:
        """
        Delete links in bulk by ids

        **Rate limit**: 1/s

        Parameters
        ----------
        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteLinksDeleteBulkResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/delete_bulk",
            method="DELETE",
            json={
                "link_ids": link_ids,
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
                    DeleteLinksDeleteBulkResponse,
                    parse_obj_as(
                        type_=DeleteLinksDeleteBulkResponse,
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

    async def archive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksArchiveResponse]:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksArchiveResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/archive",
            method="POST",
            json={
                "link_id": link_id,
                "domain_id": domain_id,
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
                    PostLinksArchiveResponse,
                    parse_obj_as(
                        type_=PostLinksArchiveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def archive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksArchiveBulkResponse]:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksArchiveBulkResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/archive_bulk",
            method="POST",
            json={
                "link_ids": link_ids,
                "domain_id": domain_id,
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
                    PostLinksArchiveBulkResponse,
                    parse_obj_as(
                        type_=PostLinksArchiveBulkResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def unarchive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksUnarchiveResponse]:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksUnarchiveResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/unarchive",
            method="POST",
            json={
                "link_id": link_id,
                "domain_id": domain_id,
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
                    PostLinksUnarchiveResponse,
                    parse_obj_as(
                        type_=PostLinksUnarchiveResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def unarchive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksUnarchiveBulkResponse]:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksUnarchiveBulkResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/unarchive_bulk",
            method="POST",
            json={
                "link_ids": link_ids,
                "domain_id": domain_id,
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
                    PostLinksUnarchiveBulkResponse,
                    parse_obj_as(
                        type_=PostLinksUnarchiveBulkResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update_existing_url(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksLinkIdRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksLinkIdRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksLinkIdRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        original_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksLinkIdResponse]:
        """
        Update original url, title or path for existing URL by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksLinkIdRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksLinkIdRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksLinkIdRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        original_url : typing.Optional[str]
            Original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksLinkIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="POST",
            params={
                "domain_id": domain_id,
            },
            json={
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksLinkIdRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksLinkIdRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksLinkIdRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "originalURL": original_url,
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
                    PostLinksLinkIdResponse,
                    parse_obj_as(
                        type_=PostLinksLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create_a_new_link(
        self,
        *,
        original_url: str,
        domain: str,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        post_links_request_skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksResponse]:
        """
        This method creates a new link. If parameter "path" is omitted, it
        generates path by algorithm, chosen in domain settings.

        Notes:

        1. If URL with a given path already exists and originalURL of the URL in database is equal to originalURL argument, it returns information about existing URL
        2. If URL with a given path already exists and originalURL is different from originalURL in database, it returns error with a status `409`
        3. If URL with a given originalURL exists, and no path is given, it returns information about existing URL and does not create anything
        4. If URL with a given originalURL exists, and custom path is given, it creates a new short URL

        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str
            Domain hostname

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        post_links_request_skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        allow_duplicates : typing.Optional[bool]
            Allow duplicates

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links",
            method="POST",
            json={
                "originalURL": original_url,
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": post_links_request_skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "domain": domain,
                "allowDuplicates": allow_duplicates,
                "folderId": folder_id,
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
                    PostLinksResponse,
                    parse_obj_as(
                        type_=PostLinksResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create_a_new_link_simple_version(
        self,
        *,
        domain: str,
        original_url: str,
        api_key: str,
        path: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        url_only: typing.Optional[GetLinksTweetbotRequestUrlOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """

                            Simple version of link create endpoint. You can use it if you can not use POST method
                            **Rate limit**: 50/s


        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        api_key : str
            API key

        path : typing.Optional[str]
            Link path

        title : typing.Optional[str]
            Link title

        url_only : typing.Optional[GetLinksTweetbotRequestUrlOnly]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/tweetbot",
            method="GET",
            params={
                "domain": domain,
                "path": path,
                "originalURL": original_url,
                "title": title,
                "urlOnly": url_only,
                "apiKey": api_key,
            },
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

    async def create_a_new_link_using_public_api_key(
        self,
        *,
        original_url: str,
        domain: str,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksPublicRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksPublicRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksPublicRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksPublicResponse]:
        """
        This method creates a new link. Only this method should be used in client-side applications

        If parameter "path" is omitted, it generates path by algorithm, chosen in domain settings.

        You can use it with public API key in your frontend applications (client-side javascript, Android & iPhone apps)
        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksPublicRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksPublicRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksPublicRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksPublicResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/public",
            method="POST",
            json={
                "originalURL": original_url,
                "cloaking": cloaking,
                "password": password,
                "redirectType": redirect_type,
                "expiresAt": convert_and_respect_annotation_metadata(
                    object_=expires_at, annotation=PostLinksPublicRequestExpiresAt, direction="write"
                ),
                "expiredURL": expired_url,
                "title": title,
                "tags": tags,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=PostLinksPublicRequestTtl, direction="write"
                ),
                "path": path,
                "androidURL": android_url,
                "iphoneURL": iphone_url,
                "createdAt": convert_and_respect_annotation_metadata(
                    object_=created_at, annotation=PostLinksPublicRequestCreatedAt, direction="write"
                ),
                "clicksLimit": clicks_limit,
                "passwordContact": password_contact,
                "skipQS": skip_qs,
                "archived": archived,
                "splitURL": split_url,
                "splitPercent": split_percent,
                "splitURLV2": convert_and_respect_annotation_metadata(
                    object_=split_urlv2,
                    annotation=typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]],
                    direction="write",
                ),
                "integrationAdroll": integration_adroll,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "domain": domain,
                "folderId": folder_id,
            },
            headers={
                "content-type": "application/json",
                "type": str(type) if type is not None else None,
                "additionalProperties": str(additional_properties) if additional_properties is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostLinksPublicResponse,
                    parse_obj_as(
                        type_=PostLinksPublicResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create_up_to1000links_in_one_call(
        self,
        *,
        domain: str,
        links: typing.Sequence[PostLinksBulkRequestLinksItem],
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Please use this method if you need to create big packs of links. It
        accepts up to 1000 links in one API call.

        It works almost the same as single link creation endpoint, but accepts
        an array of URLs and returns an array of responses.

        Returns list of Link objects. If any URL is failed to insert, it returns
        error object instead as array element. Method is not transactional – it
        can insert some links from the list and return an error for others.

        **Rate limit**: 5 queries in 10 seconds

        Parameters
        ----------
        domain : str

        links : typing.Sequence[PostLinksBulkRequestLinksItem]

        allow_duplicates : typing.Optional[bool]

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/bulk",
            method="POST",
            json={
                "domain": domain,
                "allowDuplicates": allow_duplicates,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[PostLinksBulkRequestLinksItem], direction="write"
                ),
                "folderId": folder_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def generate_example_links_for_a_domain(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostLinksExamplesResponse]:
        """
        Creates a set of demo/example links to showcase various features of the short link service.

        Example links include:
        - A/B testing with split URLs
        - Mobile targeting (different URLs for Android/iPhone)
        - Expiring links with time limits
        - File download links
        - Password-protected links

        **Rate limit**: 5/10s

        Parameters
        ----------
        domain : str
            Domain hostname to create examples for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksExamplesResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/examples",
            method="POST",
            json={
                "domain": domain,
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
                    PostLinksExamplesResponse,
                    parse_obj_as(
                        type_=PostLinksExamplesResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def duplicate_an_existing_link(
        self,
        link_id: str,
        *,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLinksDuplicateLinkIdResponse]:
        """
        Duplicates an existing link with all its properties, targeting rules, and settings.
        The duplicated link will have a new random path (or custom if provided) and be fully independent.

        **Rate limit**: 50/s

        Parameters
        ----------
        link_id : str

        path : typing.Optional[str]
            Custom path for duplicated link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksDuplicateLinkIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/duplicate/{encode_path_param(link_id)}",
            method="POST",
            json={
                "path": path,
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
                    PostLinksDuplicateLinkIdResponse,
                    parse_obj_as(
                        type_=PostLinksDuplicateLinkIdResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def append_a_single_tag_to_the_links_in_bulk(
        self, *, tag: str, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tag : str

        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tags/bulk",
            method="POST",
            json={
                "tag": tag,
                "link_ids": link_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
