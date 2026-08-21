

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unavailable_for_legal_reasons_error import UnavailableForLegalReasonsError
from ..types.context_uuid import ContextUuid
from ..types.deletion_ready_response import DeletionReadyResponse
from ..types.deletion_request_grounds import DeletionRequestGrounds
from ..types.deletion_request_response import DeletionRequestResponse
from ..types.deletion_request_uuid import DeletionRequestUuid
from ..types.supplied_auth import SuppliedAuth
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeletionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        request_grounds: typing.Optional[DeletionRequestGrounds] = OMIT,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeletionRequestResponse]:
        """
        Create a deletion request to delete all personal data stored within a particular personal data context. This will only schedule a deletion. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to delete.

        request_grounds : typing.Optional[DeletionRequestGrounds]

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletionRequestResponse]
            Deletion request queued
        """
        _response = self._client_wrapper.httpx_client.request(
            f"deletionrequests/{encode_path_param(context_uuid)}",
            method="POST",
            json={
                "request_grounds": request_grounds,
                "authenticated_identifiers": convert_and_respect_annotation_metadata(
                    object_=authenticated_identifiers, annotation=SuppliedAuth, direction="write"
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
                    DeletionRequestResponse,
                    parse_obj_as(
                        type_=DeletionRequestResponse,
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

    def query_the_status_of_a_deletion_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        deletion_request_id: typing.Optional[DeletionRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeletionReadyResponse]:
        """
        Query the status of a deletion request. The status should be polled for until completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages

        deletion_request_id : typing.Optional[DeletionRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletionReadyResponse]
            Deletion request processed
        """
        _response = self._client_wrapper.httpx_client.request(
            "deletionrequeststatus",
            method="POST",
            json={
                "deletion_request_id": deletion_request_id,
            },
            headers={
                "content-type": "application/json",
                "Accept-Language": str(accept_language) if accept_language is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletionReadyResponse,
                    parse_obj_as(
                        type_=DeletionReadyResponse,
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
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


class AsyncRawDeletionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        request_grounds: typing.Optional[DeletionRequestGrounds] = OMIT,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeletionRequestResponse]:
        """
        Create a deletion request to delete all personal data stored within a particular personal data context. This will only schedule a deletion. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to delete.

        request_grounds : typing.Optional[DeletionRequestGrounds]

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletionRequestResponse]
            Deletion request queued
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"deletionrequests/{encode_path_param(context_uuid)}",
            method="POST",
            json={
                "request_grounds": request_grounds,
                "authenticated_identifiers": convert_and_respect_annotation_metadata(
                    object_=authenticated_identifiers, annotation=SuppliedAuth, direction="write"
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
                    DeletionRequestResponse,
                    parse_obj_as(
                        type_=DeletionRequestResponse,
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

    async def query_the_status_of_a_deletion_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        deletion_request_id: typing.Optional[DeletionRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeletionReadyResponse]:
        """
        Query the status of a deletion request. The status should be polled for until completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages

        deletion_request_id : typing.Optional[DeletionRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletionReadyResponse]
            Deletion request processed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "deletionrequeststatus",
            method="POST",
            json={
                "deletion_request_id": deletion_request_id,
            },
            headers={
                "content-type": "application/json",
                "Accept-Language": str(accept_language) if accept_language is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletionReadyResponse,
                    parse_obj_as(
                        type_=DeletionReadyResponse,
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
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
