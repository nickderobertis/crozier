

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
from ..errors.not_found_error import NotFoundError
from ..types.biometric_data import BiometricData
from ..types.document_data import DocumentData
from ..types.identification_response import IdentificationResponse
from ..types.identification_status_response import IdentificationStatusResponse
from .types.identification_request_identification_type import IdentificationRequestIdentificationType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIdentificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_identification_status(
        self, verification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IdentificationStatusResponse]:
        """
        Ruft den Status einer bestehenden Identifikation ab (für UC2 Re-identification)

        Parameters
        ----------
        verification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IdentificationStatusResponse]
            Identifikations-Status erfolgreich abgerufen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"identification/{encode_path_param(verification_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IdentificationStatusResponse,
                    parse_obj_as(
                        type_=IdentificationStatusResponse,
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

    def verify_identification(
        self,
        *,
        customer_id: str,
        identification_type: IdentificationRequestIdentificationType,
        document_data: typing.Optional[DocumentData] = OMIT,
        biometric_data: typing.Optional[BiometricData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IdentificationResponse]:
        """
        Verifiziert Identifikationsdaten gegen E-ID oder andere Quellen

        Parameters
        ----------
        customer_id : str

        identification_type : IdentificationRequestIdentificationType

        document_data : typing.Optional[DocumentData]

        biometric_data : typing.Optional[BiometricData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IdentificationResponse]
            Identifikation erfolgreich verifiziert
        """
        _response = self._client_wrapper.httpx_client.request(
            "identification/verify",
            method="POST",
            json={
                "customerId": customer_id,
                "identificationType": identification_type,
                "documentData": convert_and_respect_annotation_metadata(
                    object_=document_data, annotation=DocumentData, direction="write"
                ),
                "biometricData": convert_and_respect_annotation_metadata(
                    object_=biometric_data, annotation=BiometricData, direction="write"
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
                    IdentificationResponse,
                    parse_obj_as(
                        type_=IdentificationResponse,
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


class AsyncRawIdentificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_identification_status(
        self, verification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IdentificationStatusResponse]:
        """
        Ruft den Status einer bestehenden Identifikation ab (für UC2 Re-identification)

        Parameters
        ----------
        verification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IdentificationStatusResponse]
            Identifikations-Status erfolgreich abgerufen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"identification/{encode_path_param(verification_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IdentificationStatusResponse,
                    parse_obj_as(
                        type_=IdentificationStatusResponse,
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

    async def verify_identification(
        self,
        *,
        customer_id: str,
        identification_type: IdentificationRequestIdentificationType,
        document_data: typing.Optional[DocumentData] = OMIT,
        biometric_data: typing.Optional[BiometricData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IdentificationResponse]:
        """
        Verifiziert Identifikationsdaten gegen E-ID oder andere Quellen

        Parameters
        ----------
        customer_id : str

        identification_type : IdentificationRequestIdentificationType

        document_data : typing.Optional[DocumentData]

        biometric_data : typing.Optional[BiometricData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IdentificationResponse]
            Identifikation erfolgreich verifiziert
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identification/verify",
            method="POST",
            json={
                "customerId": customer_id,
                "identificationType": identification_type,
                "documentData": convert_and_respect_annotation_metadata(
                    object_=document_data, annotation=DocumentData, direction="write"
                ),
                "biometricData": convert_and_respect_annotation_metadata(
                    object_=biometric_data, annotation=BiometricData, direction="write"
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
                    IdentificationResponse,
                    parse_obj_as(
                        type_=IdentificationResponse,
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
