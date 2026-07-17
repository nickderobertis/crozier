

import datetime as dt
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
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.assignee import Assignee
from ..types.bad_request_response import BadRequestResponse
from ..types.collection_tag import CollectionTag
from ..types.create_ticket_response import CreateTicketResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_ticket_response import DeleteTicketResponse
from ..types.get_ticket_response import GetTicketResponse
from ..types.get_tickets_response import GetTicketsResponse
from ..types.id import Id
from ..types.issues_filter import IssuesFilter
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.ticket_priority import TicketPriority
from ..types.tickets_sort import TicketsSort
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_ticket_response import UpdateTicketResponse
from ..types.updated_at import UpdatedAt
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTicketsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def collection_tickets_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[TicketsSort] = None,
        filter: typing.Optional[IssuesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTicketsResponse]:
        """
        List Tickets

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[TicketsSort]
            Apply sorting

        filter : typing.Optional[IssuesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTicketsResponse]
            List Tickets
        """
        _response = self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=TicketsSort, direction="write"
                ),
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=IssuesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTicketsResponse,
                    parse_obj_as(
                        type_=GetTicketsResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def collection_tickets_add(
        self,
        collection_id_: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTicketResponse]:
        """
        Create Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTicketResponse]
            Create a Ticket
        """
        _response = self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id_)}/tickets",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "assignees": convert_and_respect_annotation_metadata(
                    object_=assignees, annotation=typing.Sequence[Assignee], direction="write"
                ),
                "collection_id": collection_id,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "due_date": due_date,
                "id": id,
                "parent_id": parent_id,
                "priority": priority,
                "status": status,
                "subject": subject,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CollectionTag], direction="write"
                ),
                "type": type,
                "updated_at": updated_at,
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
                    CreateTicketResponse,
                    parse_obj_as(
                        type_=CreateTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def collection_tickets_one(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTicketResponse]:
        """
        Get Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTicketResponse]
            Get a Ticket
        """
        _response = self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets/{encode_path_param(ticket_id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTicketResponse,
                    parse_obj_as(
                        type_=GetTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def collection_tickets_delete(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteTicketResponse]:
        """
        Delete Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteTicketResponse]
            Delete a Ticket
        """
        _response = self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets/{encode_path_param(ticket_id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTicketResponse,
                    parse_obj_as(
                        type_=DeleteTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def collection_tickets_update(
        self,
        collection_id_: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateTicketResponse]:
        """
        Update Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateTicketResponse]
            Update a Ticket
        """
        _response = self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id_)}/tickets/{encode_path_param(ticket_id)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "assignees": convert_and_respect_annotation_metadata(
                    object_=assignees, annotation=typing.Sequence[Assignee], direction="write"
                ),
                "collection_id": collection_id,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "due_date": due_date,
                "id": id,
                "parent_id": parent_id,
                "priority": priority,
                "status": status,
                "subject": subject,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CollectionTag], direction="write"
                ),
                "type": type,
                "updated_at": updated_at,
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
                    UpdateTicketResponse,
                    parse_obj_as(
                        type_=UpdateTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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


class AsyncRawTicketsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def collection_tickets_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[TicketsSort] = None,
        filter: typing.Optional[IssuesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetTicketsResponse]:
        """
        List Tickets

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[TicketsSort]
            Apply sorting

        filter : typing.Optional[IssuesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTicketsResponse]
            List Tickets
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=TicketsSort, direction="write"
                ),
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=IssuesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTicketsResponse,
                    parse_obj_as(
                        type_=GetTicketsResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def collection_tickets_add(
        self,
        collection_id_: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTicketResponse]:
        """
        Create Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTicketResponse]
            Create a Ticket
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id_)}/tickets",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "assignees": convert_and_respect_annotation_metadata(
                    object_=assignees, annotation=typing.Sequence[Assignee], direction="write"
                ),
                "collection_id": collection_id,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "due_date": due_date,
                "id": id,
                "parent_id": parent_id,
                "priority": priority,
                "status": status,
                "subject": subject,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CollectionTag], direction="write"
                ),
                "type": type,
                "updated_at": updated_at,
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
                    CreateTicketResponse,
                    parse_obj_as(
                        type_=CreateTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def collection_tickets_one(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetTicketResponse]:
        """
        Get Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTicketResponse]
            Get a Ticket
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets/{encode_path_param(ticket_id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTicketResponse,
                    parse_obj_as(
                        type_=GetTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def collection_tickets_delete(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteTicketResponse]:
        """
        Delete Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteTicketResponse]
            Delete a Ticket
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id)}/tickets/{encode_path_param(ticket_id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTicketResponse,
                    parse_obj_as(
                        type_=DeleteTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def collection_tickets_update(
        self,
        collection_id_: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateTicketResponse]:
        """
        Update Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateTicketResponse]
            Update a Ticket
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"issue-tracking/collections/{encode_path_param(collection_id_)}/tickets/{encode_path_param(ticket_id)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "assignees": convert_and_respect_annotation_metadata(
                    object_=assignees, annotation=typing.Sequence[Assignee], direction="write"
                ),
                "collection_id": collection_id,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "due_date": due_date,
                "id": id,
                "parent_id": parent_id,
                "priority": priority,
                "status": status,
                "subject": subject,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[CollectionTag], direction="write"
                ),
                "type": type,
                "updated_at": updated_at,
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
                    UpdateTicketResponse,
                    parse_obj_as(
                        type_=UpdateTicketResponse,
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
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
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
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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
