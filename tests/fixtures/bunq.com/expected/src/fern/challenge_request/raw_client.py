

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.master_card_identity_check_challenge_request_user_read import (
    MasterCardIdentityCheckChallengeRequestUserRead,
)
from ..types.master_card_identity_check_challenge_request_user_update import (
    MasterCardIdentityCheckChallengeRequestUserUpdate,
)


OMIT = typing.cast(typing.Any, ...)


class RawChallengeRequestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_challenge_request_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MasterCardIdentityCheckChallengeRequestUserRead]:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MasterCardIdentityCheckChallengeRequestUserRead]
            Endpoint for apps to fetch a challenge request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/challenge-request/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MasterCardIdentityCheckChallengeRequestUserRead,
                    parse_obj_as(
                        type_=MasterCardIdentityCheckChallengeRequestUserRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_challenge_request_for_user(
        self, user_id: int, item_id: int, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MasterCardIdentityCheckChallengeRequestUserUpdate]:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : str
            The status of the identity check. Can be ACCEPTED_PENDING_RESPONSE or REJECTED_PENDING_RESPONSE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MasterCardIdentityCheckChallengeRequestUserUpdate]
            Endpoint for apps to fetch a challenge request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/challenge-request/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "status": status,
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
                    MasterCardIdentityCheckChallengeRequestUserUpdate,
                    parse_obj_as(
                        type_=MasterCardIdentityCheckChallengeRequestUserUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawChallengeRequestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_challenge_request_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MasterCardIdentityCheckChallengeRequestUserRead]:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MasterCardIdentityCheckChallengeRequestUserRead]
            Endpoint for apps to fetch a challenge request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/challenge-request/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MasterCardIdentityCheckChallengeRequestUserRead,
                    parse_obj_as(
                        type_=MasterCardIdentityCheckChallengeRequestUserRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_challenge_request_for_user(
        self, user_id: int, item_id: int, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MasterCardIdentityCheckChallengeRequestUserUpdate]:
        """
        Endpoint for apps to fetch a challenge request.

        Parameters
        ----------
        user_id : int


        item_id : int


        status : str
            The status of the identity check. Can be ACCEPTED_PENDING_RESPONSE or REJECTED_PENDING_RESPONSE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MasterCardIdentityCheckChallengeRequestUserUpdate]
            Endpoint for apps to fetch a challenge request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/challenge-request/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "status": status,
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
                    MasterCardIdentityCheckChallengeRequestUserUpdate,
                    parse_obj_as(
                        type_=MasterCardIdentityCheckChallengeRequestUserUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
