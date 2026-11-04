

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error import Error
from .types.bulk_create_pronunciations_response import BulkCreatePronunciationsResponse
from .types.create_pronunciation_response import CreatePronunciationResponse
from .types.delete_pronunciation_response import DeletePronunciationResponse
from .types.get_pronunciation_response import GetPronunciationResponse
from .types.list_pronunciations_request_status import ListPronunciationsRequestStatus
from .types.list_pronunciations_response import ListPronunciationsResponse
from .types.update_pronunciation_response import UpdatePronunciationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCustomPronunciationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_pronunciations(
        self,
        *,
        language: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        status: typing.Optional[ListPronunciationsRequestStatus] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPronunciationsResponse]:
        """
        Retrieve all custom pronunciations for your team, with optional filters.

        Parameters
        ----------
        language : typing.Optional[str]
            Filter by language (e.g., en-us)

        domain : typing.Optional[str]
            Filter by domain (e.g., medical)

        status : typing.Optional[ListPronunciationsRequestStatus]
            Filter by processing status

        active : typing.Optional[bool]
            Filter by active state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPronunciationsResponse]
            List of custom pronunciations
        """
        _response = self._client_wrapper.httpx_client.request(
            "pronunciations",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "language": language,
                "domain": domain,
                "status": status,
                "active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPronunciationsResponse,
                    parse_obj_as(
                        type_=ListPronunciationsResponse,
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

    def create_pronunciation(
        self, *, word: str, audio: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreatePronunciationResponse]:
        """
        Upload a single pronunciation with a reference audio file.

        Parameters
        ----------
        word : str
            The word or phrase (2-100 characters). Letters, accented characters, apostrophes, hyphens, and spaces only.

        audio : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatePronunciationResponse]
            Pronunciation created
        """
        _response = self._client_wrapper.httpx_client.request(
            "pronunciations",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "word": word,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreatePronunciationResponse,
                    parse_obj_as(
                        type_=CreatePronunciationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def bulk_create_pronunciations(
        self, *, zip: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkCreatePronunciationsResponse]:
        """
        Upload multiple pronunciations at once. Each audio file in the ZIP becomes a pronunciation — the filename (without extension) is used as the word.

        Parameters
        ----------
        zip : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkCreatePronunciationsResponse]
            Bulk creation result
        """
        _response = self._client_wrapper.httpx_client.request(
            "pronunciations/bulk",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={},
            files={
                "zip": zip,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkCreatePronunciationsResponse,
                    parse_obj_as(
                        type_=BulkCreatePronunciationsResponse,
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

    def get_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPronunciationResponse]:
        """
        Retrieve a single custom pronunciation by UUID

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPronunciationResponse]
            Pronunciation details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPronunciationResponse,
                    parse_obj_as(
                        type_=GetPronunciationResponse,
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

    def delete_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeletePronunciationResponse]:
        """
        Permanently remove a custom pronunciation. Takes effect immediately.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletePronunciationResponse]
            Pronunciation deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePronunciationResponse,
                    parse_obj_as(
                        type_=DeletePronunciationResponse,
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

    def update_pronunciation(
        self, uuid_: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdatePronunciationResponse]:
        """
        Enable or disable a pronunciation without deleting it. Inactive pronunciations are not used during synthesis.

        Parameters
        ----------
        uuid_ : str

        active : bool
            Set to false to disable, true to re-enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdatePronunciationResponse]
            Pronunciation updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "active": active,
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
                    UpdatePronunciationResponse,
                    parse_obj_as(
                        type_=UpdatePronunciationResponse,
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


class AsyncRawCustomPronunciationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_pronunciations(
        self,
        *,
        language: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        status: typing.Optional[ListPronunciationsRequestStatus] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPronunciationsResponse]:
        """
        Retrieve all custom pronunciations for your team, with optional filters.

        Parameters
        ----------
        language : typing.Optional[str]
            Filter by language (e.g., en-us)

        domain : typing.Optional[str]
            Filter by domain (e.g., medical)

        status : typing.Optional[ListPronunciationsRequestStatus]
            Filter by processing status

        active : typing.Optional[bool]
            Filter by active state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPronunciationsResponse]
            List of custom pronunciations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pronunciations",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "language": language,
                "domain": domain,
                "status": status,
                "active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPronunciationsResponse,
                    parse_obj_as(
                        type_=ListPronunciationsResponse,
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

    async def create_pronunciation(
        self, *, word: str, audio: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreatePronunciationResponse]:
        """
        Upload a single pronunciation with a reference audio file.

        Parameters
        ----------
        word : str
            The word or phrase (2-100 characters). Letters, accented characters, apostrophes, hyphens, and spaces only.

        audio : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatePronunciationResponse]
            Pronunciation created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pronunciations",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "word": word,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreatePronunciationResponse,
                    parse_obj_as(
                        type_=CreatePronunciationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def bulk_create_pronunciations(
        self, *, zip: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkCreatePronunciationsResponse]:
        """
        Upload multiple pronunciations at once. Each audio file in the ZIP becomes a pronunciation — the filename (without extension) is used as the word.

        Parameters
        ----------
        zip : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkCreatePronunciationsResponse]
            Bulk creation result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pronunciations/bulk",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={},
            files={
                "zip": zip,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkCreatePronunciationsResponse,
                    parse_obj_as(
                        type_=BulkCreatePronunciationsResponse,
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

    async def get_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPronunciationResponse]:
        """
        Retrieve a single custom pronunciation by UUID

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPronunciationResponse]
            Pronunciation details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPronunciationResponse,
                    parse_obj_as(
                        type_=GetPronunciationResponse,
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

    async def delete_pronunciation(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeletePronunciationResponse]:
        """
        Permanently remove a custom pronunciation. Takes effect immediately.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletePronunciationResponse]
            Pronunciation deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePronunciationResponse,
                    parse_obj_as(
                        type_=DeletePronunciationResponse,
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

    async def update_pronunciation(
        self, uuid_: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdatePronunciationResponse]:
        """
        Enable or disable a pronunciation without deleting it. Inactive pronunciations are not used during synthesis.

        Parameters
        ----------
        uuid_ : str

        active : bool
            Set to false to disable, true to re-enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdatePronunciationResponse]
            Pronunciation updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pronunciations/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "active": active,
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
                    UpdatePronunciationResponse,
                    parse_obj_as(
                        type_=UpdatePronunciationResponse,
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
