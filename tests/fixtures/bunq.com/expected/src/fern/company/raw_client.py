

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
from ..types.address import Address
from ..types.company_create import CompanyCreate
from ..types.company_listing import CompanyListing
from ..types.company_read import CompanyRead
from ..types.company_update import CompanyUpdate
from ..types.company_vat_number import CompanyVatNumber
from ..types.ubo import Ubo
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_company_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CompanyListing]]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CompanyListing]]
            Create and manage companies.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CompanyListing],
                    parse_obj_as(
                        type_=typing.List[CompanyListing],
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

    def create_company_for_user(
        self,
        user_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompanyCreate]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompanyCreate]
            Create and manage companies.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company",
            method="POST",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "country": country,
                "legal_form": legal_form,
                "name": name,
                "signup_track_type": signup_track_type,
                "subscription_type": subscription_type,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "vat_number": convert_and_respect_annotation_metadata(
                    object_=vat_number, annotation=CompanyVatNumber, direction="write"
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
                    CompanyCreate,
                    parse_obj_as(
                        type_=CompanyCreate,
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

    def read_company_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CompanyRead]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompanyRead]
            Create and manage companies.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompanyRead,
                    parse_obj_as(
                        type_=CompanyRead,
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

    def update_company_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompanyUpdate]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompanyUpdate]
            Create and manage companies.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "country": country,
                "legal_form": legal_form,
                "name": name,
                "signup_track_type": signup_track_type,
                "subscription_type": subscription_type,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "vat_number": convert_and_respect_annotation_metadata(
                    object_=vat_number, annotation=CompanyVatNumber, direction="write"
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
                    CompanyUpdate,
                    parse_obj_as(
                        type_=CompanyUpdate,
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


class AsyncRawCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_company_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CompanyListing]]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CompanyListing]]
            Create and manage companies.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CompanyListing],
                    parse_obj_as(
                        type_=typing.List[CompanyListing],
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

    async def create_company_for_user(
        self,
        user_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompanyCreate]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompanyCreate]
            Create and manage companies.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company",
            method="POST",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "country": country,
                "legal_form": legal_form,
                "name": name,
                "signup_track_type": signup_track_type,
                "subscription_type": subscription_type,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "vat_number": convert_and_respect_annotation_metadata(
                    object_=vat_number, annotation=CompanyVatNumber, direction="write"
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
                    CompanyCreate,
                    parse_obj_as(
                        type_=CompanyCreate,
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

    async def read_company_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CompanyRead]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompanyRead]
            Create and manage companies.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompanyRead,
                    parse_obj_as(
                        type_=CompanyRead,
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

    async def update_company_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        address_main: Address,
        address_postal: Address,
        country: str,
        legal_form: str,
        name: str,
        subscription_type: str,
        avatar_uuid: typing.Optional[str] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        signup_track_type: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        vat_number: typing.Optional[CompanyVatNumber] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompanyUpdate]:
        """
        Create and manage companies.

        Parameters
        ----------
        user_id : int


        item_id : int


        address_main : Address
            The company's main address.

        address_postal : Address
            The company's postal address.

        country : str
            The country where the company is registered.

        legal_form : str
            The company's legal form.

        name : str
            The company name.

        subscription_type : str
            The subscription type for the company.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        signup_track_type : typing.Optional[str]
            The type of signup track the user is following.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        vat_number : typing.Optional[CompanyVatNumber]
            All the vat numbers of the company

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompanyUpdate]
            Create and manage companies.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/company/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "avatar_uuid": avatar_uuid,
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "country": country,
                "legal_form": legal_form,
                "name": name,
                "signup_track_type": signup_track_type,
                "subscription_type": subscription_type,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "vat_number": convert_and_respect_annotation_metadata(
                    object_=vat_number, annotation=CompanyVatNumber, direction="write"
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
                    CompanyUpdate,
                    parse_obj_as(
                        type_=CompanyUpdate,
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
