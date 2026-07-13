

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.transferwise_account_requirement_create import TransferwiseAccountRequirementCreate
from ..types.transferwise_account_requirement_listing import TransferwiseAccountRequirementListing
from ..types.transferwise_requirement_field import TransferwiseRequirementField


OMIT = typing.cast(typing.Any, ...)


class RawTransferwiseRecipientRequirementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TransferwiseAccountRequirementListing]]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TransferwiseAccountRequirementListing]]
            Used to determine the recipient account requirements for Transferwise transfers.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-recipient-requirement",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TransferwiseAccountRequirementListing],
                    parse_obj_as(
                        type_=typing.List[TransferwiseAccountRequirementListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_transferwise_recipient_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        name_account_holder: str,
        type: str,
        country: typing.Optional[str] = OMIT,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransferwiseAccountRequirementCreate]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        name_account_holder : str
            The name of the account holder.

        type : str
            The chosen recipient account type. The possible options are provided dynamically in the response endpoint.

        country : typing.Optional[str]
            The country of the receiving account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransferwiseAccountRequirementCreate]
            Used to determine the recipient account requirements for Transferwise transfers.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-recipient-requirement",
            method="POST",
            json={
                "country": country,
                "detail": convert_and_respect_annotation_metadata(
                    object_=detail, annotation=typing.Sequence[TransferwiseRequirementField], direction="write"
                ),
                "name_account_holder": name_account_holder,
                "type": type,
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
                    TransferwiseAccountRequirementCreate,
                    parse_obj_as(
                        type_=TransferwiseAccountRequirementCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTransferwiseRecipientRequirementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_transferwise_recipient_requirement_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TransferwiseAccountRequirementListing]]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TransferwiseAccountRequirementListing]]
            Used to determine the recipient account requirements for Transferwise transfers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-recipient-requirement",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TransferwiseAccountRequirementListing],
                    parse_obj_as(
                        type_=typing.List[TransferwiseAccountRequirementListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_transferwise_recipient_requirement_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        name_account_holder: str,
        type: str,
        country: typing.Optional[str] = OMIT,
        detail: typing.Optional[typing.Sequence[TransferwiseRequirementField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransferwiseAccountRequirementCreate]:
        """
        Used to determine the recipient account requirements for Transferwise transfers.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        name_account_holder : str
            The name of the account holder.

        type : str
            The chosen recipient account type. The possible options are provided dynamically in the response endpoint.

        country : typing.Optional[str]
            The country of the receiving account.

        detail : typing.Optional[typing.Sequence[TransferwiseRequirementField]]
            The fields which were specified as "required" and have since been filled by the user. Always provide the full list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransferwiseAccountRequirementCreate]
            Used to determine the recipient account requirements for Transferwise transfers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/transferwise-quote/{jsonable_encoder(transferwise_quote_id)}/transferwise-recipient-requirement",
            method="POST",
            json={
                "country": country,
                "detail": convert_and_respect_annotation_metadata(
                    object_=detail, annotation=typing.Sequence[TransferwiseRequirementField], direction="write"
                ),
                "name_account_holder": name_account_holder,
                "type": type,
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
                    TransferwiseAccountRequirementCreate,
                    parse_obj_as(
                        type_=TransferwiseAccountRequirementCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
