

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.code import Code
from ..types.code_delivery import CodeDelivery
from ..types.email import Email
from ..types.pass_ import Pass
from ..types.problem import Problem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_code(
        self, *, email: Email, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CodeDelivery]:
        """
        Sends a one-time code to the given address. The answer is the same whether or not an account already exists behind that address: telling the two apart would turn this into a directory of registered people. The code travels by mail only and is never part of any response.

        Parameters
        ----------
        email : Email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CodeDelivery]
            The code was sent. Nothing here says whether an account exists, and nothing here promises the mail arrived — delivery is the only real test, and its outcome belongs to the mailbox, not to this answer.
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/codes",
            method="POST",
            json={
                "email": email,
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
                    CodeDelivery,
                    parse_obj_as(
                        type_=CodeDelivery,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    def create_session(
        self, *, email: Email, code: Code, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Pass]:
        """
        Exchanges an emailed code for a pass. The account comes into being here if the address had none: signing in and signing up are one act, because separating them would mean saying whether the address is known, and that is what this API refuses to say. The code is checked together with the address it was issued for — six digits are not unique, and alone they identify nobody.

        Parameters
        ----------
        email : Email

        code : Code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pass]
            Signed in. The answer does not say whether the account was born just now: that is a state, not an event, and it is read from the person, not from this moment.
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/sessions",
            method="POST",
            json={
                "email": email,
                "code": code,
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
                    Pass,
                    parse_obj_as(
                        type_=Pass,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    def delete_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Ends the session the presented token belongs to, on this device only — the other devices a person is signed in on know nothing of it.
        It takes effect at once, including for the access token just used. That token is not recalled and cannot be: it is believed on its signature alone. But every guarded operation asks after the session behind the token it was shown, and from here on the answer is that there is none. The refresh token goes the same way and for the same reason — it buys keys to a session, and there is no longer a session to buy them for. Neither is crossed out one by one; both die of what they point at.
        Signing out twice answers 401 rather than 204. The second attempt arrives holding a pass that no longer stands, and is turned away before it can be read as a request at all — the same answer every other operation now gives it.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/sessions/current",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    def refresh_session(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Pass]:
        """
        Issues new keys for the session the presented token belongs to. The session itself is not replaced: it lasts from signing in until signing out, and these are only its keys. The token presented here is spent in the act — a second use of the same one means a copy is loose, and then the session ends for everyone holding it, the rightful owner included.

        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pass]
            Fresh pass issued
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/sessions/current/refresh",
            method="POST",
            json={
                "refresh_token": refresh_token,
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
                    Pass,
                    parse_obj_as(
                        type_=Pass,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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


class AsyncRawAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_code(
        self, *, email: Email, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CodeDelivery]:
        """
        Sends a one-time code to the given address. The answer is the same whether or not an account already exists behind that address: telling the two apart would turn this into a directory of registered people. The code travels by mail only and is never part of any response.

        Parameters
        ----------
        email : Email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CodeDelivery]
            The code was sent. Nothing here says whether an account exists, and nothing here promises the mail arrived — delivery is the only real test, and its outcome belongs to the mailbox, not to this answer.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/codes",
            method="POST",
            json={
                "email": email,
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
                    CodeDelivery,
                    parse_obj_as(
                        type_=CodeDelivery,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    async def create_session(
        self, *, email: Email, code: Code, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Pass]:
        """
        Exchanges an emailed code for a pass. The account comes into being here if the address had none: signing in and signing up are one act, because separating them would mean saying whether the address is known, and that is what this API refuses to say. The code is checked together with the address it was issued for — six digits are not unique, and alone they identify nobody.

        Parameters
        ----------
        email : Email

        code : Code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pass]
            Signed in. The answer does not say whether the account was born just now: that is a state, not an event, and it is read from the person, not from this moment.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/sessions",
            method="POST",
            json={
                "email": email,
                "code": code,
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
                    Pass,
                    parse_obj_as(
                        type_=Pass,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    async def delete_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Ends the session the presented token belongs to, on this device only — the other devices a person is signed in on know nothing of it.
        It takes effect at once, including for the access token just used. That token is not recalled and cannot be: it is believed on its signature alone. But every guarded operation asks after the session behind the token it was shown, and from here on the answer is that there is none. The refresh token goes the same way and for the same reason — it buys keys to a session, and there is no longer a session to buy them for. Neither is crossed out one by one; both die of what they point at.
        Signing out twice answers 401 rather than 204. The second attempt arrives holding a pass that no longer stands, and is turned away before it can be read as a request at all — the same answer every other operation now gives it.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/sessions/current",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    async def refresh_session(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Pass]:
        """
        Issues new keys for the session the presented token belongs to. The session itself is not replaced: it lasts from signing in until signing out, and these are only its keys. The token presented here is spent in the act — a second use of the same one means a copy is loose, and then the session ends for everyone holding it, the rightful owner included.

        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pass]
            Fresh pass issued
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/sessions/current/refresh",
            method="POST",
            json={
                "refresh_token": refresh_token,
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
                    Pass,
                    parse_obj_as(
                        type_=Pass,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
