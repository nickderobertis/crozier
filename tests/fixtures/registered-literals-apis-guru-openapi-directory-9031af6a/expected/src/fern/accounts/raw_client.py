

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
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.add_user_to_account_request_account import AddUserToAccountRequestAccount
from .types.add_user_to_account_request_users_item import AddUserToAccountRequestUsersItem
from .types.add_user_to_account_response import AddUserToAccountResponse
from .types.delete_account_request_identification import DeleteAccountRequestIdentification
from .types.delete_account_response import DeleteAccountResponse
from .types.remove_user_from_account_request_account import RemoveUserFromAccountRequestAccount
from .types.remove_user_from_account_request_users_item import RemoveUserFromAccountRequestUsersItem
from .types.remove_user_from_account_response import RemoveUserFromAccountResponse
from .types.upsert_account_request_identification import UpsertAccountRequestIdentification
from .types.upsert_account_request_properties_value import UpsertAccountRequestPropertiesValue
from .types.upsert_account_response import UpsertAccountResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete_account(
        self,
        *,
        identification: DeleteAccountRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteAccountResponse]:
        """
        Endpoint used to delete an account.

        Parameters
        ----------
        identification : DeleteAccountRequestIdentification
            Account identification requires an accountId, domain or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAccountResponse]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts",
            method="DELETE",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=DeleteAccountRequestIdentification, direction="write"
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
                    DeleteAccountResponse,
                    parse_obj_as(
                        type_=DeleteAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def upsert_account(
        self,
        *,
        identification: UpsertAccountRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpsertAccountResponse]:
        """
        Endpoint used to create or update an account.

        Parameters
        ----------
        identification : UpsertAccountRequestIdentification
            Account identification requires an accountId, domain or both

        properties : typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpsertAccountResponse]
            Account will be created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/upsert",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=UpsertAccountRequestIdentification, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties,
                    annotation=typing.Dict[str, UpsertAccountRequestPropertiesValue],
                    direction="write",
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
                    UpsertAccountResponse,
                    parse_obj_as(
                        type_=UpsertAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def add_user_to_account(
        self,
        *,
        account: AddUserToAccountRequestAccount,
        users: typing.Sequence[AddUserToAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddUserToAccountResponse]:
        """
        You can add up to 100 users to an account.

        Parameters
        ----------
        account : AddUserToAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[AddUserToAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddUserToAccountResponse]
            Object was created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/users/add",
            method="POST",
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=AddUserToAccountRequestAccount, direction="write"
                ),
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[AddUserToAccountRequestUsersItem], direction="write"
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
                    AddUserToAccountResponse,
                    parse_obj_as(
                        type_=AddUserToAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def remove_user_from_account(
        self,
        *,
        account: RemoveUserFromAccountRequestAccount,
        users: typing.Sequence[RemoveUserFromAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RemoveUserFromAccountResponse]:
        """
        You can remove up to 100 users from an account.

        When removing a user, the user will still be stored in journy.io, but marked as "removed".

        Parameters
        ----------
        account : RemoveUserFromAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[RemoveUserFromAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RemoveUserFromAccountResponse]
            No content
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/users/remove",
            method="POST",
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=RemoveUserFromAccountRequestAccount, direction="write"
                ),
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[RemoveUserFromAccountRequestUsersItem], direction="write"
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
                    RemoveUserFromAccountResponse,
                    parse_obj_as(
                        type_=RemoveUserFromAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete_account(
        self,
        *,
        identification: DeleteAccountRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteAccountResponse]:
        """
        Endpoint used to delete an account.

        Parameters
        ----------
        identification : DeleteAccountRequestIdentification
            Account identification requires an accountId, domain or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAccountResponse]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts",
            method="DELETE",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=DeleteAccountRequestIdentification, direction="write"
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
                    DeleteAccountResponse,
                    parse_obj_as(
                        type_=DeleteAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def upsert_account(
        self,
        *,
        identification: UpsertAccountRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpsertAccountResponse]:
        """
        Endpoint used to create or update an account.

        Parameters
        ----------
        identification : UpsertAccountRequestIdentification
            Account identification requires an accountId, domain or both

        properties : typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpsertAccountResponse]
            Account will be created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/upsert",
            method="POST",
            json={
                "identification": convert_and_respect_annotation_metadata(
                    object_=identification, annotation=UpsertAccountRequestIdentification, direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties,
                    annotation=typing.Dict[str, UpsertAccountRequestPropertiesValue],
                    direction="write",
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
                    UpsertAccountResponse,
                    parse_obj_as(
                        type_=UpsertAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def add_user_to_account(
        self,
        *,
        account: AddUserToAccountRequestAccount,
        users: typing.Sequence[AddUserToAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddUserToAccountResponse]:
        """
        You can add up to 100 users to an account.

        Parameters
        ----------
        account : AddUserToAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[AddUserToAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddUserToAccountResponse]
            Object was created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/users/add",
            method="POST",
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=AddUserToAccountRequestAccount, direction="write"
                ),
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[AddUserToAccountRequestUsersItem], direction="write"
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
                    AddUserToAccountResponse,
                    parse_obj_as(
                        type_=AddUserToAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def remove_user_from_account(
        self,
        *,
        account: RemoveUserFromAccountRequestAccount,
        users: typing.Sequence[RemoveUserFromAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RemoveUserFromAccountResponse]:
        """
        You can remove up to 100 users from an account.

        When removing a user, the user will still be stored in journy.io, but marked as "removed".

        Parameters
        ----------
        account : RemoveUserFromAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[RemoveUserFromAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RemoveUserFromAccountResponse]
            No content
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/users/remove",
            method="POST",
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=RemoveUserFromAccountRequestAccount, direction="write"
                ),
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[RemoveUserFromAccountRequestUsersItem], direction="write"
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
                    RemoveUserFromAccountResponse,
                    parse_obj_as(
                        type_=RemoveUserFromAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
