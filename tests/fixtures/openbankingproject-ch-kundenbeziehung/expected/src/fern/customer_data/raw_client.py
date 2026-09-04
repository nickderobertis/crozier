

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.basic_customer_data import BasicCustomerData
from ..types.customer_check_response import CustomerCheckResponse
from ..types.customer_data_response import CustomerDataResponse
from ..types.error_response import ErrorResponse
from ..types.full_customer_dataset import FullCustomerDataset
from .types.customer_data_request_purpose import CustomerDataRequestPurpose
from .types.customer_data_request_requested_modules_item import CustomerDataRequestRequestedModulesItem
from .types.full_data_request_purpose import FullDataRequestPurpose
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCustomerDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_customer(
        self,
        *,
        shared_customer_hash: str,
        basic_data: BasicCustomerData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomerCheckResponse]:
        """
        Prüft ob ein Kunde bereits bei einer Institution identifiziert wurde (MVP Identifikation)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash der Grunddaten für Matching

        basic_data : BasicCustomerData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomerCheckResponse]
            Kunde erfolgreich geprüft
        """
        _response = self._client_wrapper.httpx_client.request(
            "customer/check",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "basicData": convert_and_respect_annotation_metadata(
                    object_=basic_data, annotation=BasicCustomerData, direction="write"
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
                    CustomerCheckResponse,
                    parse_obj_as(
                        type_=CustomerCheckResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def request_full_customer_data(
        self,
        *,
        shared_customer_hash: str,
        purpose: FullDataRequestPurpose,
        consent_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FullCustomerDataset]:
        """
        Fordert das vollständige Kundendatenset an (erfordert gültigen Consent)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        purpose : FullDataRequestPurpose

        consent_token : str
            JWT-Token mit Consent-Nachweis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FullCustomerDataset]
            Kundendaten erfolgreich übertragen
        """
        _response = self._client_wrapper.httpx_client.request(
            "customer/fullRequest",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "purpose": purpose,
                "consentToken": consent_token,
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
                    FullCustomerDataset,
                    parse_obj_as(
                        type_=FullCustomerDataset,
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

    def get_customer_data(
        self,
        *,
        shared_customer_hash: str,
        requested_modules: typing.Sequence[CustomerDataRequestRequestedModulesItem],
        consent_token: str,
        purpose: typing.Optional[CustomerDataRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomerDataResponse]:
        """
        Ruft spezifische Kundendatenmodule basierend auf gewährtem Consent ab

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        requested_modules : typing.Sequence[CustomerDataRequestRequestedModulesItem]
            Angeforderte Datenbausteine

        consent_token : str
            JWT-Token mit Consent-Nachweis

        purpose : typing.Optional[CustomerDataRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomerDataResponse]
            Kundendaten erfolgreich abgerufen
        """
        _response = self._client_wrapper.httpx_client.request(
            "customer/data",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "requestedModules": requested_modules,
                "consentToken": consent_token,
                "purpose": purpose,
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
                    CustomerDataResponse,
                    parse_obj_as(
                        type_=CustomerDataResponse,
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


class AsyncRawCustomerDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_customer(
        self,
        *,
        shared_customer_hash: str,
        basic_data: BasicCustomerData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomerCheckResponse]:
        """
        Prüft ob ein Kunde bereits bei einer Institution identifiziert wurde (MVP Identifikation)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash der Grunddaten für Matching

        basic_data : BasicCustomerData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomerCheckResponse]
            Kunde erfolgreich geprüft
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customer/check",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "basicData": convert_and_respect_annotation_metadata(
                    object_=basic_data, annotation=BasicCustomerData, direction="write"
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
                    CustomerCheckResponse,
                    parse_obj_as(
                        type_=CustomerCheckResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def request_full_customer_data(
        self,
        *,
        shared_customer_hash: str,
        purpose: FullDataRequestPurpose,
        consent_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FullCustomerDataset]:
        """
        Fordert das vollständige Kundendatenset an (erfordert gültigen Consent)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        purpose : FullDataRequestPurpose

        consent_token : str
            JWT-Token mit Consent-Nachweis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FullCustomerDataset]
            Kundendaten erfolgreich übertragen
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customer/fullRequest",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "purpose": purpose,
                "consentToken": consent_token,
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
                    FullCustomerDataset,
                    parse_obj_as(
                        type_=FullCustomerDataset,
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

    async def get_customer_data(
        self,
        *,
        shared_customer_hash: str,
        requested_modules: typing.Sequence[CustomerDataRequestRequestedModulesItem],
        consent_token: str,
        purpose: typing.Optional[CustomerDataRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomerDataResponse]:
        """
        Ruft spezifische Kundendatenmodule basierend auf gewährtem Consent ab

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        requested_modules : typing.Sequence[CustomerDataRequestRequestedModulesItem]
            Angeforderte Datenbausteine

        consent_token : str
            JWT-Token mit Consent-Nachweis

        purpose : typing.Optional[CustomerDataRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomerDataResponse]
            Kundendaten erfolgreich abgerufen
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customer/data",
            method="POST",
            json={
                "sharedCustomerHash": shared_customer_hash,
                "requestedModules": requested_modules,
                "consentToken": consent_token,
                "purpose": purpose,
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
                    CustomerDataResponse,
                    parse_obj_as(
                        type_=CustomerDataResponse,
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
