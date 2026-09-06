

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_translation_request import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest,
)
from ..types.global_resources_shared_models_translation_request import GlobalResourcesSharedModelsTranslationRequest
from ..types.global_resources_shared_models_translation_request_state import (
    GlobalResourcesSharedModelsTranslationRequestState,
)
from .raw_client import AsyncRawTranslationrequestsClient, RawTranslationrequestsClient


OMIT = typing.cast(typing.Any, ...)


class TranslationrequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranslationrequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranslationrequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranslationrequestsClient
        """
        return self._raw_client

    def gettranslationrequests(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationrequests.gettranslationrequests()
        """
        _response = self._raw_client.gettranslationrequests(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def createtranslationrequest(
        self,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import datetime

        from fern import FernApi, GlobalResourcesSharedModelsTranslationRequestState

        client = FernApi()
        client.translationrequests.createtranslationrequest(
            cc_email_addresses=["CCEmailAddresses"],
            charge_to_account="ChargeToAccount",
            deadline=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            locale_ids=[1],
            notes="Notes",
            state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
        )
        """
        _response = self._raw_client.createtranslationrequest(
            cc_email_addresses=cc_email_addresses,
            charge_to_account=charge_to_account,
            deadline=deadline,
            locale_ids=locale_ids,
            notes=notes,
            state=state,
            approval_user_id=approval_user_id,
            id=id,
            questions_user_id=questions_user_id,
            submitted_by=submitted_by,
            translator_email=translator_email,
            translator_name=translator_name,
            request_options=request_options,
        )
        return _response.data

    def gettranslationrequest(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsTranslationRequest:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationRequest
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationrequests.gettranslationrequest(
            id=1,
        )
        """
        _response = self._raw_client.gettranslationrequest(id, request_options=request_options)
        return _response.data

    def updatetranslationrequest(
        self,
        id_: int,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        do_resend_request: typing.Optional[bool] = None,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        do_resend_request : typing.Optional[bool]


        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi, GlobalResourcesSharedModelsTranslationRequestState

        client = FernApi()
        client.translationrequests.updatetranslationrequest(
            id_=1,
            cc_email_addresses=["CCEmailAddresses"],
            charge_to_account="ChargeToAccount",
            deadline=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            locale_ids=[1],
            notes="Notes",
            state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
        )
        """
        _response = self._raw_client.updatetranslationrequest(
            id_,
            cc_email_addresses=cc_email_addresses,
            charge_to_account=charge_to_account,
            deadline=deadline,
            locale_ids=locale_ids,
            notes=notes,
            state=state,
            do_resend_request=do_resend_request,
            approval_user_id=approval_user_id,
            id=id,
            questions_user_id=questions_user_id,
            submitted_by=submitted_by,
            translator_email=translator_email,
            translator_name=translator_name,
            request_options=request_options,
        )
        return _response.data

    def updatetranslationrequeststrings(
        self, id: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationrequests.updatetranslationrequeststrings(
            id=1,
            request=["string"],
        )
        """
        _response = self._raw_client.updatetranslationrequeststrings(
            id, request=request, request_options=request_options
        )
        return _response.data


class AsyncTranslationrequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranslationrequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranslationrequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranslationrequestsClient
        """
        return self._raw_client

    async def gettranslationrequests(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationrequests.gettranslationrequests()


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationrequests(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def createtranslationrequest(
        self,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            GlobalResourcesSharedModelsTranslationRequestState,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationrequests.createtranslationrequest(
                cc_email_addresses=["CCEmailAddresses"],
                charge_to_account="ChargeToAccount",
                deadline=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                locale_ids=[1],
                notes="Notes",
                state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createtranslationrequest(
            cc_email_addresses=cc_email_addresses,
            charge_to_account=charge_to_account,
            deadline=deadline,
            locale_ids=locale_ids,
            notes=notes,
            state=state,
            approval_user_id=approval_user_id,
            id=id,
            questions_user_id=questions_user_id,
            submitted_by=submitted_by,
            translator_email=translator_email,
            translator_name=translator_name,
            request_options=request_options,
        )
        return _response.data

    async def gettranslationrequest(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsTranslationRequest:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationRequest
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationrequests.gettranslationrequest(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationrequest(id, request_options=request_options)
        return _response.data

    async def updatetranslationrequest(
        self,
        id_: int,
        *,
        cc_email_addresses: typing.Sequence[str],
        charge_to_account: str,
        deadline: dt.datetime,
        locale_ids: typing.Sequence[int],
        notes: str,
        state: GlobalResourcesSharedModelsTranslationRequestState,
        do_resend_request: typing.Optional[bool] = None,
        approval_user_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        questions_user_id: typing.Optional[int] = OMIT,
        submitted_by: typing.Optional[int] = OMIT,
        translator_email: typing.Optional[str] = OMIT,
        translator_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        cc_email_addresses : typing.Sequence[str]
            Additional email addresses to CC on emails pertaining to the request

        charge_to_account : str
            The account to charge for the request

        deadline : dt.datetime
            The date by which the translations in the request are needed. Defaults to 30 days from the current date

        locale_ids : typing.Sequence[int]
            Locale IDs to which these strings are requested to be translated

        notes : str
            Additional notes or comments about the request

        state : GlobalResourcesSharedModelsTranslationRequestState
            The state of the request

        do_resend_request : typing.Optional[bool]


        approval_user_id : typing.Optional[int]
            The ID of the user from which approval for the request is required

        id : typing.Optional[int]
            The ID of the request

        questions_user_id : typing.Optional[int]
            The ID of the user to which to address questions regarding the request

        submitted_by : typing.Optional[int]
            The ID of the User that submitted the request

        translator_email : typing.Optional[str]
            The email address for the translator

        translator_name : typing.Optional[str]
            The name of the translator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            GlobalResourcesSharedModelsTranslationRequestState,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationrequests.updatetranslationrequest(
                id_=1,
                cc_email_addresses=["CCEmailAddresses"],
                charge_to_account="ChargeToAccount",
                deadline=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                locale_ids=[1],
                notes="Notes",
                state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationrequest(
            id_,
            cc_email_addresses=cc_email_addresses,
            charge_to_account=charge_to_account,
            deadline=deadline,
            locale_ids=locale_ids,
            notes=notes,
            state=state,
            do_resend_request=do_resend_request,
            approval_user_id=approval_user_id,
            id=id,
            questions_user_id=questions_user_id,
            submitted_by=submitted_by,
            translator_email=translator_email,
            translator_name=translator_name,
            request_options=request_options,
        )
        return _response.data

    async def updatetranslationrequeststrings(
        self, id: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[str]

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
            await client.translationrequests.updatetranslationrequeststrings(
                id=1,
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationrequeststrings(
            id, request=request, request_options=request_options
        )
        return _response.data
