

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
from ..types.payment_auto_allocate_create import PaymentAutoAllocateCreate
from ..types.payment_auto_allocate_definition import PaymentAutoAllocateDefinition
from ..types.payment_auto_allocate_delete import PaymentAutoAllocateDelete
from ..types.payment_auto_allocate_listing import PaymentAutoAllocateListing
from ..types.payment_auto_allocate_read import PaymentAutoAllocateRead
from ..types.payment_auto_allocate_update import PaymentAutoAllocateUpdate
from ..types.payment_auto_allocate_user_listing import PaymentAutoAllocateUserListing


OMIT = typing.cast(typing.Any, ...)


class RawPaymentAutoAllocateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_payment_auto_allocate_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PaymentAutoAllocateListing]]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PaymentAutoAllocateListing]]
            Manage a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentAutoAllocateListing],
                    parse_obj_as(
                        type_=typing.List[PaymentAutoAllocateListing],
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

    def create_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentAutoAllocateCreate]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentAutoAllocateCreate]
            Manage a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate",
            method="POST",
            json={
                "definition": convert_and_respect_annotation_metadata(
                    object_=definition, annotation=typing.Sequence[PaymentAutoAllocateDefinition], direction="write"
                ),
                "payment_id": payment_id,
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
                    PaymentAutoAllocateCreate,
                    parse_obj_as(
                        type_=PaymentAutoAllocateCreate,
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

    def read_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentAutoAllocateRead]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentAutoAllocateRead]
            Manage a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentAutoAllocateRead,
                    parse_obj_as(
                        type_=PaymentAutoAllocateRead,
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

    def update_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentAutoAllocateUpdate]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentAutoAllocateUpdate]
            Manage a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "definition": convert_and_respect_annotation_metadata(
                    object_=definition, annotation=typing.Sequence[PaymentAutoAllocateDefinition], direction="write"
                ),
                "payment_id": payment_id,
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
                    PaymentAutoAllocateUpdate,
                    parse_obj_as(
                        type_=PaymentAutoAllocateUpdate,
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

    def delete_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentAutoAllocateDelete]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentAutoAllocateDelete]
            Manage a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentAutoAllocateDelete,
                    parse_obj_as(
                        type_=PaymentAutoAllocateDelete,
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

    def list_all_payment_auto_allocate_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PaymentAutoAllocateUserListing]]:
        """
        List a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PaymentAutoAllocateUserListing]]
            List a users automatic payment auto allocated settings.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-auto-allocate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentAutoAllocateUserListing],
                    parse_obj_as(
                        type_=typing.List[PaymentAutoAllocateUserListing],
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


class AsyncRawPaymentAutoAllocateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_payment_auto_allocate_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PaymentAutoAllocateListing]]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PaymentAutoAllocateListing]]
            Manage a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentAutoAllocateListing],
                    parse_obj_as(
                        type_=typing.List[PaymentAutoAllocateListing],
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

    async def create_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentAutoAllocateCreate]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentAutoAllocateCreate]
            Manage a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate",
            method="POST",
            json={
                "definition": convert_and_respect_annotation_metadata(
                    object_=definition, annotation=typing.Sequence[PaymentAutoAllocateDefinition], direction="write"
                ),
                "payment_id": payment_id,
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
                    PaymentAutoAllocateCreate,
                    parse_obj_as(
                        type_=PaymentAutoAllocateCreate,
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

    async def read_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentAutoAllocateRead]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentAutoAllocateRead]
            Manage a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentAutoAllocateRead,
                    parse_obj_as(
                        type_=PaymentAutoAllocateRead,
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

    async def update_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        definition: typing.Sequence[PaymentAutoAllocateDefinition],
        payment_id: int,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentAutoAllocateUpdate]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        definition : typing.Sequence[PaymentAutoAllocateDefinition]
            The definition of how the money should be allocated.

        payment_id : int
            The payment that should be used to define the triggers for the payment auto allocate.

        type : str
            Whether a payment should be sorted ONCE or RECURRING.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentAutoAllocateUpdate]
            Manage a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "definition": convert_and_respect_annotation_metadata(
                    object_=definition, annotation=typing.Sequence[PaymentAutoAllocateDefinition], direction="write"
                ),
                "payment_id": payment_id,
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
                    PaymentAutoAllocateUpdate,
                    parse_obj_as(
                        type_=PaymentAutoAllocateUpdate,
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

    async def delete_payment_auto_allocate_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentAutoAllocateDelete]:
        """
        Manage a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentAutoAllocateDelete]
            Manage a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/payment-auto-allocate/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentAutoAllocateDelete,
                    parse_obj_as(
                        type_=PaymentAutoAllocateDelete,
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

    async def list_all_payment_auto_allocate_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PaymentAutoAllocateUserListing]]:
        """
        List a users automatic payment auto allocated settings.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PaymentAutoAllocateUserListing]]
            List a users automatic payment auto allocated settings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-auto-allocate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentAutoAllocateUserListing],
                    parse_obj_as(
                        type_=typing.List[PaymentAutoAllocateUserListing],
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
