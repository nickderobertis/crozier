

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
from .types.ask_transcript_question_response import AskTranscriptQuestionResponse
from .types.create_transcript_response import CreateTranscriptResponse
from .types.get_transcript_question_response import GetTranscriptQuestionResponse
from .types.get_transcript_response import GetTranscriptResponse
from .types.list_transcript_questions_response import ListTranscriptQuestionsResponse
from .types.list_transcripts_response import ListTranscriptsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSpeechToTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_transcripts(
        self,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTranscriptsResponse]:
        """
        Retrieve paginated list of transcript jobs

        Parameters
        ----------
        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTranscriptsResponse]
            List of transcripts
        """
        _response = self._client_wrapper.httpx_client.request(
            "speech-to-text",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTranscriptsResponse,
                    parse_obj_as(
                        type_=ListTranscriptsResponse,
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

    def create_transcript(
        self,
        *,
        audio_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTranscriptResponse]:
        """
        Submit audio or video for transcription

        Parameters
        ----------
        audio_token : typing.Optional[str]
            Signed ActiveStorage token

        url : typing.Optional[str]
            HTTPS URL to audio/video file

        query : typing.Optional[str]
            Optional intelligence question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTranscriptResponse]
            Transcript job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "speech-to-text",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_token": audio_token,
                "url": url,
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
                    CreateTranscriptResponse,
                    parse_obj_as(
                        type_=CreateTranscriptResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_transcript(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTranscriptResponse]:
        """
        Retrieve transcript status, text, and timestamps

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTranscriptResponse]
            Transcript details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTranscriptResponse,
                    parse_obj_as(
                        type_=GetTranscriptResponse,
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

    def ask_transcript_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AskTranscriptQuestionResponse]:
        """
        Submit a question about a completed transcript

        Parameters
        ----------
        uuid_ : str

        query : str
            Question to ask about the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AskTranscriptQuestionResponse]
            Question submitted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/ask",
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
                    AskTranscriptQuestionResponse,
                    parse_obj_as(
                        type_=AskTranscriptQuestionResponse,
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

    def list_transcript_questions(
        self,
        uuid_: str,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTranscriptQuestionsResponse]:
        """
        List all questions asked about a transcript

        Parameters
        ----------
        uuid_ : str

        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTranscriptQuestionsResponse]
            List of questions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/questions",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTranscriptQuestionsResponse,
                    parse_obj_as(
                        type_=ListTranscriptQuestionsResponse,
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

    def get_transcript_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTranscriptQuestionResponse]:
        """
        Check the status of a specific question

        Parameters
        ----------
        uuid_ : str

        question_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTranscriptQuestionResponse]
            Question details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/questions/{encode_path_param(question_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTranscriptQuestionResponse,
                    parse_obj_as(
                        type_=GetTranscriptQuestionResponse,
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


class AsyncRawSpeechToTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_transcripts(
        self,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTranscriptsResponse]:
        """
        Retrieve paginated list of transcript jobs

        Parameters
        ----------
        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTranscriptsResponse]
            List of transcripts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "speech-to-text",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTranscriptsResponse,
                    parse_obj_as(
                        type_=ListTranscriptsResponse,
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

    async def create_transcript(
        self,
        *,
        audio_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTranscriptResponse]:
        """
        Submit audio or video for transcription

        Parameters
        ----------
        audio_token : typing.Optional[str]
            Signed ActiveStorage token

        url : typing.Optional[str]
            HTTPS URL to audio/video file

        query : typing.Optional[str]
            Optional intelligence question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTranscriptResponse]
            Transcript job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "speech-to-text",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_token": audio_token,
                "url": url,
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
                    CreateTranscriptResponse,
                    parse_obj_as(
                        type_=CreateTranscriptResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_transcript(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTranscriptResponse]:
        """
        Retrieve transcript status, text, and timestamps

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTranscriptResponse]
            Transcript details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTranscriptResponse,
                    parse_obj_as(
                        type_=GetTranscriptResponse,
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

    async def ask_transcript_question(
        self, uuid_: str, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AskTranscriptQuestionResponse]:
        """
        Submit a question about a completed transcript

        Parameters
        ----------
        uuid_ : str

        query : str
            Question to ask about the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AskTranscriptQuestionResponse]
            Question submitted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/ask",
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
                    AskTranscriptQuestionResponse,
                    parse_obj_as(
                        type_=AskTranscriptQuestionResponse,
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

    async def list_transcript_questions(
        self,
        uuid_: str,
        *,
        page: int,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTranscriptQuestionsResponse]:
        """
        List all questions asked about a transcript

        Parameters
        ----------
        uuid_ : str

        page : int

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTranscriptQuestionsResponse]
            List of questions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/questions",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTranscriptQuestionsResponse,
                    parse_obj_as(
                        type_=ListTranscriptQuestionsResponse,
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

    async def get_transcript_question(
        self, uuid_: str, question_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTranscriptQuestionResponse]:
        """
        Check the status of a specific question

        Parameters
        ----------
        uuid_ : str

        question_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTranscriptQuestionResponse]
            Question details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"speech-to-text/{encode_path_param(uuid_)}/questions/{encode_path_param(question_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTranscriptQuestionResponse,
                    parse_obj_as(
                        type_=GetTranscriptQuestionResponse,
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
