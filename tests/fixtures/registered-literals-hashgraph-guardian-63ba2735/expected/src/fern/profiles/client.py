

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.did_document_dto import DidDocumentDto
from ..types.did_document_status_dto import DidDocumentStatusDto
from ..types.did_key_dto import DidKeyDto
from ..types.did_key_status_dto import DidKeyStatusDto
from ..types.profile_dto import ProfileDto
from ..types.subject_dto import SubjectDto
from ..types.task_dto import TaskDto
from .raw_client import AsyncRawProfilesClient, RawProfilesClient


OMIT = typing.cast(typing.Any, ...)


class ProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfilesClient
        """
        return self._raw_client

    def profile_api_get_profile(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfileDto:
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
        ProfileDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_get_profile(
            username="username",
        )
        """
        _response = self._raw_client.profile_api_get_profile(username, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_set_user_profile(
            username="username",
            entity="entity",
            hedera_account_id="hederaAccountId",
            hedera_account_key="hederaAccountKey",
        )
        """
        _response = self._raw_client.profile_api_set_user_profile(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_set_user_profile_async(
            username="username",
            entity="entity",
            hedera_account_id="hederaAccountId",
            hedera_account_key="hederaAccountKey",
        )
        """
        _response = self._raw_client.profile_api_set_user_profile_async(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

    def profile_api_get_user_balance(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
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
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_get_user_balance(
            username="username",
        )
        """
        _response = self._raw_client.profile_api_get_user_balance(username, request_options=request_options)
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_restore_user_profile(
            username="username",
            entity="entity",
            hedera_account_id="hederaAccountId",
            hedera_account_key="hederaAccountKey",
        )
        """
        _response = self._raw_client.profile_api_restore_user_profile(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_restore_topic(
            username="username",
            entity="entity",
            hedera_account_id="hederaAccountId",
            hedera_account_key="hederaAccountKey",
        )
        """
        _response = self._raw_client.profile_api_restore_topic(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DidDocumentStatusDto:
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
        DidDocumentStatusDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_validate_did_document(
            id="id",
        )
        """
        _response = self._raw_client.profile_api_validate_did_document(
            id=id,
            context=context,
            also_known_as=also_known_as,
            controller=controller,
            verification_method=verification_method,
            authentication=authentication,
            assertion_method=assertion_method,
            key_agreement=key_agreement,
            capability_invocation=capability_invocation,
            capability_delegation=capability_delegation,
            service=service,
            request_options=request_options,
        )
        return _response.data

    def profile_api_validate_did_keys(
        self,
        *,
        document: DidDocumentDto,
        keys: typing.Sequence[DidKeyDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DidKeyStatusDto:
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
        DidKeyStatusDto
            Successful operation.

        Examples
        --------
        from fern import DidDocumentDto, DidKeyDto, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.profile_api_validate_did_keys(
            document=DidDocumentDto(
                id="id",
            ),
            keys=[
                DidKeyDto(
                    id="id",
                    key="key",
                )
            ],
        )
        """
        _response = self._raw_client.profile_api_validate_did_keys(
            document=document, keys=keys, request_options=request_options
        )
        return _response.data


class AsyncProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfilesClient
        """
        return self._raw_client

    async def profile_api_get_profile(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfileDto:
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
        ProfileDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_get_profile(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_get_profile(username, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_set_user_profile(
                username="username",
                entity="entity",
                hedera_account_id="hederaAccountId",
                hedera_account_key="hederaAccountKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_set_user_profile(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_set_user_profile_async(
                username="username",
                entity="entity",
                hedera_account_id="hederaAccountId",
                hedera_account_key="hederaAccountKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_set_user_profile_async(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

    async def profile_api_get_user_balance(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
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
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_get_user_balance(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_get_user_balance(username, request_options=request_options)
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_restore_user_profile(
                username="username",
                entity="entity",
                hedera_account_id="hederaAccountId",
                hedera_account_key="hederaAccountKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_restore_user_profile(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TaskDto:
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
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_restore_topic(
                username="username",
                entity="entity",
                hedera_account_id="hederaAccountId",
                hedera_account_key="hederaAccountKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_restore_topic(
            username,
            entity=entity,
            hedera_account_id=hedera_account_id,
            hedera_account_key=hedera_account_key,
            parent=parent,
            vc_document=vc_document,
            did_document=did_document,
            did_keys=did_keys,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DidDocumentStatusDto:
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
        DidDocumentStatusDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_validate_did_document(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_validate_did_document(
            id=id,
            context=context,
            also_known_as=also_known_as,
            controller=controller,
            verification_method=verification_method,
            authentication=authentication,
            assertion_method=assertion_method,
            key_agreement=key_agreement,
            capability_invocation=capability_invocation,
            capability_delegation=capability_delegation,
            service=service,
            request_options=request_options,
        )
        return _response.data

    async def profile_api_validate_did_keys(
        self,
        *,
        document: DidDocumentDto,
        keys: typing.Sequence[DidKeyDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DidKeyStatusDto:
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
        DidKeyStatusDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DidDocumentDto, DidKeyDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.profile_api_validate_did_keys(
                document=DidDocumentDto(
                    id="id",
                ),
                keys=[
                    DidKeyDto(
                        id="id",
                        key="key",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.profile_api_validate_did_keys(
            document=document, keys=keys, request_options=request_options
        )
        return _response.data
