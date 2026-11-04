

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
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error import Error
from .types.ask_detect_intelligence_question_response import AskDetectIntelligenceQuestionResponse
from .types.get_detect_intelligence_question_response import GetDetectIntelligenceQuestionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDetectIntelligenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ask_detect_intelligence_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AskDetectIntelligenceQuestionResponse]:
        """
        Submit a natural-language question about a completed detection report. Returns 202 Accepted while the answer is generated in the background.

        Parameters
        ----------
        uuid_ : str
            UUID of the completed detection report

        query : str
            The natural-language question to ask about the detection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AskDetectIntelligenceQuestionResponse]
            Question accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"detects/{encode_path_param(uuid_)}/intelligence",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "query": query,
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
                    AskDetectIntelligenceQuestionResponse,
                    parse_obj_as(
                        type_=AskDetectIntelligenceQuestionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_detect_intelligence_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDetectIntelligenceQuestionResponse]:
        """
        Retrieve the status and answer for a previously submitted question. Poll until status is completed or failed.

        Parameters
        ----------
        uuid_ : str
            UUID of the detection report

        question_uuid : str
            UUID of the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDetectIntelligenceQuestionResponse]
            Question status and answer
        """
        _response = self._client_wrapper.httpx_client.request(
            f"detects/{encode_path_param(uuid_)}/intelligence/{encode_path_param(question_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDetectIntelligenceQuestionResponse,
                    parse_obj_as(
                        type_=GetDetectIntelligenceQuestionResponse,
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


class AsyncRawDetectIntelligenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ask_detect_intelligence_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AskDetectIntelligenceQuestionResponse]:
        """
        Submit a natural-language question about a completed detection report. Returns 202 Accepted while the answer is generated in the background.

        Parameters
        ----------
        uuid_ : str
            UUID of the completed detection report

        query : str
            The natural-language question to ask about the detection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AskDetectIntelligenceQuestionResponse]
            Question accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"detects/{encode_path_param(uuid_)}/intelligence",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "query": query,
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
                    AskDetectIntelligenceQuestionResponse,
                    parse_obj_as(
                        type_=AskDetectIntelligenceQuestionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_detect_intelligence_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDetectIntelligenceQuestionResponse]:
        """
        Retrieve the status and answer for a previously submitted question. Poll until status is completed or failed.

        Parameters
        ----------
        uuid_ : str
            UUID of the detection report

        question_uuid : str
            UUID of the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDetectIntelligenceQuestionResponse]
            Question status and answer
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"detects/{encode_path_param(uuid_)}/intelligence/{encode_path_param(question_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDetectIntelligenceQuestionResponse,
                    parse_obj_as(
                        type_=GetDetectIntelligenceQuestionResponse,
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
