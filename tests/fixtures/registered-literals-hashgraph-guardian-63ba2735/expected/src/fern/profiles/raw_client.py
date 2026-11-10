

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.did_document_dto import DidDocumentDto
from ..types.did_document_status_dto import DidDocumentStatusDto
from ..types.did_key_dto import DidKeyDto
from ..types.did_key_status_dto import DidKeyStatusDto
from ..types.profile_dto import ProfileDto
from ..types.subject_dto import SubjectDto
from ..types.task_dto import TaskDto
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def profile_api_get_profile(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProfileDto]:
        """
        Returns user account information. For users with the Standard Registry role it also returns address book and VC document information.

        Parameters
        ----------
        username : str
            The name of the user for whom to fetch the information

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProfileDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileDto,
                    parse_obj_as(
                        type_=ProfileDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_set_user_profile(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Sets Hedera credentials for the user. For users with the Standard Registry role it also creates an address book.

        Parameters
        ----------
        username : str
            The name of the user for whom to update the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_set_user_profile_async(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskDto]:
        """
        Sets Hedera credentials for the user. For users with the Standard Registry role it also creates an address book.

        Parameters
        ----------
        username : str
            The name of the user for whom to update the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/push/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_get_user_balance(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Requests Hedera account balance. Only users with the Installer role are allowed to make the request.

        Parameters
        ----------
        username : str
            The name of the user for whom to fetch the balance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_restore_user_profile(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskDto]:
        """
        Restore user data (policy, DID documents, VC documents).

        Parameters
        ----------
        username : str
            The name of the user for whom to restore the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/restore/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_restore_topic(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskDto]:
        """
        List of available recovery topics.

        Parameters
        ----------
        username : str
            The name of the user for whom to restore the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/restore/topics/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_validate_did_document(
        self,
        *,
        id: str,
        context: typing.Optional[typing.Sequence[str]] = OMIT,
        also_known_as: typing.Optional[typing.Sequence[str]] = OMIT,
        controller: typing.Optional[typing.Sequence[str]] = OMIT,
        verification_method: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        authentication: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        assertion_method: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        key_agreement: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        capability_invocation: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        capability_delegation: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        service: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DidDocumentStatusDto]:
        """
        Validate DID document format.

        Parameters
        ----------
        id : str

        context : typing.Optional[typing.Sequence[str]]

        also_known_as : typing.Optional[typing.Sequence[str]]

        controller : typing.Optional[typing.Sequence[str]]

        verification_method : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        authentication : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        assertion_method : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        key_agreement : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        capability_invocation : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        capability_delegation : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        service : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DidDocumentStatusDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "profiles/did-document/validate",
            method="POST",
            json={
                "id": id,
                "context": context,
                "alsoKnownAs": also_known_as,
                "controller": controller,
                "verificationMethod": verification_method,
                "authentication": authentication,
                "assertionMethod": assertion_method,
                "keyAgreement": key_agreement,
                "capabilityInvocation": capability_invocation,
                "capabilityDelegation": capability_delegation,
                "service": service,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DidDocumentStatusDto,
                    parse_obj_as(
                        type_=DidDocumentStatusDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def profile_api_validate_did_keys(
        self,
        *,
        document: DidDocumentDto,
        keys: typing.Sequence[DidKeyDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DidKeyStatusDto]:
        """
        Validate DID document keys.

        Parameters
        ----------
        document : DidDocumentDto

        keys : typing.Sequence[DidKeyDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DidKeyStatusDto]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "profiles/did-keys/validate",
            method="POST",
            json={
                "document": convert_and_respect_annotation_metadata(
                    object_=document, annotation=DidDocumentDto, direction="write"
                ),
                "keys": convert_and_respect_annotation_metadata(
                    object_=keys, annotation=typing.Sequence[DidKeyDto], direction="write"
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
                    DidKeyStatusDto,
                    parse_obj_as(
                        type_=DidKeyStatusDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def profile_api_get_profile(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProfileDto]:
        """
        Returns user account information. For users with the Standard Registry role it also returns address book and VC document information.

        Parameters
        ----------
        username : str
            The name of the user for whom to fetch the information

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProfileDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileDto,
                    parse_obj_as(
                        type_=ProfileDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_set_user_profile(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Sets Hedera credentials for the user. For users with the Standard Registry role it also creates an address book.

        Parameters
        ----------
        username : str
            The name of the user for whom to update the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_set_user_profile_async(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskDto]:
        """
        Sets Hedera credentials for the user. For users with the Standard Registry role it also creates an address book.

        Parameters
        ----------
        username : str
            The name of the user for whom to update the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/push/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_get_user_balance(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Requests Hedera account balance. Only users with the Installer role are allowed to make the request.

        Parameters
        ----------
        username : str
            The name of the user for whom to fetch the balance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{encode_path_param(username)}/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_restore_user_profile(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskDto]:
        """
        Restore user data (policy, DID documents, VC documents).

        Parameters
        ----------
        username : str
            The name of the user for whom to restore the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/restore/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_restore_topic(
        self,
        username: str,
        *,
        entity: str,
        hedera_account_id: str,
        hedera_account_key: str,
        parent: typing.Optional[str] = OMIT,
        vc_document: typing.Optional[SubjectDto] = OMIT,
        did_document: typing.Optional[DidDocumentDto] = OMIT,
        did_keys: typing.Optional[typing.Sequence[DidKeyDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskDto]:
        """
        List of available recovery topics.

        Parameters
        ----------
        username : str
            The name of the user for whom to restore the information.

        entity : str

        hedera_account_id : str

        hedera_account_key : str

        parent : typing.Optional[str]

        vc_document : typing.Optional[SubjectDto]

        did_document : typing.Optional[DidDocumentDto]

        did_keys : typing.Optional[typing.Sequence[DidKeyDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/restore/topics/{encode_path_param(username)}",
            method="PUT",
            json={
                "entity": entity,
                "hederaAccountId": hedera_account_id,
                "hederaAccountKey": hedera_account_key,
                "parent": parent,
                "vcDocument": convert_and_respect_annotation_metadata(
                    object_=vc_document, annotation=typing.Optional[SubjectDto], direction="write"
                ),
                "didDocument": convert_and_respect_annotation_metadata(
                    object_=did_document, annotation=typing.Optional[DidDocumentDto], direction="write"
                ),
                "didKeys": convert_and_respect_annotation_metadata(
                    object_=did_keys, annotation=typing.Optional[typing.Sequence[DidKeyDto]], direction="write"
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
                    TaskDto,
                    parse_obj_as(
                        type_=TaskDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_validate_did_document(
        self,
        *,
        id: str,
        context: typing.Optional[typing.Sequence[str]] = OMIT,
        also_known_as: typing.Optional[typing.Sequence[str]] = OMIT,
        controller: typing.Optional[typing.Sequence[str]] = OMIT,
        verification_method: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        authentication: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        assertion_method: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        key_agreement: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        capability_invocation: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        capability_delegation: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        service: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DidDocumentStatusDto]:
        """
        Validate DID document format.

        Parameters
        ----------
        id : str

        context : typing.Optional[typing.Sequence[str]]

        also_known_as : typing.Optional[typing.Sequence[str]]

        controller : typing.Optional[typing.Sequence[str]]

        verification_method : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        authentication : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        assertion_method : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        key_agreement : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        capability_invocation : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        capability_delegation : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        service : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DidDocumentStatusDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profiles/did-document/validate",
            method="POST",
            json={
                "id": id,
                "context": context,
                "alsoKnownAs": also_known_as,
                "controller": controller,
                "verificationMethod": verification_method,
                "authentication": authentication,
                "assertionMethod": assertion_method,
                "keyAgreement": key_agreement,
                "capabilityInvocation": capability_invocation,
                "capabilityDelegation": capability_delegation,
                "service": service,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DidDocumentStatusDto,
                    parse_obj_as(
                        type_=DidDocumentStatusDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def profile_api_validate_did_keys(
        self,
        *,
        document: DidDocumentDto,
        keys: typing.Sequence[DidKeyDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DidKeyStatusDto]:
        """
        Validate DID document keys.

        Parameters
        ----------
        document : DidDocumentDto

        keys : typing.Sequence[DidKeyDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DidKeyStatusDto]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profiles/did-keys/validate",
            method="POST",
            json={
                "document": convert_and_respect_annotation_metadata(
                    object_=document, annotation=DidDocumentDto, direction="write"
                ),
                "keys": convert_and_respect_annotation_metadata(
                    object_=keys, annotation=typing.Sequence[DidKeyDto], direction="write"
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
                    DidKeyStatusDto,
                    parse_obj_as(
                        type_=DidKeyStatusDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
