

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.practice_event import PracticeEvent
from ..types.practice_intent import PracticeIntent
from ..types.practice_service_metadata import PracticeServiceMetadata
from .types.create_insurance_product_request_coverage import CreateInsuranceProductRequestCoverage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPracticeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_service_metadata(
        self,
        practice_id: str,
        *,
        practice_service_metadata_create_practice_id: str,
        service_name: str,
        duration_minutes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PracticeServiceMetadata]:
        """
        Parameters
        ----------
        practice_id : str

        practice_service_metadata_create_practice_id : str

        service_name : str

        duration_minutes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PracticeServiceMetadata]
            The created metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/service-metadata",
            method="POST",
            json={
                "practice_id": practice_service_metadata_create_practice_id,
                "service_name": service_name,
                "duration_minutes": duration_minutes,
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
                    PracticeServiceMetadata,
                    parse_obj_as(
                        type_=PracticeServiceMetadata,
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

    def create_intent(
        self,
        practice_id: str,
        *,
        practice_intent_create_practice_id: str,
        intent: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PracticeIntent]:
        """
        Parameters
        ----------
        practice_id : str

        practice_intent_create_practice_id : str

        intent : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PracticeIntent]
            The created intent.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/intents",
            method="POST",
            json={
                "practice_id": practice_intent_create_practice_id,
                "intent": intent,
                "tags": tags,
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
                    PracticeIntent,
                    parse_obj_as(
                        type_=PracticeIntent,
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

    def create_insurance_product(
        self,
        practice_id: str,
        *,
        insurance_product_practice_id: str,
        coverage: typing.Optional[CreateInsuranceProductRequestCoverage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PracticeEvent]:
        """
        Parameters
        ----------
        practice_id : str

        insurance_product_practice_id : str

        coverage : typing.Optional[CreateInsuranceProductRequestCoverage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PracticeEvent]
            The created product's events.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/insurance-products",
            method="POST",
            json={
                "practice_id": insurance_product_practice_id,
                "coverage": convert_and_respect_annotation_metadata(
                    object_=coverage, annotation=CreateInsuranceProductRequestCoverage, direction="write"
                ),
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
                    PracticeEvent,
                    parse_obj_as(
                        type_=PracticeEvent,
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

    def create_note(
        self,
        practice_id: str,
        *,
        note_practice_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        practice_id : str

        note_practice_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/notes",
            method="POST",
            data={
                "practice_id": note_practice_id,
                "body": body,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPracticeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_service_metadata(
        self,
        practice_id: str,
        *,
        practice_service_metadata_create_practice_id: str,
        service_name: str,
        duration_minutes: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PracticeServiceMetadata]:
        """
        Parameters
        ----------
        practice_id : str

        practice_service_metadata_create_practice_id : str

        service_name : str

        duration_minutes : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PracticeServiceMetadata]
            The created metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/service-metadata",
            method="POST",
            json={
                "practice_id": practice_service_metadata_create_practice_id,
                "service_name": service_name,
                "duration_minutes": duration_minutes,
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
                    PracticeServiceMetadata,
                    parse_obj_as(
                        type_=PracticeServiceMetadata,
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

    async def create_intent(
        self,
        practice_id: str,
        *,
        practice_intent_create_practice_id: str,
        intent: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PracticeIntent]:
        """
        Parameters
        ----------
        practice_id : str

        practice_intent_create_practice_id : str

        intent : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PracticeIntent]
            The created intent.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/intents",
            method="POST",
            json={
                "practice_id": practice_intent_create_practice_id,
                "intent": intent,
                "tags": tags,
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
                    PracticeIntent,
                    parse_obj_as(
                        type_=PracticeIntent,
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

    async def create_insurance_product(
        self,
        practice_id: str,
        *,
        insurance_product_practice_id: str,
        coverage: typing.Optional[CreateInsuranceProductRequestCoverage] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PracticeEvent]:
        """
        Parameters
        ----------
        practice_id : str

        insurance_product_practice_id : str

        coverage : typing.Optional[CreateInsuranceProductRequestCoverage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PracticeEvent]
            The created product's events.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/insurance-products",
            method="POST",
            json={
                "practice_id": insurance_product_practice_id,
                "coverage": convert_and_respect_annotation_metadata(
                    object_=coverage, annotation=CreateInsuranceProductRequestCoverage, direction="write"
                ),
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
                    PracticeEvent,
                    parse_obj_as(
                        type_=PracticeEvent,
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

    async def create_note(
        self,
        practice_id: str,
        *,
        note_practice_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        practice_id : str

        note_practice_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"practice/{encode_path_param(practice_id)}/notes",
            method="POST",
            data={
                "practice_id": note_practice_id,
                "body": body,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
