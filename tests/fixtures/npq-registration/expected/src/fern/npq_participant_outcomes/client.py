

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id_attribute import IdAttribute
from ..types.list_participant_outcomes_filter import ListParticipantOutcomesFilter
from ..types.pagination_filter import PaginationFilter
from ..types.participant_outcome_response import ParticipantOutcomeResponse
from ..types.participant_outcomes_response import ParticipantOutcomesResponse
from .raw_client import AsyncRawNpqParticipantOutcomesClient, RawNpqParticipantOutcomesClient
from .types.participant_outcome_create_request_data import ParticipantOutcomeCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class NpqParticipantOutcomesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNpqParticipantOutcomesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNpqParticipantOutcomesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNpqParticipantOutcomesClient
        """
        return self._raw_client

    def retrieve_multiple_npq_outcomes_for_all_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantOutcomesFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomesResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantOutcomesFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomesResponse
            A list of NPQ Outcomes for all participants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_all_participants()
        """
        _response = self._raw_client.retrieve_multiple_npq_outcomes_for_all_participants(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    def retrieve_multiple_npq_outcomes_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomesResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomesResponse
            A list of NPQ Outcomes for a single participant

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_a_single_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.retrieve_multiple_npq_outcomes_for_a_single_participant(
            id, page=page, request_options=request_options
        )
        return _response.data

    def submit_a_npq_outcome_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantOutcomeCreateRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomeResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantOutcomeCreateRequestData
            The NPQ outcome submission request attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomeResponse
            The details of an NPQ Outcome

        Examples
        --------
        from fern.npq_participant_outcomes import (
            ParticipantOutcomeCreateRequestData,
            ParticipantOutcomeCreateRequestDataAttributes,
            ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier,
            ParticipantOutcomeCreateRequestDataAttributesState,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_participant_outcomes.submit_a_npq_outcome_for_a_single_participant(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantOutcomeCreateRequestData(
                type="npq-outcome-confirmation",
                attributes=ParticipantOutcomeCreateRequestDataAttributes(
                    course_identifier=ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    state=ParticipantOutcomeCreateRequestDataAttributesState.PASSED,
                    completion_date="2021-05-31T00:00:00+00:00",
                ),
            ),
        )
        """
        _response = self._raw_client.submit_a_npq_outcome_for_a_single_participant(
            id, data=data, request_options=request_options
        )
        return _response.data


class AsyncNpqParticipantOutcomesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNpqParticipantOutcomesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNpqParticipantOutcomesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNpqParticipantOutcomesClient
        """
        return self._raw_client

    async def retrieve_multiple_npq_outcomes_for_all_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantOutcomesFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomesResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantOutcomesFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomesResponse
            A list of NPQ Outcomes for all participants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_all_participants()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_npq_outcomes_for_all_participants(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    async def retrieve_multiple_npq_outcomes_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomesResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomesResponse
            A list of NPQ Outcomes for a single participant

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_a_single_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_npq_outcomes_for_a_single_participant(
            id, page=page, request_options=request_options
        )
        return _response.data

    async def submit_a_npq_outcome_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantOutcomeCreateRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantOutcomeResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantOutcomeCreateRequestData
            The NPQ outcome submission request attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantOutcomeResponse
            The details of an NPQ Outcome

        Examples
        --------
        import asyncio

        from fern.npq_participant_outcomes import (
            ParticipantOutcomeCreateRequestData,
            ParticipantOutcomeCreateRequestDataAttributes,
            ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier,
            ParticipantOutcomeCreateRequestDataAttributesState,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_participant_outcomes.submit_a_npq_outcome_for_a_single_participant(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantOutcomeCreateRequestData(
                    type="npq-outcome-confirmation",
                    attributes=ParticipantOutcomeCreateRequestDataAttributes(
                        course_identifier=ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                        state=ParticipantOutcomeCreateRequestDataAttributesState.PASSED,
                        completion_date="2021-05-31T00:00:00+00:00",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_npq_outcome_for_a_single_participant(
            id, data=data, request_options=request_options
        )
        return _response.data
