

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.linked_profile import LinkedProfile
from ..types.user import User
from pydantic import ValidationError


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_users(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        minimum_contributions: typing.Optional[float] = None,
        linked_profile: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        submitted_before: typing.Optional[dt.datetime] = None,
        submitted_after: typing.Optional[dt.datetime] = None,
        username: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[User]]:
        """
        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to the users who have contributed to this assignment.

        country : typing.Optional[str]
            Restrict results to the users who have submitted a contribution with a public location located within this country.

        minimum_contributions : typing.Optional[float]
            Restrict results to the users who have submitted at least this many contributions.

        linked_profile : typing.Optional[str]
            Restrict results to the users who a linked profile of this type.

        owned_by : typing.Optional[str]
            Restrict results to the users who are owned by of this owner.

        submitted_before : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution before this date time.

        submitted_after : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution after this date time.

        username : typing.Optional[str]
            Restrict results to the user with this username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[User]]
            A list of users
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "minimumContributions": minimum_contributions,
                "linkedProfile": linked_profile,
                "ownedBy": owned_by,
                "submittedBefore": serialize_datetime(submitted_before) if submitted_before is not None else None,
                "submittedAfter": serialize_datetime(submitted_after) if submitted_after is not None else None,
                "username": username,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    def retrieve_a_single_user_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def retrieve_a_users_linked_profile_by_type(
        self, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LinkedProfile]:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        type : str
            Type of the linked profile to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LinkedProfile]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}/linked/{encode_path_param(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LinkedProfile,
                    parse_obj_as(
                        type_=LinkedProfile,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_users(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        minimum_contributions: typing.Optional[float] = None,
        linked_profile: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        submitted_before: typing.Optional[dt.datetime] = None,
        submitted_after: typing.Optional[dt.datetime] = None,
        username: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[User]]:
        """
        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to the users who have contributed to this assignment.

        country : typing.Optional[str]
            Restrict results to the users who have submitted a contribution with a public location located within this country.

        minimum_contributions : typing.Optional[float]
            Restrict results to the users who have submitted at least this many contributions.

        linked_profile : typing.Optional[str]
            Restrict results to the users who a linked profile of this type.

        owned_by : typing.Optional[str]
            Restrict results to the users who are owned by of this owner.

        submitted_before : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution before this date time.

        submitted_after : typing.Optional[dt.datetime]
            Limit results to users who have submitted at least one contribution after this date time.

        username : typing.Optional[str]
            Restrict results to the user with this username.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[User]]
            A list of users
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "minimumContributions": minimum_contributions,
                "linkedProfile": linked_profile,
                "ownedBy": owned_by,
                "submittedBefore": serialize_datetime(submitted_before) if submitted_before is not None else None,
                "submittedAfter": serialize_datetime(submitted_after) if submitted_after is not None else None,
                "username": username,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    async def retrieve_a_single_user_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def retrieve_a_users_linked_profile_by_type(
        self, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LinkedProfile]:
        """
        Parameters
        ----------
        id : str
            Id of the user to return

        type : str
            Type of the linked profile to fetch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LinkedProfile]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}/linked/{encode_path_param(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LinkedProfile,
                    parse_obj_as(
                        type_=LinkedProfile,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
