

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDraftRegistrationsClient, RawDraftRegistrationsClient
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


OMIT = typing.cast(typing.Any, ...)


class DraftRegistrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDraftRegistrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDraftRegistrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDraftRegistrationsClient
        """
        return self._raw_client

    def read(self, *, request_options: typing.Optional[RequestOptions] = None) -> DraftRegistrationsReadResponse:
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
        DraftRegistrationsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.read()
        """
        _response = self._raw_client.read(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        attributes: DraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftRegistrationsCreateResponse:
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
        DraftRegistrationsCreateResponse
            Created

        Examples
        --------
        from fern.draft_registrations import DraftRegistrationsCreateRequestAttributes

        from fern import FernApi

        client = FernApi()
        client.draft_registrations.create(
            attributes=DraftRegistrationsCreateRequestAttributes(),
        )
        """
        _response = self._raw_client.create(attributes=attributes, request_options=request_options)
        return _response.data

    def retrieve_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDraftRegistrationsDraftIdResponse:
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
        GetDraftRegistrationsDraftIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.retrieve_a_draft_registration(
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.retrieve_a_draft_registration(draft_id, request_options=request_options)
        return _response.data

    def delete_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.delete_a_draft_registration(
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.delete_a_draft_registration(draft_id, request_options=request_options)
        return _response.data

    def update_a_draft_registration(
        self,
        draft_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.update_a_draft_registration(
            draft_id="draft_id",
            request={
                "data": {
                    "attributes": {
                        "registration_responses": {"summary": "Test Value"},
                        "title": "test title change",
                    },
                    "id": "626ffc1ad90ebe0011fc7601",
                    "type": "draft_registrations",
                }
            },
        )
        """
        _response = self._raw_client.update_a_draft_registration(
            draft_id, request=request, request_options=request_options
        )
        return _response.data

    def draft_registration_contributors_list(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.draft_registration_contributors_list(
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.draft_registration_contributors_list(draft_id, request_options=request_options)
        return _response.data

    def draft_registration_contributors_create(
        self,
        draft_id: str,
        *,
        relationships: DraftRegistrationContributorsCreateRequestRelationships,
        attributes: typing.Optional[DraftRegistrationContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern.draft_registrations import (
            DraftRegistrationContributorsCreateRequestRelationships,
        )

        from fern import FernApi

        client = FernApi()
        client.draft_registrations.draft_registration_contributors_create(
            draft_id="draft_id",
            relationships=DraftRegistrationContributorsCreateRequestRelationships(
                user="user",
            ),
        )
        """
        _response = self._raw_client.draft_registration_contributors_create(
            draft_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    def retreive_a_contributor_from_a_draft_registration(
        self, draft_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.retreive_a_contributor_from_a_draft_registration(
            draft_id="draft_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.retreive_a_contributor_from_a_draft_registration(
            draft_id, user_id, request_options=request_options
        )
        return _response.data

    def retrieve_institutions_afilliated_with_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDraftRegistrationsDraftIdInstitutionsResponse:
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
        GetDraftRegistrationsDraftIdInstitutionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.retrieve_institutions_afilliated_with_a_draft_registration(
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.retrieve_institutions_afilliated_with_a_draft_registration(
            draft_id, request_options=request_options
        )
        return _response.data

    def nodes_draft_registrations_subjects(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesDraftRegistrationsSubjectsResponse:
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
        NodesDraftRegistrationsSubjectsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.nodes_draft_registrations_subjects(
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.nodes_draft_registrations_subjects(draft_id, request_options=request_options)
        return _response.data

    def nodes_draft_registrations_read(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesDraftRegistrationsReadResponse:
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
        NodesDraftRegistrationsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_registrations.nodes_draft_registrations_read(
            node_id="node_id",
            draft_id="draft_id",
        )
        """
        _response = self._raw_client.nodes_draft_registrations_read(node_id, draft_id, request_options=request_options)
        return _response.data


class AsyncDraftRegistrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDraftRegistrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDraftRegistrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDraftRegistrationsClient
        """
        return self._raw_client

    async def read(self, *, request_options: typing.Optional[RequestOptions] = None) -> DraftRegistrationsReadResponse:
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
        DraftRegistrationsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.read()


        asyncio.run(main())
        """
        _response = await self._raw_client.read(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        attributes: DraftRegistrationsCreateRequestAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DraftRegistrationsCreateResponse:
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
        DraftRegistrationsCreateResponse
            Created

        Examples
        --------
        import asyncio

        from fern.draft_registrations import DraftRegistrationsCreateRequestAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.create(
                attributes=DraftRegistrationsCreateRequestAttributes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(attributes=attributes, request_options=request_options)
        return _response.data

    async def retrieve_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDraftRegistrationsDraftIdResponse:
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
        GetDraftRegistrationsDraftIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.retrieve_a_draft_registration(
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_draft_registration(draft_id, request_options=request_options)
        return _response.data

    async def delete_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.delete_a_draft_registration(
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_draft_registration(draft_id, request_options=request_options)
        return _response.data

    async def update_a_draft_registration(
        self,
        draft_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.update_a_draft_registration(
                draft_id="draft_id",
                request={
                    "data": {
                        "attributes": {
                            "registration_responses": {"summary": "Test Value"},
                            "title": "test title change",
                        },
                        "id": "626ffc1ad90ebe0011fc7601",
                        "type": "draft_registrations",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_draft_registration(
            draft_id, request=request, request_options=request_options
        )
        return _response.data

    async def draft_registration_contributors_list(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.draft_registration_contributors_list(
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registration_contributors_list(
            draft_id, request_options=request_options
        )
        return _response.data

    async def draft_registration_contributors_create(
        self,
        draft_id: str,
        *,
        relationships: DraftRegistrationContributorsCreateRequestRelationships,
        attributes: typing.Optional[DraftRegistrationContributorsCreateRequestAttributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern.draft_registrations import (
            DraftRegistrationContributorsCreateRequestRelationships,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.draft_registration_contributors_create(
                draft_id="draft_id",
                relationships=DraftRegistrationContributorsCreateRequestRelationships(
                    user="user",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.draft_registration_contributors_create(
            draft_id, relationships=relationships, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def retreive_a_contributor_from_a_draft_registration(
        self, draft_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.retreive_a_contributor_from_a_draft_registration(
                draft_id="draft_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retreive_a_contributor_from_a_draft_registration(
            draft_id, user_id, request_options=request_options
        )
        return _response.data

    async def retrieve_institutions_afilliated_with_a_draft_registration(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDraftRegistrationsDraftIdInstitutionsResponse:
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
        GetDraftRegistrationsDraftIdInstitutionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.retrieve_institutions_afilliated_with_a_draft_registration(
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_institutions_afilliated_with_a_draft_registration(
            draft_id, request_options=request_options
        )
        return _response.data

    async def nodes_draft_registrations_subjects(
        self, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesDraftRegistrationsSubjectsResponse:
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
        NodesDraftRegistrationsSubjectsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.nodes_draft_registrations_subjects(
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.nodes_draft_registrations_subjects(draft_id, request_options=request_options)
        return _response.data

    async def nodes_draft_registrations_read(
        self, node_id: str, draft_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodesDraftRegistrationsReadResponse:
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
        NodesDraftRegistrationsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_registrations.nodes_draft_registrations_read(
                node_id="node_id",
                draft_id="draft_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.nodes_draft_registrations_read(
            node_id, draft_id, request_options=request_options
        )
        return _response.data
