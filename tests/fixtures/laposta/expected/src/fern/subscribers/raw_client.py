

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
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.history import History
from ..types.member_envelope import MemberEnvelope
from ..types.member_list import MemberList
from .types.alle_relaties_opvragen_request_state import AlleRelatiesOpvragenRequestState
from .types.relatie_wijzigen_request_state import RelatieWijzigenRequestState
from .types.relatiegeschiedenis_opvragen_request_order import RelatiegeschiedenisOpvragenRequestOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubscribersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alle_relaties_opvragen(
        self,
        *,
        list_id: str,
        state: typing.Optional[AlleRelatiesOpvragenRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberList]:
        """
        All fields of a list in an array of member objects. The member objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        state : typing.Optional[AlleRelatiesOpvragenRequestState]
            The status of the requested subscribers: active, unsubscribed or cleaned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberList]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "member",
            method="GET",
            params={
                "list_id": list_id,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberList,
                    parse_obj_as(
                        type_=MemberList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def relatie_toevoegen(
        self,
        *,
        list_id: str,
        ip: str,
        email: str,
        source_url: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        options: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You can use this in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        ip : str
            The IP address the sign-up came from. For a form on your site that is the visitor address, not your server address.

        email : str
            The email address of the subscriber to be added

        source_url : typing.Optional[str]
            The URL from which the subscriber is registered

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            The values of the extra fields. The name (key) of the field is the 'custom_name' (part of the Field object). This is the same as the 'Variable' in the application. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Without those brackets the call still succeeds but nothing changes, and a label that the list does not have returns error code 203.

        options : typing.Optional[typing.Sequence[typing.Any]]
            Additional instructions, with possibilities being: upsert: true to overwrite fields if the email address is already linked to an active contact in this list. Normally, you would receive an error if the email address is already linked to an active contact. Note: If a subscriber is unsubscribed and you perform an upsert with that email address, it will be set to active again. If you want to prevent an unsubscribed subscriber from being reactivated, you can use the suppress_reactivation option. suppress_reactivation: true to prevent an unsubscribed subscriber from being reactivated during an upsert suppress_email_notification: true to prevent a notification email from being sent every time someone logs in via an API ignore_doubleoptin: true to instantly activate subscribers on a double-optin list and ensure that no confirmation email is sent when signing up through the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "member",
            method="POST",
            data={
                "list_id": list_id,
                "ip": ip,
                "email": email,
                "source_url": source_url,
                "custom_fields": custom_fields,
                "options": options,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def relatie_opvragen(
        self, member_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MemberEnvelope]:
        """
        All information about a subscriber in a member object

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def relatie_wijzigen(
        self,
        member_id: str,
        *,
        list_id: str,
        email: typing.Optional[str] = OMIT,
        state: typing.Optional[RelatieWijzigenRequestState] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MemberEnvelope]:
        """
        You only have to include the fields that need to be modified in the request. Fields that are not named will keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        member_id : str

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        email : typing.Optional[str]
            The email address of the subscriber that must be modified

        state : typing.Optional[RelatieWijzigenRequestState]
            The new status of the subscriber: active or unsubscribed

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            The values of the extra created fields. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Only labels the list already has are accepted; you create new labels in the application or during an import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "email": email,
                "state": state,
                "custom_fields": custom_fields,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def relatie_verwijderen(
        self, member_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MemberEnvelope]:
        """
        This permanently deletes a subscriber. If the subscriber does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the subscriber.

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def relatiegeschiedenis_opvragen(
        self,
        member_id: str,
        *,
        list_id: str,
        campaign_id: typing.Optional[str] = None,
        event_date_from: typing.Optional[str] = None,
        event_date_to: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        order: typing.Optional[RelatiegeschiedenisOpvragenRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[History]:
        """
        The full event history of a subscriber, similar to the details shown in the application.

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        campaign_id : typing.Optional[str]
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        event_date_from : typing.Optional[str]
            Only return events from this date and time, inclusive. Use the regular format or ISO format described above.

        event_date_to : typing.Optional[str]
            Only return events before this date and time, exclusive. Use the regular format or ISO format described above.

        limit : typing.Optional[int]
            Maximum number of history items to return. Default is 100, maximum is 1000

        cursor : typing.Optional[str]
            Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.

        order_by : typing.Optional[str]
            Field to order by. Currently only event_date is supported

        order : typing.Optional[RelatiegeschiedenisOpvragenRequestOrder]
            Sort direction: desc or asc. Default is desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[History]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}/history",
            method="GET",
            params={
                "list_id": list_id,
                "campaign_id": campaign_id,
                "event_date_from": event_date_from,
                "event_date_to": event_date_to,
                "limit": limit,
                "cursor": cursor,
                "order_by": order_by,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    History,
                    parse_obj_as(
                        type_=History,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawSubscribersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def alle_relaties_opvragen(
        self,
        *,
        list_id: str,
        state: typing.Optional[AlleRelatiesOpvragenRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberList]:
        """
        All fields of a list in an array of member objects. The member objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        state : typing.Optional[AlleRelatiesOpvragenRequestState]
            The status of the requested subscribers: active, unsubscribed or cleaned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberList]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "member",
            method="GET",
            params={
                "list_id": list_id,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberList,
                    parse_obj_as(
                        type_=MemberList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def relatie_toevoegen(
        self,
        *,
        list_id: str,
        ip: str,
        email: str,
        source_url: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        options: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You can use this in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        ip : str
            The IP address the sign-up came from. For a form on your site that is the visitor address, not your server address.

        email : str
            The email address of the subscriber to be added

        source_url : typing.Optional[str]
            The URL from which the subscriber is registered

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            The values of the extra fields. The name (key) of the field is the 'custom_name' (part of the Field object). This is the same as the 'Variable' in the application. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Without those brackets the call still succeeds but nothing changes, and a label that the list does not have returns error code 203.

        options : typing.Optional[typing.Sequence[typing.Any]]
            Additional instructions, with possibilities being: upsert: true to overwrite fields if the email address is already linked to an active contact in this list. Normally, you would receive an error if the email address is already linked to an active contact. Note: If a subscriber is unsubscribed and you perform an upsert with that email address, it will be set to active again. If you want to prevent an unsubscribed subscriber from being reactivated, you can use the suppress_reactivation option. suppress_reactivation: true to prevent an unsubscribed subscriber from being reactivated during an upsert suppress_email_notification: true to prevent a notification email from being sent every time someone logs in via an API ignore_doubleoptin: true to instantly activate subscribers on a double-optin list and ensure that no confirmation email is sent when signing up through the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "member",
            method="POST",
            data={
                "list_id": list_id,
                "ip": ip,
                "email": email,
                "source_url": source_url,
                "custom_fields": custom_fields,
                "options": options,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def relatie_opvragen(
        self, member_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MemberEnvelope]:
        """
        All information about a subscriber in a member object

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def relatie_wijzigen(
        self,
        member_id: str,
        *,
        list_id: str,
        email: typing.Optional[str] = OMIT,
        state: typing.Optional[RelatieWijzigenRequestState] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MemberEnvelope]:
        """
        You only have to include the fields that need to be modified in the request. Fields that are not named will keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        member_id : str

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        email : typing.Optional[str]
            The email address of the subscriber that must be modified

        state : typing.Optional[RelatieWijzigenRequestState]
            The new status of the subscriber: active or unsubscribed

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            The values of the extra created fields. You pass labels as an array, with square brackets: custom_fields[labels][]=Klant. Only labels the list already has are accepted; you create new labels in the application or during an import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "email": email,
                "state": state,
                "custom_fields": custom_fields,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def relatie_verwijderen(
        self, member_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MemberEnvelope]:
        """
        This permanently deletes a subscriber. If the subscriber does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the subscriber.

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MemberEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MemberEnvelope,
                    parse_obj_as(
                        type_=MemberEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def relatiegeschiedenis_opvragen(
        self,
        member_id: str,
        *,
        list_id: str,
        campaign_id: typing.Optional[str] = None,
        event_date_from: typing.Optional[str] = None,
        event_date_to: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        order: typing.Optional[RelatiegeschiedenisOpvragenRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[History]:
        """
        The full event history of a subscriber, similar to the details shown in the application.

        Parameters
        ----------
        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        campaign_id : typing.Optional[str]
            The id of the campaign. You find it in the response of [Get all campaigns](/campagnes/alle-campagnes-opvragen).

        event_date_from : typing.Optional[str]
            Only return events from this date and time, inclusive. Use the regular format or ISO format described above.

        event_date_to : typing.Optional[str]
            Only return events before this date and time, exclusive. Use the regular format or ISO format described above.

        limit : typing.Optional[int]
            Maximum number of history items to return. Default is 100, maximum is 1000

        cursor : typing.Optional[str]
            Cursor from pagination.next_cursor to request the next page. Do not interpret this value yourself; send it back unchanged.

        order_by : typing.Optional[str]
            Field to order by. Currently only event_date is supported

        order : typing.Optional[RelatiegeschiedenisOpvragenRequestOrder]
            Sort direction: desc or asc. Default is desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[History]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"member/{encode_path_param(member_id)}/history",
            method="GET",
            params={
                "list_id": list_id,
                "campaign_id": campaign_id,
                "event_date_from": event_date_from,
                "event_date_to": event_date_to,
                "limit": limit,
                "cursor": cursor,
                "order_by": order_by,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    History,
                    parse_obj_as(
                        type_=History,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
