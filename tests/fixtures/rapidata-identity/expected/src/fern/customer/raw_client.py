

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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.get_customers_request_email import GetCustomersRequestEmail
from ..types.get_customers_request_id import GetCustomersRequestId
from ..types.get_customers_request_organization_id import GetCustomersRequestOrganizationId
from ..types.get_customers_request_organization_name import GetCustomersRequestOrganizationName
from ..types.query_customers_endpoint_paged_result_of_output import QueryCustomersEndpointPagedResultOfOutput
from ..types.validation_problem_details import ValidationProblemDetails
from .types.get_customers_request_logic import GetCustomersRequestLogic
from .types.get_customers_request_sort_item import GetCustomersRequestSortItem
from pydantic import ValidationError


class RawCustomerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        This cannot be undone. An organization the account is the only member of is deleted with it,
         along with everything it owns; invoices already raised are kept. Responds with 409 when the
         account is the last owner of an organization that has other members — transfer ownership
         first — or when such an organization still has an open invoice or a billing reconciliation in
         progress. Issuing it again for an account that is already deleted succeeds and changes
         nothing further. The same address and the same external login can be used to register a new
         account afterwards; none of the old account's data comes back with it.

        Parameters
        ----------
        customer_id : str
            The id of the customer to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def queries_customers_with_filtering_and_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]
        ] = None,
        id: typing.Optional[GetCustomersRequestId] = None,
        email: typing.Optional[GetCustomersRequestEmail] = None,
        organization_name: typing.Optional[GetCustomersRequestOrganizationName] = None,
        organization_id: typing.Optional[GetCustomersRequestOrganizationId] = None,
        logic: typing.Optional[GetCustomersRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryCustomersEndpointPagedResultOfOutput]:
        """
        Results are scoped to customers that belong to the caller's organization.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetCustomersRequestId]
            Filter by id.

        email : typing.Optional[GetCustomersRequestEmail]
            Filter by email.

        organization_name : typing.Optional[GetCustomersRequestOrganizationName]
            Filter by organization_name.

        organization_id : typing.Optional[GetCustomersRequestOrganizationId]
            Filter by organization_id.

        logic : typing.Optional[GetCustomersRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryCustomersEndpointPagedResultOfOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "customers",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "sort": sort,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=GetCustomersRequestId, direction="write"
                ),
                "email": convert_and_respect_annotation_metadata(
                    object_=email, annotation=GetCustomersRequestEmail, direction="write"
                ),
                "organization_name": convert_and_respect_annotation_metadata(
                    object_=organization_name, annotation=GetCustomersRequestOrganizationName, direction="write"
                ),
                "organization_id": convert_and_respect_annotation_metadata(
                    object_=organization_id, annotation=GetCustomersRequestOrganizationId, direction="write"
                ),
                "logic": logic,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryCustomersEndpointPagedResultOfOutput,
                    parse_obj_as(
                        type_=QueryCustomersEndpointPagedResultOfOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCustomerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        This cannot be undone. An organization the account is the only member of is deleted with it,
         along with everything it owns; invoices already raised are kept. Responds with 409 when the
         account is the last owner of an organization that has other members — transfer ownership
         first — or when such an organization still has an open invoice or a billing reconciliation in
         progress. Issuing it again for an account that is already deleted succeeds and changes
         nothing further. The same address and the same external login can be used to register a new
         account afterwards; none of the old account's data comes back with it.

        Parameters
        ----------
        customer_id : str
            The id of the customer to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def queries_customers_with_filtering_and_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]
        ] = None,
        id: typing.Optional[GetCustomersRequestId] = None,
        email: typing.Optional[GetCustomersRequestEmail] = None,
        organization_name: typing.Optional[GetCustomersRequestOrganizationName] = None,
        organization_id: typing.Optional[GetCustomersRequestOrganizationId] = None,
        logic: typing.Optional[GetCustomersRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryCustomersEndpointPagedResultOfOutput]:
        """
        Results are scoped to customers that belong to the caller's organization.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetCustomersRequestId]
            Filter by id.

        email : typing.Optional[GetCustomersRequestEmail]
            Filter by email.

        organization_name : typing.Optional[GetCustomersRequestOrganizationName]
            Filter by organization_name.

        organization_id : typing.Optional[GetCustomersRequestOrganizationId]
            Filter by organization_id.

        logic : typing.Optional[GetCustomersRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryCustomersEndpointPagedResultOfOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customers",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "sort": sort,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=GetCustomersRequestId, direction="write"
                ),
                "email": convert_and_respect_annotation_metadata(
                    object_=email, annotation=GetCustomersRequestEmail, direction="write"
                ),
                "organization_name": convert_and_respect_annotation_metadata(
                    object_=organization_name, annotation=GetCustomersRequestOrganizationName, direction="write"
                ),
                "organization_id": convert_and_respect_annotation_metadata(
                    object_=organization_id, annotation=GetCustomersRequestOrganizationId, direction="write"
                ),
                "logic": logic,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryCustomersEndpointPagedResultOfOutput,
                    parse_obj_as(
                        type_=QueryCustomersEndpointPagedResultOfOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
