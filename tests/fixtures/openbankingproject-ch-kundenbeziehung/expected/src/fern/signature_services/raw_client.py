

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
from ..types.document_to_sign import DocumentToSign
from ..types.signature_response import SignatureResponse
from ..types.signature_status import SignatureStatus
from .types.signature_request_notification_method import SignatureRequestNotificationMethod
from .types.signature_request_signature_type import SignatureRequestSignatureType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSignatureServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def initiate_signature(
        self,
        *,
        customer_id: str,
        documents: typing.Sequence[DocumentToSign],
        signature_type: SignatureRequestSignatureType,
        notification_method: typing.Optional[SignatureRequestNotificationMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SignatureResponse]:
        """
        Startet einen QES- oder eSignatur-Prozess

        Parameters
        ----------
        customer_id : str

        documents : typing.Sequence[DocumentToSign]

        signature_type : SignatureRequestSignatureType

        notification_method : typing.Optional[SignatureRequestNotificationMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignatureResponse]
            Signatur-Prozess erfolgreich initiiert
        """
        _response = self._client_wrapper.httpx_client.request(
            "signature/initiate",
            method="POST",
            json={
                "customerId": customer_id,
                "documents": convert_and_respect_annotation_metadata(
                    object_=documents, annotation=typing.Sequence[DocumentToSign], direction="write"
                ),
                "signatureType": signature_type,
                "notificationMethod": notification_method,
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
                    SignatureResponse,
                    parse_obj_as(
                        type_=SignatureResponse,
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

    def get_signature_status(
        self, signature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SignatureStatus]:
        """
        Ruft den Status eines Signatur-Prozesses ab

        Parameters
        ----------
        signature_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignatureStatus]
            Signatur-Status erfolgreich abgerufen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"signature/{encode_path_param(signature_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SignatureStatus,
                    parse_obj_as(
                        type_=SignatureStatus,
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


class AsyncRawSignatureServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def initiate_signature(
        self,
        *,
        customer_id: str,
        documents: typing.Sequence[DocumentToSign],
        signature_type: SignatureRequestSignatureType,
        notification_method: typing.Optional[SignatureRequestNotificationMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SignatureResponse]:
        """
        Startet einen QES- oder eSignatur-Prozess

        Parameters
        ----------
        customer_id : str

        documents : typing.Sequence[DocumentToSign]

        signature_type : SignatureRequestSignatureType

        notification_method : typing.Optional[SignatureRequestNotificationMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignatureResponse]
            Signatur-Prozess erfolgreich initiiert
        """
        _response = await self._client_wrapper.httpx_client.request(
            "signature/initiate",
            method="POST",
            json={
                "customerId": customer_id,
                "documents": convert_and_respect_annotation_metadata(
                    object_=documents, annotation=typing.Sequence[DocumentToSign], direction="write"
                ),
                "signatureType": signature_type,
                "notificationMethod": notification_method,
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
                    SignatureResponse,
                    parse_obj_as(
                        type_=SignatureResponse,
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

    async def get_signature_status(
        self, signature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SignatureStatus]:
        """
        Ruft den Status eines Signatur-Prozesses ab

        Parameters
        ----------
        signature_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignatureStatus]
            Signatur-Status erfolgreich abgerufen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"signature/{encode_path_param(signature_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SignatureStatus,
                    parse_obj_as(
                        type_=SignatureStatus,
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
