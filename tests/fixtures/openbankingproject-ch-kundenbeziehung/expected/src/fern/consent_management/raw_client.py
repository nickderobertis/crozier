

import datetime as dt
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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.consent_response import ConsentResponse
from ..types.consent_status import ConsentStatus
from ..types.data_category import DataCategory
from ..types.error_response import ErrorResponse
from .types.consent_request_customer_contact_method import ConsentRequestCustomerContactMethod
from .types.consent_request_purpose import ConsentRequestPurpose
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConsentManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_consent(
        self,
        *,
        customer_id: str,
        requesting_institution: str,
        data_categories: typing.Sequence[DataCategory],
        purpose: ConsentRequestPurpose,
        expiry_date: dt.datetime,
        providing_institution: typing.Optional[str] = OMIT,
        customer_contact_method: typing.Optional[ConsentRequestCustomerContactMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConsentResponse]:
        """
        Initiiert einen Consent-Flow für Datenaustausch zwischen Institutionen

        Parameters
        ----------
        customer_id : str
            Eindeutige Kunden-ID (sharedCustomerHash)

        requesting_institution : str
            Institution die Daten anfordert

        data_categories : typing.Sequence[DataCategory]
            Angeforderte Datenkategorien

        purpose : ConsentRequestPurpose
            Zweck der Datenverwendung

        expiry_date : dt.datetime
            Ablaufzeitpunkt des Consents

        providing_institution : typing.Optional[str]
            Institution die Daten bereitstellt

        customer_contact_method : typing.Optional[ConsentRequestCustomerContactMethod]
            Bevorzugter Kontaktweg für Consent-Bestätigung

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsentResponse]
            Consent erfolgreich erstellt
        """
        _response = self._client_wrapper.httpx_client.request(
            "consent",
            method="POST",
            json={
                "customerId": customer_id,
                "requestingInstitution": requesting_institution,
                "providingInstitution": providing_institution,
                "dataCategories": data_categories,
                "purpose": purpose,
                "expiryDate": expiry_date,
                "customerContactMethod": customer_contact_method,
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
                    ConsentResponse,
                    parse_obj_as(
                        type_=ConsentResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_consent_status(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConsentStatus]:
        """
        Ruft den aktuellen Status eines Consent-Requests ab

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsentStatus]
            Consent-Status erfolgreich abgerufen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consent/{encode_path_param(consent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsentStatus,
                    parse_obj_as(
                        type_=ConsentStatus,
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

    def revoke_consent(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Widerruft einen bestehenden Consent

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consent/{encode_path_param(consent_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawConsentManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_consent(
        self,
        *,
        customer_id: str,
        requesting_institution: str,
        data_categories: typing.Sequence[DataCategory],
        purpose: ConsentRequestPurpose,
        expiry_date: dt.datetime,
        providing_institution: typing.Optional[str] = OMIT,
        customer_contact_method: typing.Optional[ConsentRequestCustomerContactMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConsentResponse]:
        """
        Initiiert einen Consent-Flow für Datenaustausch zwischen Institutionen

        Parameters
        ----------
        customer_id : str
            Eindeutige Kunden-ID (sharedCustomerHash)

        requesting_institution : str
            Institution die Daten anfordert

        data_categories : typing.Sequence[DataCategory]
            Angeforderte Datenkategorien

        purpose : ConsentRequestPurpose
            Zweck der Datenverwendung

        expiry_date : dt.datetime
            Ablaufzeitpunkt des Consents

        providing_institution : typing.Optional[str]
            Institution die Daten bereitstellt

        customer_contact_method : typing.Optional[ConsentRequestCustomerContactMethod]
            Bevorzugter Kontaktweg für Consent-Bestätigung

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsentResponse]
            Consent erfolgreich erstellt
        """
        _response = await self._client_wrapper.httpx_client.request(
            "consent",
            method="POST",
            json={
                "customerId": customer_id,
                "requestingInstitution": requesting_institution,
                "providingInstitution": providing_institution,
                "dataCategories": data_categories,
                "purpose": purpose,
                "expiryDate": expiry_date,
                "customerContactMethod": customer_contact_method,
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
                    ConsentResponse,
                    parse_obj_as(
                        type_=ConsentResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_consent_status(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConsentStatus]:
        """
        Ruft den aktuellen Status eines Consent-Requests ab

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsentStatus]
            Consent-Status erfolgreich abgerufen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consent/{encode_path_param(consent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsentStatus,
                    parse_obj_as(
                        type_=ConsentStatus,
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

    async def revoke_consent(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Widerruft einen bestehenden Consent

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consent/{encode_path_param(consent_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
