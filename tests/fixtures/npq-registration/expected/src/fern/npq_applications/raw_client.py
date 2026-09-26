

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.application_response import ApplicationResponse
from ..types.applications_response import ApplicationsResponse
from ..types.bad_request_response import BadRequestResponse
from ..types.id_attribute import IdAttribute
from ..types.list_applications_filter import ListApplicationsFilter
from ..types.not_found_response import NotFoundResponse
from ..types.pagination_filter import PaginationFilter
from ..types.sorting_options import SortingOptions
from ..types.unauthorised_response import UnauthorisedResponse
from ..types.unprocessable_entity_response import UnprocessableEntityResponse
from .types.application_accept_request_data import ApplicationAcceptRequestData
from .types.application_change_funded_place_request_data import ApplicationChangeFundedPlaceRequestData
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNpqApplicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_multiple_npq_applications(
        self,
        *,
        filter: typing.Optional[ListApplicationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListApplicationsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationsResponse]
            A list of NPQ applications
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/npq-applications",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListApplicationsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationsResponse,
                    parse_obj_as(
                        type_=ApplicationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    def retrieve_a_single_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationResponse]
            A single NPQ application
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    def accept_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationAcceptRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationAcceptRequestData
            A NPQ application acceptance request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationResponse]
            The NPQ application being accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/accept",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ApplicationAcceptRequestData, direction="write"
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
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    def reject_an_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationResponse]
            The NPQ application being rejected
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/reject",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    def change_funded_place_value_of_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationChangeFundedPlaceRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationChangeFundedPlaceRequestData
            A NPQ application change funded place request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationResponse]
            The NPQ application after changing the funded place
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/change-funded-place",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ApplicationChangeFundedPlaceRequestData, direction="write"
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
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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


class AsyncRawNpqApplicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_multiple_npq_applications(
        self,
        *,
        filter: typing.Optional[ListApplicationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListApplicationsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationsResponse]
            A list of NPQ applications
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/npq-applications",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListApplicationsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationsResponse,
                    parse_obj_as(
                        type_=ApplicationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    async def retrieve_a_single_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationResponse]
            A single NPQ application
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    async def accept_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationAcceptRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationAcceptRequestData
            A NPQ application acceptance request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationResponse]
            The NPQ application being accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/accept",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ApplicationAcceptRequestData, direction="write"
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
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    async def reject_an_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationResponse]
            The NPQ application being rejected
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/reject",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    async def change_funded_place_value_of_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationChangeFundedPlaceRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationChangeFundedPlaceRequestData
            A NPQ application change funded place request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationResponse]
            The NPQ application after changing the funded place
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/npq-applications/{encode_path_param(id)}/change-funded-place",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ApplicationChangeFundedPlaceRequestData, direction="write"
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
                    ApplicationResponse,
                    parse_obj_as(
                        type_=ApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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
