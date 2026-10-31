

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.audio_reference import AudioReference
from ..types.base_response import BaseResponse
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSpeakerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_speakers(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        List all available speakers with optional pagination and detail control.

        - `detailed`: If true, returns complete metadata including references and embeddings.
        - `offset` / `limit`: Support for paginated speaker listing.

        Parameters
        ----------
        detailed : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speakers/list",
            method="GET",
            params={
                "detailed": detailed,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def refresh_speakers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BaseResponse]:
        """
        Force reload of all speaker metadata from disk.
        Use this when files are modified externally or newly added.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speakers/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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

    def update_speakers(
        self,
        *,
        speakers: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Batch update multiple speakers by providing a list of speaker JSON configs.

        Each speaker must already exist (matched by ID).
        Will overwrite corresponding fields and persist changes to disk.

        Parameters
        ----------
        speakers : typing.Sequence[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speakers/update",
            method="POST",
            json={
                "speakers": speakers,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_speaker(
        self,
        *,
        name: str,
        gender: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        wavs: typing.Optional[typing.Sequence[AudioReference]] = OMIT,
        save_file: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Create a new speaker profile with optional reference audios.

        - `name` is required and used as unique identifier.
        - `wavs` is a list of audio samples (base64-encoded) and reference texts for embedding.
        - `save_file`: If true, the speaker will be saved to disk and available after refresh.

        Parameters
        ----------
        name : str

        gender : typing.Optional[str]

        author : typing.Optional[str]

        desc : typing.Optional[str]

        version : typing.Optional[str]

        wavs : typing.Optional[typing.Sequence[AudioReference]]

        save_file : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speaker/create",
            method="POST",
            json={
                "name": name,
                "gender": gender,
                "author": author,
                "desc": desc,
                "version": version,
                "wavs": convert_and_respect_annotation_metadata(
                    object_=wavs, annotation=typing.Optional[typing.Sequence[AudioReference]], direction="write"
                ),
                "save_file": save_file,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_speaker(
        self,
        *,
        json: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Update a single speaker's configuration by full JSON override.

        The speaker must already exist (matched by ID).
        Fields like name, gender, refs, etc., will be updated accordingly.

        Parameters
        ----------
        json : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speaker/update",
            method="POST",
            json={
                "json": json,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def speaker_detail(
        self,
        *,
        id: str,
        with_emb: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Fetch metadata of a specific speaker by ID.

        - `with_emb`: If true, includes embedding vectors and all reference data.

        Parameters
        ----------
        id : str

        with_emb : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speaker/detail",
            method="POST",
            json={
                "id": id,
                "with_emb": with_emb,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawSpeakerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_speakers(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        List all available speakers with optional pagination and detail control.

        - `detailed`: If true, returns complete metadata including references and embeddings.
        - `offset` / `limit`: Support for paginated speaker listing.

        Parameters
        ----------
        detailed : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speakers/list",
            method="GET",
            params={
                "detailed": detailed,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def refresh_speakers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Force reload of all speaker metadata from disk.
        Use this when files are modified externally or newly added.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speakers/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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

    async def update_speakers(
        self,
        *,
        speakers: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Batch update multiple speakers by providing a list of speaker JSON configs.

        Each speaker must already exist (matched by ID).
        Will overwrite corresponding fields and persist changes to disk.

        Parameters
        ----------
        speakers : typing.Sequence[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speakers/update",
            method="POST",
            json={
                "speakers": speakers,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_speaker(
        self,
        *,
        name: str,
        gender: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        wavs: typing.Optional[typing.Sequence[AudioReference]] = OMIT,
        save_file: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Create a new speaker profile with optional reference audios.

        - `name` is required and used as unique identifier.
        - `wavs` is a list of audio samples (base64-encoded) and reference texts for embedding.
        - `save_file`: If true, the speaker will be saved to disk and available after refresh.

        Parameters
        ----------
        name : str

        gender : typing.Optional[str]

        author : typing.Optional[str]

        desc : typing.Optional[str]

        version : typing.Optional[str]

        wavs : typing.Optional[typing.Sequence[AudioReference]]

        save_file : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speaker/create",
            method="POST",
            json={
                "name": name,
                "gender": gender,
                "author": author,
                "desc": desc,
                "version": version,
                "wavs": convert_and_respect_annotation_metadata(
                    object_=wavs, annotation=typing.Optional[typing.Sequence[AudioReference]], direction="write"
                ),
                "save_file": save_file,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_speaker(
        self,
        *,
        json: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Update a single speaker's configuration by full JSON override.

        The speaker must already exist (matched by ID).
        Fields like name, gender, refs, etc., will be updated accordingly.

        Parameters
        ----------
        json : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speaker/update",
            method="POST",
            json={
                "json": json,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def speaker_detail(
        self,
        *,
        id: str,
        with_emb: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Fetch metadata of a specific speaker by ID.

        - `with_emb`: If true, includes embedding vectors and all reference data.

        Parameters
        ----------
        id : str

        with_emb : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speaker/detail",
            method="POST",
            json={
                "id": id,
                "with_emb": with_emb,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
