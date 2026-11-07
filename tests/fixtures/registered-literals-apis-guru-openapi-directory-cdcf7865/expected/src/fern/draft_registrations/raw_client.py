

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
from .types.draft_registration_contributors_create_request_attributes import (
    DraftRegistrationContributorsCreateRequestAttributes,
)
from .types.draft_registration_contributors_create_request_relationships import (
    DraftRegistrationContributorsCreateRequestRelationships,
)
from .types.draft_registrations_create_request_attributes import DraftRegistrationsCreateRequestAttributes
from .types.draft_registrations_create_response import DraftRegistrationsCreateResponse
from .types.draft_registrations_read_response import DraftRegistrationsReadResponse
from .types.get_draft_registrations_draft_id_institutions_response import (
    GetDraftRegistrationsDraftIdInstitutionsResponse,
)
from .types.get_draft_registrations_draft_id_response import GetDraftRegistrationsDraftIdResponse
from .types.nodes_draft_registrations_read_response import NodesDraftRegistrationsReadResponse
from .types.nodes_draft_registrations_subjects_response import NodesDraftRegistrationsSubjectsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDraftRegistrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DraftRegistrationsReadResponse]:
        """
        Retrieve a list of all currently available Draft Registrations for that user.
        #### Permissions
        Only Draft Registration contributors may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DraftRegistrationsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "draft_registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DraftRegistrationsReadResponse,
                    parse_obj_as(
                        type_=DraftRegistrationsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        attributes: DraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DraftRegistrationsCreateResponse]:
        """
        This creates a Draft Registration that can be used to edit and register research.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.
        A Draft Registration created by this endpoint will not have a Project linked with it by default, but if the user includes a `branched_from` attribute in their Draft Registration creation payload with the value of the `branched_from` being guid of a Project they have permissions for the Draft Registration will be linked to the Project. If you linked your Draft Registration on a Project, your original Project remains editable and will now have the Draft Registration linked to it.
        #### Permissions
        Any user can create a Draft Registration. If the `branched_from` attribute is provided, then the user must be an ADMIN contributor on the Project being registered.
        #### Required
        Required fields for creating a Draft Registration include:

        &nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created Draft Registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : DraftRegistrationsCreateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DraftRegistrationsCreateResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "draft_registrations/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DraftRegistrationsCreateRequestAttributes, direction="write"
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
                    DraftRegistrationsCreateResponse,
                    parse_obj_as(
                        type_=DraftRegistrationsCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDraftRegistrationsDraftIdResponse]:
        """
        Retrieve the details of a given Draft Registration
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it.
        #### Permissions
        Only draft registration contributors may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDraftRegistrationsDraftIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftRegistrationsDraftIdResponse,
                    parse_obj_as(
                        type_=GetDraftRegistrationsDraftIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
        #### Permissions
        Only draft registration contributors with ADMIN permissions may delete draft registrations
        #### Returns
        If the request is successful, no content is returned.
        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_a_draft_registration(
        self,
        draft_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Updates a Draft Registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged. Note this will not register or change the machine state of a Draft Registration, it can only edit the Draft Registration's attributes prior to its registration.
        #### Permissions
        Only draft registration contributors may view draft registrations and only draft registration contributors with WRITE or ADMIN permissions may update draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def draft_registration_contributors_list(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Retrieves the details of all given Contributors for a Draft Registration.
        Contributors are users who can make changes to the Draft Registration.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def draft_registration_contributors_create(
        self,
        draft_id: str,
        *,
        relationships: DraftRegistrationContributorsCreateRequestRelationships,
        attributes: typing.Optional[DraftRegistrationContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Adds a contributor to a Draft Registration, contributors can view, edit, register or delete a Draft Registration depending on their permissions.
        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Draft Registration.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.
        All attributes describing the relationship between the node and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        relationships : DraftRegistrationContributorsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[DraftRegistrationContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=DraftRegistrationContributorsCreateRequestAttributes,
                    direction="write",
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships,
                    annotation=DraftRegistrationContributorsCreateRequestRelationships,
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
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retreive_a_contributor_from_a_draft_registration(
        self, draft_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Retrieves the details of a given contributor.

        Contributors are users who can view or edit to the Draft Registrations.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        user_id : str
            The unique identifier of the Contributor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_institutions_afilliated_with_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDraftRegistrationsDraftIdInstitutionsResponse]:
        """
        Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDraftRegistrationsDraftIdInstitutionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftRegistrationsDraftIdInstitutionsResponse,
                    parse_obj_as(
                        type_=GetDraftRegistrationsDraftIdInstitutionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def nodes_draft_registrations_subjects(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NodesDraftRegistrationsSubjectsResponse]:
        """
        This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodesDraftRegistrationsSubjectsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/subjects/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodesDraftRegistrationsSubjectsResponse,
                    parse_obj_as(
                        type_=NodesDraftRegistrationsSubjectsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def nodes_draft_registrations_read(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NodesDraftRegistrationsReadResponse]:
        """
        Retrieve the details of a given draft registration.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodesDraftRegistrationsReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}/draft_registrations/{encode_path_param(draft_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodesDraftRegistrationsReadResponse,
                    parse_obj_as(
                        type_=NodesDraftRegistrationsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDraftRegistrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DraftRegistrationsReadResponse]:
        """
        Retrieve a list of all currently available Draft Registrations for that user.
        #### Permissions
        Only Draft Registration contributors may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DraftRegistrationsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "draft_registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DraftRegistrationsReadResponse,
                    parse_obj_as(
                        type_=DraftRegistrationsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        attributes: DraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DraftRegistrationsCreateResponse]:
        """
        This creates a Draft Registration that can be used to edit and register research.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.
        A Draft Registration created by this endpoint will not have a Project linked with it by default, but if the user includes a `branched_from` attribute in their Draft Registration creation payload with the value of the `branched_from` being guid of a Project they have permissions for the Draft Registration will be linked to the Project. If you linked your Draft Registration on a Project, your original Project remains editable and will now have the Draft Registration linked to it.
        #### Permissions
        Any user can create a Draft Registration. If the `branched_from` attribute is provided, then the user must be an ADMIN contributor on the Project being registered.
        #### Required
        Required fields for creating a Draft Registration include:

        &nbsp;&nbsp;&nbsp;&nbsp;`schema_id`
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the created Draft Registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : DraftRegistrationsCreateRequestAttributes
            The properties of the Draft Registration entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DraftRegistrationsCreateResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "draft_registrations/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DraftRegistrationsCreateRequestAttributes, direction="write"
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
                    DraftRegistrationsCreateResponse,
                    parse_obj_as(
                        type_=DraftRegistrationsCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDraftRegistrationsDraftIdResponse]:
        """
        Retrieve the details of a given Draft Registration
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it.
        #### Permissions
        Only draft registration contributors may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDraftRegistrationsDraftIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftRegistrationsDraftIdResponse,
                    parse_obj_as(
                        type_=GetDraftRegistrationsDraftIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Permanently deletes a draft registration. A draft that has already been registered cannot be deleted.
        #### Permissions
        Only draft registration contributors with ADMIN permissions may delete draft registrations
        #### Returns
        If the request is successful, no content is returned.
        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_a_draft_registration(
        self,
        draft_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Updates a Draft Registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged. Note this will not register or change the machine state of a Draft Registration, it can only edit the Draft Registration's attributes prior to its registration.
        #### Permissions
        Only draft registration contributors may view draft registrations and only draft registration contributors with WRITE or ADMIN permissions may update draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the new representation of the updated draft registration, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def draft_registration_contributors_list(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Retrieves the details of all given Contributors for a Draft Registration.
        Contributors are users who can make changes to the Draft Registration.
        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def draft_registration_contributors_create(
        self,
        draft_id: str,
        *,
        relationships: DraftRegistrationContributorsCreateRequestRelationships,
        attributes: typing.Optional[DraftRegistrationContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Adds a contributor to a Draft Registration, contributors can view, edit, register or delete a Draft Registration depending on their permissions.
        Contributors are categorized as either "bibliographic" or "non-bibliographic" contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
        #### Permissions
        Only project administrators can add contributors to a Draft Registration.
        #### Required
        A relationship object with a `data` key, containing the `users` type and valid user ID is required.
        All attributes describing the relationship between the node and the user are optional.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the new contributor, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        relationships : DraftRegistrationContributorsCreateRequestRelationships
            URLs to other entities or entity collections that have a relationship to the contributor entity.

        attributes : typing.Optional[DraftRegistrationContributorsCreateRequestAttributes]
            The properties of the contributor entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=DraftRegistrationContributorsCreateRequestAttributes,
                    direction="write",
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships,
                    annotation=DraftRegistrationContributorsCreateRequestRelationships,
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
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retreive_a_contributor_from_a_draft_registration(
        self, draft_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Retrieves the details of a given contributor.

        Contributors are users who can view or edit to the Draft Registrations.

        Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the Draft Registration.

        user_id : str
            The unique identifier of the Contributor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/contributors/{encode_path_param(user_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_institutions_afilliated_with_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDraftRegistrationsDraftIdInstitutionsResponse]:
        """
        Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDraftRegistrationsDraftIdInstitutionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/institutions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftRegistrationsDraftIdInstitutionsResponse,
                    parse_obj_as(
                        type_=GetDraftRegistrationsDraftIdInstitutionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def nodes_draft_registrations_subjects(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NodesDraftRegistrationsSubjectsResponse]:
        """
        This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.

        Parameters
        ----------
        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodesDraftRegistrationsSubjectsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"draft_registrations/{encode_path_param(draft_id)}/subjects/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodesDraftRegistrationsSubjectsResponse,
                    parse_obj_as(
                        type_=NodesDraftRegistrationsSubjectsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def nodes_draft_registrations_read(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NodesDraftRegistrationsReadResponse]:
        """
        Retrieve the details of a given draft registration.
        Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.

        Your original project remains editable but will now have the draft registration linked to it.
        #### Permissions
        Only project administrators may view draft registrations.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        node_id : str
            The unique identifier of the node.

        draft_id : str
            The unique identifier of the draft registration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodesDraftRegistrationsReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}/draft_registrations/{encode_path_param(draft_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodesDraftRegistrationsReadResponse,
                    parse_obj_as(
                        type_=NodesDraftRegistrationsReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
