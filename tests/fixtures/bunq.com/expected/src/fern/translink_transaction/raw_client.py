

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
from ..types.payment import Payment
from ..types.translink_transaction_create import TranslinkTransactionCreate
from ..types.translink_transaction_listing import TranslinkTransactionListing
from ..types.translink_transaction_read import TranslinkTransactionRead
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranslinkTransactionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_translink_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TranslinkTransactionListing]]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TranslinkTransactionListing]]
            Used to create translink transactions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TranslinkTransactionListing],
                    parse_obj_as(
                        type_=typing.List[TranslinkTransactionListing],
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

    def create_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        description: str,
        payments: typing.Sequence[Payment],
        reference: str,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TranslinkTransactionCreate]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        description : str
            Description of the payment request.

        payments : typing.Sequence[Payment]
            The list of payments we want to send in a single transaction.

        reference : str
            The request reference.

        type : str
            Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TranslinkTransactionCreate]
            Used to create translink transactions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction",
            method="POST",
            json={
                "description": description,
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[Payment], direction="write"
                ),
                "reference": reference,
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
                    TranslinkTransactionCreate,
                    parse_obj_as(
                        type_=TranslinkTransactionCreate,
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

    def read_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TranslinkTransactionRead]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TranslinkTransactionRead]
            Used to create translink transactions.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranslinkTransactionRead,
                    parse_obj_as(
                        type_=TranslinkTransactionRead,
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


class AsyncRawTranslinkTransactionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_translink_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TranslinkTransactionListing]]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TranslinkTransactionListing]]
            Used to create translink transactions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TranslinkTransactionListing],
                    parse_obj_as(
                        type_=typing.List[TranslinkTransactionListing],
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

    async def create_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        description: str,
        payments: typing.Sequence[Payment],
        reference: str,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TranslinkTransactionCreate]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        description : str
            Description of the payment request.

        payments : typing.Sequence[Payment]
            The list of payments we want to send in a single transaction.

        reference : str
            The request reference.

        type : str
            Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TranslinkTransactionCreate]
            Used to create translink transactions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction",
            method="POST",
            json={
                "description": description,
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[Payment], direction="write"
                ),
                "reference": reference,
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
                    TranslinkTransactionCreate,
                    parse_obj_as(
                        type_=TranslinkTransactionCreate,
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

    async def read_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TranslinkTransactionRead]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TranslinkTransactionRead]
            Used to create translink transactions.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/translink-transaction/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranslinkTransactionRead,
                    parse_obj_as(
                        type_=TranslinkTransactionRead,
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
