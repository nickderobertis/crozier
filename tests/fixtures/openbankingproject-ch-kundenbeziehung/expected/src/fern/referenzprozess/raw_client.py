

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
from ..errors.bad_request_error import BadRequestError
from ..types.process_initialization_response import ProcessInitializationResponse
from ..types.process_status import ProcessStatus
from ..types.process_step_response import ProcessStepResponse
from .types.process_initialization_request_customer_context import ProcessInitializationRequestCustomerContext
from .types.process_initialization_request_industry import ProcessInitializationRequestIndustry
from .types.process_initialization_request_process_configuration import ProcessInitializationRequestProcessConfiguration
from .types.process_initialization_request_use_case import ProcessInitializationRequestUseCase
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawReferenzprozessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def initialize_process(
        self,
        *,
        industry: ProcessInitializationRequestIndustry,
        use_case: ProcessInitializationRequestUseCase,
        customer_context: ProcessInitializationRequestCustomerContext,
        process_configuration: typing.Optional[ProcessInitializationRequestProcessConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcessInitializationResponse]:
        """
        Initiiert den universellen 10-Stufen-Referenzprozess für Customer Onboarding

        Parameters
        ----------
        industry : ProcessInitializationRequestIndustry
            Ziel-Ecosystem für den Prozess

        use_case : ProcessInitializationRequestUseCase
            Spezifischer Use Case

        customer_context : ProcessInitializationRequestCustomerContext

        process_configuration : typing.Optional[ProcessInitializationRequestProcessConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProcessInitializationResponse]
            Referenzprozess erfolgreich initialisiert
        """
        _response = self._client_wrapper.httpx_client.request(
            "process/initialize",
            method="POST",
            json={
                "industry": industry,
                "useCase": use_case,
                "customerContext": convert_and_respect_annotation_metadata(
                    object_=customer_context, annotation=ProcessInitializationRequestCustomerContext, direction="write"
                ),
                "processConfiguration": convert_and_respect_annotation_metadata(
                    object_=process_configuration,
                    annotation=ProcessInitializationRequestProcessConfiguration,
                    direction="write",
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
                    ProcessInitializationResponse,
                    parse_obj_as(
                        type_=ProcessInitializationResponse,
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

    def execute_process_step(
        self,
        process_id: str,
        step_number: int,
        *,
        step_data: typing.Dict[str, typing.Any],
        skip_to_step: typing.Optional[int] = OMIT,
        customer_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcessStepResponse]:
        """
        Führt einen spezifischen Schritt (1-10) des Referenzprozesses aus

        Parameters
        ----------
        process_id : str

        step_number : int

        step_data : typing.Dict[str, typing.Any]
            Step-spezifische Daten

        skip_to_step : typing.Optional[int]

        customer_consent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProcessStepResponse]
            Prozessschritt erfolgreich ausgeführt
        """
        _response = self._client_wrapper.httpx_client.request(
            f"process/{encode_path_param(process_id)}/step/{encode_path_param(step_number)}",
            method="POST",
            json={
                "stepData": step_data,
                "skipToStep": skip_to_step,
                "customerConsent": customer_consent,
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
                    ProcessStepResponse,
                    parse_obj_as(
                        type_=ProcessStepResponse,
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

    def get_process_status(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProcessStatus]:
        """
        Ruft den aktuellen Status und Fortschritt des Referenzprozesses ab

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProcessStatus]
            Prozess-Status erfolgreich abgerufen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"process/{encode_path_param(process_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProcessStatus,
                    parse_obj_as(
                        type_=ProcessStatus,
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


class AsyncRawReferenzprozessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def initialize_process(
        self,
        *,
        industry: ProcessInitializationRequestIndustry,
        use_case: ProcessInitializationRequestUseCase,
        customer_context: ProcessInitializationRequestCustomerContext,
        process_configuration: typing.Optional[ProcessInitializationRequestProcessConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProcessInitializationResponse]:
        """
        Initiiert den universellen 10-Stufen-Referenzprozess für Customer Onboarding

        Parameters
        ----------
        industry : ProcessInitializationRequestIndustry
            Ziel-Ecosystem für den Prozess

        use_case : ProcessInitializationRequestUseCase
            Spezifischer Use Case

        customer_context : ProcessInitializationRequestCustomerContext

        process_configuration : typing.Optional[ProcessInitializationRequestProcessConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProcessInitializationResponse]
            Referenzprozess erfolgreich initialisiert
        """
        _response = await self._client_wrapper.httpx_client.request(
            "process/initialize",
            method="POST",
            json={
                "industry": industry,
                "useCase": use_case,
                "customerContext": convert_and_respect_annotation_metadata(
                    object_=customer_context, annotation=ProcessInitializationRequestCustomerContext, direction="write"
                ),
                "processConfiguration": convert_and_respect_annotation_metadata(
                    object_=process_configuration,
                    annotation=ProcessInitializationRequestProcessConfiguration,
                    direction="write",
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
                    ProcessInitializationResponse,
                    parse_obj_as(
                        type_=ProcessInitializationResponse,
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

    async def execute_process_step(
        self,
        process_id: str,
        step_number: int,
        *,
        step_data: typing.Dict[str, typing.Any],
        skip_to_step: typing.Optional[int] = OMIT,
        customer_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProcessStepResponse]:
        """
        Führt einen spezifischen Schritt (1-10) des Referenzprozesses aus

        Parameters
        ----------
        process_id : str

        step_number : int

        step_data : typing.Dict[str, typing.Any]
            Step-spezifische Daten

        skip_to_step : typing.Optional[int]

        customer_consent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProcessStepResponse]
            Prozessschritt erfolgreich ausgeführt
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"process/{encode_path_param(process_id)}/step/{encode_path_param(step_number)}",
            method="POST",
            json={
                "stepData": step_data,
                "skipToStep": skip_to_step,
                "customerConsent": customer_consent,
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
                    ProcessStepResponse,
                    parse_obj_as(
                        type_=ProcessStepResponse,
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

    async def get_process_status(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProcessStatus]:
        """
        Ruft den aktuellen Status und Fortschritt des Referenzprozesses ab

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProcessStatus]
            Prozess-Status erfolgreich abgerufen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"process/{encode_path_param(process_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProcessStatus,
                    parse_obj_as(
                        type_=ProcessStatus,
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
