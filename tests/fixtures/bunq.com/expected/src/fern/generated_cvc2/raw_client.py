

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
from ..types.card_generated_cvc2create import CardGeneratedCvc2Create
from ..types.card_generated_cvc2listing import CardGeneratedCvc2Listing
from ..types.card_generated_cvc2read import CardGeneratedCvc2Read
from ..types.card_generated_cvc2update import CardGeneratedCvc2Update
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGeneratedCvc2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CardGeneratedCvc2Listing]]:
        """
        Get all generated CVC2 codes for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CardGeneratedCvc2Listing]]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CardGeneratedCvc2Listing],
                    parse_obj_as(
                        type_=typing.List[CardGeneratedCvc2Listing],
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

    def create_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardGeneratedCvc2Create]:
        """
        Generate a new CVC2 code for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardGeneratedCvc2Create]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2",
            method="POST",
            json={
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
                    CardGeneratedCvc2Create,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Create,
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

    def read_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CardGeneratedCvc2Read]:
        """
        Get the details for a specific generated CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardGeneratedCvc2Read]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CardGeneratedCvc2Read,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Read,
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

    def update_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        item_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardGeneratedCvc2Update]:
        """
        Endpoint for generating and retrieving a new CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardGeneratedCvc2Update]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2/{encode_path_param(item_id)}",
            method="PUT",
            json={
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
                    CardGeneratedCvc2Update,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Update,
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


class AsyncRawGeneratedCvc2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CardGeneratedCvc2Listing]]:
        """
        Get all generated CVC2 codes for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CardGeneratedCvc2Listing]]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CardGeneratedCvc2Listing],
                    parse_obj_as(
                        type_=typing.List[CardGeneratedCvc2Listing],
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

    async def create_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardGeneratedCvc2Create]:
        """
        Generate a new CVC2 code for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardGeneratedCvc2Create]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2",
            method="POST",
            json={
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
                    CardGeneratedCvc2Create,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Create,
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

    async def read_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CardGeneratedCvc2Read]:
        """
        Get the details for a specific generated CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardGeneratedCvc2Read]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CardGeneratedCvc2Read,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Read,
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

    async def update_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        item_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardGeneratedCvc2Update]:
        """
        Endpoint for generating and retrieving a new CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardGeneratedCvc2Update]
            Endpoint for generating and retrieving a new CVC2 code.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(card_id)}/generated-cvc2/{encode_path_param(item_id)}",
            method="PUT",
            json={
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
                    CardGeneratedCvc2Update,
                    parse_obj_as(
                        type_=CardGeneratedCvc2Update,
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
