

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.create_merchant_response import CreateMerchantResponse
from ..types.delete_merchant_credentials_response import DeleteMerchantCredentialsResponse
from ..types.delete_merchant_response import DeleteMerchantResponse
from ..types.error_model import ErrorModel
from ..types.get_merchant_credentials_response import GetMerchantCredentialsResponse
from ..types.get_merchant_response import GetMerchantResponse
from ..types.item import Item
from ..types.set_merchant_credentials_response import SetMerchantCredentialsResponse
from ..types.update_merchant_response import UpdateMerchantResponse
from ..types.update_struct import UpdateStruct
from .types.create_merchant_request_merchant_type import CreateMerchantRequestMerchantType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMerchantClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_merchant(
        self,
        *,
        merchant_name: str,
        contact_first: typing.Optional[str] = OMIT,
        contact_last: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        send_taxcloud_invite: typing.Optional[bool] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        merchant_type: typing.Optional[CreateMerchantRequestMerchantType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMerchantResponse]:
        """
        Creates a new merchant under the authenticated account. Requires X-API-KEY header.

        Parameters
        ----------
        merchant_name : str
            Legal or trading name of the merchant business. Required; must be 1–255 characters.

        contact_first : typing.Optional[str]
            First name of the merchant's primary contact. Optional.

        contact_last : typing.Optional[str]
            Last name of the merchant's primary contact. Optional.

        contact_email : typing.Optional[str]
            Email address of the merchant's primary contact; used for TaxCloud invitations and notifications. Optional.

        send_taxcloud_invite : typing.Optional[bool]
            Sends invite to set up and connect a TaxCloud account to a merchant who does not already use TaxCloud. To connect a TaxCloud account for a merchant who already uses TaxCloud, use the "Set Merchant Credentials" function. Ignored when merchant_type is 'self-managed'.

        reference_id : typing.Optional[str]
            The ID you use in your own system to identify this merchant.

        merchant_type : typing.Optional[CreateMerchantRequestMerchantType]
            The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMerchantResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/create",
            method="POST",
            json={
                "merchantName": merchant_name,
                "contactFirst": contact_first,
                "contactLast": contact_last,
                "contactEmail": contact_email,
                "sendTaxcloudInvite": send_taxcloud_invite,
                "referenceId": reference_id,
                "merchant_type": merchant_type,
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
                    CreateMerchantResponse,
                    parse_obj_as(
                        type_=CreateMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def delete_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMerchantCredentialsResponse]:
        """
        Deletes TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being deleted. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMerchantCredentialsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/credentials/delete",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    DeleteMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=DeleteMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def get_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMerchantCredentialsResponse]:
        """
        Retrieves TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being retrieved. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMerchantCredentialsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/credentials/get",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    GetMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=GetMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def set_merchant_credentials(
        self,
        *,
        api_key: str,
        connection_id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SetMerchantCredentialsResponse]:
        """
        Sets or updates TaxCloud credentials for a merchant. Credentials are encrypted at rest with AES-256-GCM. On success an asynchronous webhook notification is sent to the configured endpoint.

        Parameters
        ----------
        api_key : str
            TaxCloud API key to associate with the merchant. Stored encrypted at rest with AES-256-GCM.

        connection_id : str
            TaxCloud connection ID that pairs with the API key to identify the merchant's TaxCloud integration.

        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being set. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SetMerchantCredentialsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/credentials/set",
            method="POST",
            json={
                "apiKey": api_key,
                "connectionId": connection_id,
                "merchantId": merchant_id,
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
                    SetMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=SetMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def delete_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMerchantResponse]:
        """
        Soft-deletes a merchant by setting deleted_at to now. The caller must own the merchant. If the merchant is not owned by the caller, or is already soft-deleted (deleted_at <= now), the ownership check returns 403. A 404 is only reachable in a rare race after the ownership check passes.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to soft-delete. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMerchantResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/delete",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    DeleteMerchantResponse,
                    parse_obj_as(
                        type_=DeleteMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def get_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMerchantResponse]:
        """
        Returns a single merchant by UUID. The caller must own the merchant. Cross-account reads are blocked. Soft-deleted merchants (deleted_at <= now) are treated as non-existent and return 404.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to retrieve. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMerchantResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/get",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    GetMerchantResponse,
                    parse_obj_as(
                        type_=GetMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def list_merchants(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[Item]]]:
        """
        Returns every active merchant owned by the calling account. A merchant is considered active when its deleted_at is NULL or set to a future date. Soft-deleted merchants (deleted_at <= now) are excluded from results.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[Item]]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[Item]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[Item]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    def update_merchant(
        self, *, merchant_id: str, update: UpdateStruct, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateMerchantResponse]:
        """
        Updates an existing merchant. The caller must own the merchant. Cross-account modification is blocked. Soft-deleted merchants (deleted_at <= now), and merchants owned by another account, fail the ownership check and return 403.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to update. The merchant must be owned by the calling account.

        update : UpdateStruct
            New field values for the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMerchantResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "merchant/update",
            method="POST",
            json={
                "merchantId": merchant_id,
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=UpdateStruct, direction="write"
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
                    UpdateMerchantResponse,
                    parse_obj_as(
                        type_=UpdateMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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


class AsyncRawMerchantClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_merchant(
        self,
        *,
        merchant_name: str,
        contact_first: typing.Optional[str] = OMIT,
        contact_last: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        send_taxcloud_invite: typing.Optional[bool] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        merchant_type: typing.Optional[CreateMerchantRequestMerchantType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMerchantResponse]:
        """
        Creates a new merchant under the authenticated account. Requires X-API-KEY header.

        Parameters
        ----------
        merchant_name : str
            Legal or trading name of the merchant business. Required; must be 1–255 characters.

        contact_first : typing.Optional[str]
            First name of the merchant's primary contact. Optional.

        contact_last : typing.Optional[str]
            Last name of the merchant's primary contact. Optional.

        contact_email : typing.Optional[str]
            Email address of the merchant's primary contact; used for TaxCloud invitations and notifications. Optional.

        send_taxcloud_invite : typing.Optional[bool]
            Sends invite to set up and connect a TaxCloud account to a merchant who does not already use TaxCloud. To connect a TaxCloud account for a merchant who already uses TaxCloud, use the "Set Merchant Credentials" function. Ignored when merchant_type is 'self-managed'.

        reference_id : typing.Optional[str]
            The ID you use in your own system to identify this merchant.

        merchant_type : typing.Optional[CreateMerchantRequestMerchantType]
            The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMerchantResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/create",
            method="POST",
            json={
                "merchantName": merchant_name,
                "contactFirst": contact_first,
                "contactLast": contact_last,
                "contactEmail": contact_email,
                "sendTaxcloudInvite": send_taxcloud_invite,
                "referenceId": reference_id,
                "merchant_type": merchant_type,
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
                    CreateMerchantResponse,
                    parse_obj_as(
                        type_=CreateMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def delete_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMerchantCredentialsResponse]:
        """
        Deletes TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being deleted. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMerchantCredentialsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/credentials/delete",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    DeleteMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=DeleteMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def get_merchant_credentials(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMerchantCredentialsResponse]:
        """
        Retrieves TaxCloud credentials for a merchant. The caller must own the merchant.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being retrieved. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMerchantCredentialsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/credentials/get",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    GetMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=GetMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def set_merchant_credentials(
        self,
        *,
        api_key: str,
        connection_id: str,
        merchant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SetMerchantCredentialsResponse]:
        """
        Sets or updates TaxCloud credentials for a merchant. Credentials are encrypted at rest with AES-256-GCM. On success an asynchronous webhook notification is sent to the configured endpoint.

        Parameters
        ----------
        api_key : str
            TaxCloud API key to associate with the merchant. Stored encrypted at rest with AES-256-GCM.

        connection_id : str
            TaxCloud connection ID that pairs with the API key to identify the merchant's TaxCloud integration.

        merchant_id : str
            UUID of the merchant whose TaxCloud credentials are being set. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SetMerchantCredentialsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/credentials/set",
            method="POST",
            json={
                "apiKey": api_key,
                "connectionId": connection_id,
                "merchantId": merchant_id,
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
                    SetMerchantCredentialsResponse,
                    parse_obj_as(
                        type_=SetMerchantCredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def delete_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMerchantResponse]:
        """
        Soft-deletes a merchant by setting deleted_at to now. The caller must own the merchant. If the merchant is not owned by the caller, or is already soft-deleted (deleted_at <= now), the ownership check returns 403. A 404 is only reachable in a rare race after the ownership check passes.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to soft-delete. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMerchantResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/delete",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    DeleteMerchantResponse,
                    parse_obj_as(
                        type_=DeleteMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def get_merchant(
        self, *, merchant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMerchantResponse]:
        """
        Returns a single merchant by UUID. The caller must own the merchant. Cross-account reads are blocked. Soft-deleted merchants (deleted_at <= now) are treated as non-existent and return 404.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to retrieve. The merchant must be owned by the calling account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMerchantResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/get",
            method="POST",
            json={
                "merchantId": merchant_id,
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
                    GetMerchantResponse,
                    parse_obj_as(
                        type_=GetMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def list_merchants(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[Item]]]:
        """
        Returns every active merchant owned by the calling account. A merchant is considered active when its deleted_at is NULL or set to a future date. Soft-deleted merchants (deleted_at <= now) are excluded from results.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[Item]]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[Item]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[Item]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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

    async def update_merchant(
        self, *, merchant_id: str, update: UpdateStruct, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateMerchantResponse]:
        """
        Updates an existing merchant. The caller must own the merchant. Cross-account modification is blocked. Soft-deleted merchants (deleted_at <= now), and merchants owned by another account, fail the ownership check and return 403.

        Parameters
        ----------
        merchant_id : str
            UUID of the merchant to update. The merchant must be owned by the calling account.

        update : UpdateStruct
            New field values for the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMerchantResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "merchant/update",
            method="POST",
            json={
                "merchantId": merchant_id,
                "update": convert_and_respect_annotation_metadata(
                    object_=update, annotation=UpdateStruct, direction="write"
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
                    UpdateMerchantResponse,
                    parse_obj_as(
                        type_=UpdateMerchantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorModel,
                        parse_obj_as(
                            type_=ErrorModel,
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
