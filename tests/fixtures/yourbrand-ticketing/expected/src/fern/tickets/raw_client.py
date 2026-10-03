

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.paged_result_of_ticket import PagedResultOfTicket
from ..types.paged_result_of_ticket_comment import PagedResultOfTicketComment
from ..types.paged_result_of_ticket_event import PagedResultOfTicketEvent
from ..types.problem_details import ProblemDetails
from ..types.sort_direction import SortDirection
from ..types.ticket import Ticket
from ..types.ticket_comment import TicketComment
from ..types.ticket_impact import TicketImpact
from ..types.ticket_priority import TicketPriority
from ..types.ticket_urgency import TicketUrgency
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTicketsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def gettickets(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        status: typing.Optional[typing.Sequence[int]] = None,
        assignee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagedResultOfTicket]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        status : typing.Optional[typing.Sequence[int]]

        assignee_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagedResultOfTicket]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Tickets",
            method="GET",
            params={
                "organizationId": organization_id,
                "projectId": project_id,
                "status": status,
                "assigneeId": assignee_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicket,
                    parse_obj_as(
                        type_=PagedResultOfTicket,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def createticket(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        assignee_id: typing.Optional[str] = OMIT,
        estimated_time: typing.Optional[str] = OMIT,
        completed_time: typing.Optional[str] = OMIT,
        remaining_time: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        impact: typing.Optional[TicketImpact] = OMIT,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ticket]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        title : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[int]

        assignee_id : typing.Optional[str]

        estimated_time : typing.Optional[str]

        completed_time : typing.Optional[str]

        remaining_time : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        impact : typing.Optional[TicketImpact]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ticket]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Tickets",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "projectId": project_id,
                "title": title,
                "description": description,
                "status": status,
                "assigneeId": assignee_id,
                "estimatedTime": estimated_time,
                "completedTime": completed_time,
                "remainingTime": remaining_time,
                "priority": priority,
                "impact": impact,
                "urgency": urgency,
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
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
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

    def getticketevents(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagedResultOfTicketEvent]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagedResultOfTicketEvent]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/events",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicketEvent,
                    parse_obj_as(
                        type_=PagedResultOfTicketEvent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def getticketbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ticket]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ticket]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def deleteticket(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
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

    def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/project",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "projectId": project_id,
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

    def updatepriority(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        priority: typing.Optional[TicketPriority] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/priority",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "priority": priority,
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

    def updateurgency(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/urgency",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "urgency": urgency,
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

    def updateimpact(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        impact: typing.Optional[TicketImpact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        impact : typing.Optional[TicketImpact]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/impact",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "impact": impact,
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

    def updatetitle(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/subject",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updatetext(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/text",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updatestatus(
        self,
        id: int,
        *,
        request: int,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/status",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updateassignee(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/assignee",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updateestimatedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/estimatedTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updatecompletedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/completedTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def updateremainingtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/remainingTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    def getticketcomments(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagedResultOfTicketComment]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagedResultOfTicketComment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicketComment,
                    parse_obj_as(
                        type_=PagedResultOfTicketComment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def postticketcomment(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicketComment]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketComment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "text": text,
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
                    TicketComment,
                    parse_obj_as(
                        type_=TicketComment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def getticketcommentbyid(
        self,
        id: int,
        comment_id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicketComment]:
        """
        Parameters
        ----------
        id : int

        comment_id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketComment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments/{encode_path_param(comment_id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketComment,
                    parse_obj_as(
                        type_=TicketComment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def gettickets(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        status: typing.Optional[typing.Sequence[int]] = None,
        assignee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagedResultOfTicket]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        status : typing.Optional[typing.Sequence[int]]

        assignee_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagedResultOfTicket]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Tickets",
            method="GET",
            params={
                "organizationId": organization_id,
                "projectId": project_id,
                "status": status,
                "assigneeId": assignee_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicket,
                    parse_obj_as(
                        type_=PagedResultOfTicket,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def createticket(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        assignee_id: typing.Optional[str] = OMIT,
        estimated_time: typing.Optional[str] = OMIT,
        completed_time: typing.Optional[str] = OMIT,
        remaining_time: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        impact: typing.Optional[TicketImpact] = OMIT,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ticket]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        title : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[int]

        assignee_id : typing.Optional[str]

        estimated_time : typing.Optional[str]

        completed_time : typing.Optional[str]

        remaining_time : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        impact : typing.Optional[TicketImpact]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ticket]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Tickets",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "projectId": project_id,
                "title": title,
                "description": description,
                "status": status,
                "assigneeId": assignee_id,
                "estimatedTime": estimated_time,
                "completedTime": completed_time,
                "remainingTime": remaining_time,
                "priority": priority,
                "impact": impact,
                "urgency": urgency,
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
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
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

    async def getticketevents(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagedResultOfTicketEvent]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagedResultOfTicketEvent]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/events",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicketEvent,
                    parse_obj_as(
                        type_=PagedResultOfTicketEvent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def getticketbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ticket]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ticket]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Ticket,
                    parse_obj_as(
                        type_=Ticket,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def deleteticket(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
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

    async def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/project",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "projectId": project_id,
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

    async def updatepriority(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        priority: typing.Optional[TicketPriority] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/priority",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "priority": priority,
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

    async def updateurgency(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/urgency",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "urgency": urgency,
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

    async def updateimpact(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        impact: typing.Optional[TicketImpact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        impact : typing.Optional[TicketImpact]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/impact",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "impact": impact,
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

    async def updatetitle(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/subject",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updatetext(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/text",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updatestatus(
        self,
        id: int,
        *,
        request: int,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/status",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updateassignee(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/assignee",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updateestimatedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/estimatedTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updatecompletedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/completedTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def updateremainingtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/remainingTime",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
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

    async def getticketcomments(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagedResultOfTicketComment]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagedResultOfTicketComment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedResultOfTicketComment,
                    parse_obj_as(
                        type_=PagedResultOfTicketComment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def postticketcomment(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicketComment]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketComment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "text": text,
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
                    TicketComment,
                    parse_obj_as(
                        type_=TicketComment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def getticketcommentbyid(
        self,
        id: int,
        comment_id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicketComment]:
        """
        Parameters
        ----------
        id : int

        comment_id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketComment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Tickets/{encode_path_param(id)}/comments/{encode_path_param(comment_id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketComment,
                    parse_obj_as(
                        type_=TicketComment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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
