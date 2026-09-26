

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id_attribute import IdAttribute
from ..types.list_participants_filter import ListParticipantsFilter
from ..types.pagination_filter import PaginationFilter
from ..types.participant_response import ParticipantResponse
from ..types.participants_response import ParticipantsResponse
from ..types.sorting_options import SortingOptions
from .raw_client import AsyncRawNpqParticipantsClient, RawNpqParticipantsClient
from .types.participant_change_schedule_request_data import ParticipantChangeScheduleRequestData
from .types.participant_defer_request_data import ParticipantDeferRequestData
from .types.participant_resume_request_data import ParticipantResumeRequestData
from .types.participant_withdraw_request_data import ParticipantWithdrawRequestData


OMIT = typing.cast(typing.Any, ...)


class NpqParticipantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNpqParticipantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNpqParticipantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNpqParticipantsClient
        """
        return self._raw_client

    def retrieve_multiple_npq_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantsResponse
            A list of NPQ participants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.retrieve_multiple_npq_participants()
        """
        _response = self._raw_client.retrieve_multiple_npq_participants(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data

    def retrieve_a_single_npq_participant(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            A single NPQ participant

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.retrieve_a_single_npq_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.retrieve_a_single_npq_participant(id, request_options=request_options)
        return _response.data

    def resume_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantResumeRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantResumeRequestData
            A participant resume request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being resumed

        Examples
        --------
        from fern.npq_participants import (
            ParticipantResumeRequestData,
            ParticipantResumeRequestDataAttributes,
            ParticipantResumeRequestDataAttributesCourseIdentifier,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.resume_an_npq_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantResumeRequestData(
                type="participant-resume",
                attributes=ParticipantResumeRequestDataAttributes(
                    course_identifier=ParticipantResumeRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                ),
            ),
        )
        """
        _response = self._raw_client.resume_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    def defer_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeferRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeferRequestData
            A participant defer request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being deferred

        Examples
        --------
        from fern.npq_participants import (
            ParticipantDeferRequestData,
            ParticipantDeferRequestDataAttributes,
            ParticipantDeferRequestDataAttributesCourseIdentifier,
            ParticipantDeferRequestDataAttributesReason,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.defer_an_npq_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantDeferRequestData(
                type="participant-defer",
                attributes=ParticipantDeferRequestDataAttributes(
                    course_identifier=ParticipantDeferRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    reason=ParticipantDeferRequestDataAttributesReason.BEREAVEMENT,
                ),
            ),
        )
        """
        _response = self._raw_client.defer_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    def withdraw_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantWithdrawRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantWithdrawRequestData
            A participant withdraw request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being withdrawn

        Examples
        --------
        from fern.npq_participants import (
            ParticipantWithdrawRequestData,
            ParticipantWithdrawRequestDataAttributes,
            ParticipantWithdrawRequestDataAttributesCourseIdentifier,
            ParticipantWithdrawRequestDataAttributesReason,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.withdraw_an_npq_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantWithdrawRequestData(
                type="participant-withdraw",
                attributes=ParticipantWithdrawRequestDataAttributes(
                    course_identifier=ParticipantWithdrawRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    reason=ParticipantWithdrawRequestDataAttributesReason.INSUFFICIENT_CAPACITY_TO_UNDERTAKE_PROGRAMME,
                ),
            ),
        )
        """
        _response = self._raw_client.withdraw_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    def notify_that_an_npq_participant_is_changing_training_schedule(
        self,
        id: IdAttribute,
        *,
        data: ParticipantChangeScheduleRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantChangeScheduleRequestData
            An NPQ participant change schedule request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant changing schedule

        Examples
        --------
        from fern.npq_participants import (
            ParticipantChangeScheduleRequestData,
            ParticipantChangeScheduleRequestDataAttributes,
            ParticipantChangeScheduleRequestDataAttributesCourseIdentifier,
            ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participants.notify_that_an_npq_participant_is_changing_training_schedule(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantChangeScheduleRequestData(
                type="participant-change-schedule",
                attributes=ParticipantChangeScheduleRequestDataAttributes(
                    schedule_identifier=ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_MARCH,
                    course_identifier=ParticipantChangeScheduleRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                ),
            ),
        )
        """
        _response = self._raw_client.notify_that_an_npq_participant_is_changing_training_schedule(
            id, data=data, request_options=request_options
        )
        return _response.data


class AsyncNpqParticipantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNpqParticipantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNpqParticipantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNpqParticipantsClient
        """
        return self._raw_client

    async def retrieve_multiple_npq_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantsResponse
            A list of NPQ participants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.retrieve_multiple_npq_participants()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_npq_participants(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data

    async def retrieve_a_single_npq_participant(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            A single NPQ participant

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.retrieve_a_single_npq_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_npq_participant(id, request_options=request_options)
        return _response.data

    async def resume_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantResumeRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantResumeRequestData
            A participant resume request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being resumed

        Examples
        --------
        import asyncio

        from fern.npq_participants import (
            ParticipantResumeRequestData,
            ParticipantResumeRequestDataAttributes,
            ParticipantResumeRequestDataAttributesCourseIdentifier,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.resume_an_npq_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantResumeRequestData(
                    type="participant-resume",
                    attributes=ParticipantResumeRequestDataAttributes(
                        course_identifier=ParticipantResumeRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    async def defer_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeferRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeferRequestData
            A participant defer request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being deferred

        Examples
        --------
        import asyncio

        from fern.npq_participants import (
            ParticipantDeferRequestData,
            ParticipantDeferRequestDataAttributes,
            ParticipantDeferRequestDataAttributesCourseIdentifier,
            ParticipantDeferRequestDataAttributesReason,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.defer_an_npq_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantDeferRequestData(
                    type="participant-defer",
                    attributes=ParticipantDeferRequestDataAttributes(
                        course_identifier=ParticipantDeferRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                        reason=ParticipantDeferRequestDataAttributesReason.BEREAVEMENT,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.defer_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    async def withdraw_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantWithdrawRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantWithdrawRequestData
            A participant withdraw request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant being withdrawn

        Examples
        --------
        import asyncio

        from fern.npq_participants import (
            ParticipantWithdrawRequestData,
            ParticipantWithdrawRequestDataAttributes,
            ParticipantWithdrawRequestDataAttributesCourseIdentifier,
            ParticipantWithdrawRequestDataAttributesReason,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.withdraw_an_npq_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantWithdrawRequestData(
                    type="participant-withdraw",
                    attributes=ParticipantWithdrawRequestDataAttributes(
                        course_identifier=ParticipantWithdrawRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                        reason=ParticipantWithdrawRequestDataAttributesReason.INSUFFICIENT_CAPACITY_TO_UNDERTAKE_PROGRAMME,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.withdraw_an_npq_participant(id, data=data, request_options=request_options)
        return _response.data

    async def notify_that_an_npq_participant_is_changing_training_schedule(
        self,
        id: IdAttribute,
        *,
        data: ParticipantChangeScheduleRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantChangeScheduleRequestData
            An NPQ participant change schedule request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantResponse
            The NPQ participant changing schedule

        Examples
        --------
        import asyncio

        from fern.npq_participants import (
            ParticipantChangeScheduleRequestData,
            ParticipantChangeScheduleRequestDataAttributes,
            ParticipantChangeScheduleRequestDataAttributesCourseIdentifier,
            ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participants.notify_that_an_npq_participant_is_changing_training_schedule(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantChangeScheduleRequestData(
                    type="participant-change-schedule",
                    attributes=ParticipantChangeScheduleRequestDataAttributes(
                        schedule_identifier=ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_MARCH,
                        course_identifier=ParticipantChangeScheduleRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.notify_that_an_npq_participant_is_changing_training_schedule(
            id, data=data, request_options=request_options
        )
        return _response.data
