

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
from ..types.list_envelope import ListEnvelope
from ..types.list_list import ListList
from ..types.sync_result import SyncResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alle_lijsten_opvragen(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListList]:
        """
        All lists in an array of list objects. The list objects have been ordered in an array with the name 'data'. No parameters need to be provided.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListList]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListList,
                    parse_obj_as(
                        type_=ListList,
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

    def lijst_toevoegen(
        self,
        *,
        name: str,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You may use these in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        name : str
            Name given to the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "list",
            method="POST",
            data={
                "name": name,
                "locked": locked,
                "remarks": remarks,
                "subscribe_notification_email": subscribe_notification_email,
                "unsubscribe_notification_email": unsubscribe_notification_email,
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
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    def lijst_opvragen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListEnvelope]:
        """
        All information about a list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    def lijst_wijzigen(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListEnvelope]:
        """
        You will only have to include the fields that need to be modified in the application. Fields that are not mentioned will keep their current value. As soon as a field is mentioned, it is checked and may therefore cause an error message. A code is displayed with this error message. You may use this code in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            A name for the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="POST",
            data={
                "name": name,
                "locked": locked,
                "remarks": remarks,
                "subscribe_notification_email": subscribe_notification_email,
                "unsubscribe_notification_email": unsubscribe_notification_email,
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
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    def lijst_verwijderen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListEnvelope]:
        """
        This permanently deletes a list. If the list does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    def lijst_synchroniseren_bulk(
        self,
        list_id: str,
        *,
        actions: str,
        members: typing.Dict[str, typing.Any],
        member_id: str,
        email: str,
        custom_fields: typing.Dict[str, typing.Any],
        mode_verouderd: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SyncResult]:
        """
        Adds, updates or unsubscribes multiple subscribers in one request. This endpoint is off by default: an account without access gets a 401 with the message "Not permitted to issue bulk requests (1)". Contact Laposta to have it enabled for your account.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        actions : str
            An array with at least one of the following options: add, update, or unsubscribe_excluded. These determine whether members may be added, updated and/or unsubscribed (read details below).

        members : typing.Dict[str, typing.Any]
            An array with member objects. A minimum of 1, maximum of 500,000.

        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        email : str
            The email address of the relation to be changed or added. If the member_id is also specified, then a new email address can be specified here for the existing relation.

        custom_fields : typing.Dict[str, typing.Any]
            A JSON object where the key is the name of the extra field and the value is the value of the extra field.

        mode_verouderd : typing.Optional[str]
            For backwards compatibility you can still pass edit, add or add_and_edit, but this parameter is being phased out. Do not send mode together with actions.

        source_url : typing.Optional[str]
            The URL from which the relation was registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SyncResult]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}/members",
            method="POST",
            json={
                "actions": actions,
                "mode (verouderd)": mode_verouderd,
                "members": members,
                "member_id": member_id,
                "email": email,
                "custom_fields": custom_fields,
                "source_url": source_url,
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
                    SyncResult,
                    parse_obj_as(
                        type_=SyncResult,
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

    def lijst_leegmaken(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListEnvelope]:
        """
        This permanently purges all active subscribers from a list, but doesn't delete the list itself. If the list does not exist, an error message is displayed. In response, you are shown another list object.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}/members",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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


class AsyncRawListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def alle_lijsten_opvragen(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListList]:
        """
        All lists in an array of list objects. The list objects have been ordered in an array with the name 'data'. No parameters need to be provided.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListList]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListList,
                    parse_obj_as(
                        type_=ListList,
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

    async def lijst_toevoegen(
        self,
        *,
        name: str,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. You may use these in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        name : str
            Name given to the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "list",
            method="POST",
            data={
                "name": name,
                "locked": locked,
                "remarks": remarks,
                "subscribe_notification_email": subscribe_notification_email,
                "unsubscribe_notification_email": unsubscribe_notification_email,
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
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    async def lijst_opvragen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListEnvelope]:
        """
        All information about a list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    async def lijst_wijzigen(
        self,
        list_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        locked: typing.Optional[bool] = OMIT,
        remarks: typing.Optional[str] = OMIT,
        subscribe_notification_email: typing.Optional[str] = OMIT,
        unsubscribe_notification_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListEnvelope]:
        """
        You will only have to include the fields that need to be modified in the application. Fields that are not mentioned will keep their current value. As soon as a field is mentioned, it is checked and may therefore cause an error message. A code is displayed with this error message. You may use this code in combination with the variable 'parameter' to display a message to the user. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            A name for the list in question

        locked : typing.Optional[bool]
            If a list is locked, it cannot be changed by a user of the application. (true or false)

        remarks : typing.Optional[str]
            Potential remarks

        subscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon a subscription

        unsubscribe_notification_email : typing.Optional[str]
            Email address to which a notification will be sent upon the cancelling of a subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="POST",
            data={
                "name": name,
                "locked": locked,
                "remarks": remarks,
                "subscribe_notification_email": subscribe_notification_email,
                "unsubscribe_notification_email": unsubscribe_notification_email,
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
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    async def lijst_verwijderen(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListEnvelope]:
        """
        This permanently deletes a list. If the list does not exist, an error message is displayed. In response you are shown another list object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the list.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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

    async def lijst_synchroniseren_bulk(
        self,
        list_id: str,
        *,
        actions: str,
        members: typing.Dict[str, typing.Any],
        member_id: str,
        email: str,
        custom_fields: typing.Dict[str, typing.Any],
        mode_verouderd: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SyncResult]:
        """
        Adds, updates or unsubscribes multiple subscribers in one request. This endpoint is off by default: an account without access gets a 401 with the message "Not permitted to issue bulk requests (1)". Contact Laposta to have it enabled for your account.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        actions : str
            An array with at least one of the following options: add, update, or unsubscribe_excluded. These determine whether members may be added, updated and/or unsubscribed (read details below).

        members : typing.Dict[str, typing.Any]
            An array with member objects. A minimum of 1, maximum of 500,000.

        member_id : str
            The id of the subscriber, or simply their email address. Both work.

        email : str
            The email address of the relation to be changed or added. If the member_id is also specified, then a new email address can be specified here for the existing relation.

        custom_fields : typing.Dict[str, typing.Any]
            A JSON object where the key is the name of the extra field and the value is the value of the extra field.

        mode_verouderd : typing.Optional[str]
            For backwards compatibility you can still pass edit, add or add_and_edit, but this parameter is being phased out. Do not send mode together with actions.

        source_url : typing.Optional[str]
            The URL from which the relation was registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SyncResult]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}/members",
            method="POST",
            json={
                "actions": actions,
                "mode (verouderd)": mode_verouderd,
                "members": members,
                "member_id": member_id,
                "email": email,
                "custom_fields": custom_fields,
                "source_url": source_url,
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
                    SyncResult,
                    parse_obj_as(
                        type_=SyncResult,
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

    async def lijst_leegmaken(
        self, list_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListEnvelope]:
        """
        This permanently purges all active subscribers from a list, but doesn't delete the list itself. If the list does not exist, an error message is displayed. In response, you are shown another list object.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"list/{encode_path_param(list_id)}/members",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEnvelope,
                    parse_obj_as(
                        type_=ListEnvelope,
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
