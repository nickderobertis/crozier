

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.open_questions import OpenQuestions
from ..types.ticket import Ticket
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawQuestionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_open_questions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OpenQuestions]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenQuestions]
            The open questions.
        """
        _response = self._client_wrapper.httpx_client.request(
            "questions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenQuestions,
                    parse_obj_as(
                        type_=OpenQuestions,
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

    def file_question(
        self,
        *,
        bench: str,
        question_bench: str,
        asked_by: str,
        urgent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ticket]:
        """
        Parameters
        ----------
        bench : str
            The bench the question is filed under.

        question_bench : str
            The bench the question is about.

        asked_by : str
            The grower asking.

        urgent : typing.Optional[bool]
            Whether a keeper should answer today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ticket]
            The filed question's ticket.
        """
        _response = self._client_wrapper.httpx_client.request(
            "questions",
            method="POST",
            params={
                "bench": bench,
            },
            json={
                "bench": bench,
                "asked_by": asked_by,
                "urgent": urgent,
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


class AsyncRawQuestionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_open_questions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OpenQuestions]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenQuestions]
            The open questions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "questions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenQuestions,
                    parse_obj_as(
                        type_=OpenQuestions,
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

    async def file_question(
        self,
        *,
        bench: str,
        question_bench: str,
        asked_by: str,
        urgent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ticket]:
        """
        Parameters
        ----------
        bench : str
            The bench the question is filed under.

        question_bench : str
            The bench the question is about.

        asked_by : str
            The grower asking.

        urgent : typing.Optional[bool]
            Whether a keeper should answer today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ticket]
            The filed question's ticket.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "questions",
            method="POST",
            params={
                "bench": bench,
            },
            json={
                "bench": bench,
                "asked_by": asked_by,
                "urgent": urgent,
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
