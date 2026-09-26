

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id_attribute import IdAttribute
from ..types.list_participant_declarations_filter import ListParticipantDeclarationsFilter
from ..types.pagination_filter import PaginationFilter
from ..types.participant_declaration_response import ParticipantDeclarationResponse
from ..types.participant_declarations_response import ParticipantDeclarationsResponse
from .raw_client import AsyncRawParticipantDeclarationsClient, RawParticipantDeclarationsClient
from .types.participant_declaration_change_delivery_partner_request_data import (
    ParticipantDeclarationChangeDeliveryPartnerRequestData,
)
from .types.participant_declaration_request_data import ParticipantDeclarationRequestData


OMIT = typing.cast(typing.Any, ...)


class ParticipantDeclarationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawParticipantDeclarationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawParticipantDeclarationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawParticipantDeclarationsClient
        """
        return self._raw_client

    def retrieve_multiple_participant_declarations(
        self,
        *,
        filter: typing.Optional[ListParticipantDeclarationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantDeclarationsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantDeclarationsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationsResponse
            A list of Participant declarations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.participant_declarations.retrieve_multiple_participant_declarations()
        """
        _response = self._raw_client.retrieve_multiple_participant_declarations(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    def declare_a_participant_has_reached_a_milestone(
        self, *, data: ParticipantDeclarationRequestData, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        data : ParticipantDeclarationRequestData
            A participant declaration data request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The participant declaration being created

        Examples
        --------
        import datetime

        from fern.participant_declarations import (
            ParticipantDeclarationRequestData,
            ParticipantDeclarationRequestDataType,
        )

        from fern import (
            FernApi,
            ParticipantDeclarationStartedRequest,
            ParticipantDeclarationStartedRequestCourseIdentifier,
            ParticipantDeclarationStartedRequestDeclarationType,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.participant_declarations.declare_a_participant_has_reached_a_milestone(
            data=ParticipantDeclarationRequestData(
                type=ParticipantDeclarationRequestDataType.PARTICIPANT_DECLARATION,
                attributes=ParticipantDeclarationStartedRequest(
                    participant_id="db3a7848-7308-4879-942a-c4a70ced400a",
                    declaration_type=ParticipantDeclarationStartedRequestDeclarationType.STARTED,
                    declaration_date=datetime.datetime.fromisoformat(
                        "2021-05-31 02:21:32+00:00",
                    ),
                    course_identifier=ParticipantDeclarationStartedRequestCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                    delivery_partner_id="524df095-f9bf-4f9d-ba4c-772545a99e60",
                ),
            ),
        )
        """
        _response = self._raw_client.declare_a_participant_has_reached_a_milestone(
            data=data, request_options=request_options
        )
        return _response.data

    def retrieve_a_single_participant_declarations(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            A single Participant declarations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.participant_declarations.retrieve_a_single_participant_declarations(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.retrieve_a_single_participant_declarations(id, request_options=request_options)
        return _response.data

    def void_a_declaration(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The participant declaration being voided

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.participant_declarations.void_a_declaration(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.void_a_declaration(id, request_options=request_options)
        return _response.data

    def change_declaration_delivery_partner(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeclarationChangeDeliveryPartnerRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeclarationChangeDeliveryPartnerRequestData
            A participant declaration change delivery partner request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The declaration delivery partner is going to be changed

        Examples
        --------
        from fern.participant_declarations import (
            ParticipantDeclarationChangeDeliveryPartnerRequestData,
            ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes,
            ParticipantDeclarationChangeDeliveryPartnerRequestDataType,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.participant_declarations.change_declaration_delivery_partner(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ParticipantDeclarationChangeDeliveryPartnerRequestData(
                type=ParticipantDeclarationChangeDeliveryPartnerRequestDataType.PARTICIPANT_DECLARATION,
                attributes=ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes(
                    delivery_partner_id="db3a7848-7308-4879-942a-c4a70ced400a",
                    secondary_delivery_partner_id="f0de7abf-399b-4e68-83de-2c33b503810c",
                ),
            ),
        )
        """
        _response = self._raw_client.change_declaration_delivery_partner(id, data=data, request_options=request_options)
        return _response.data


class AsyncParticipantDeclarationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawParticipantDeclarationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawParticipantDeclarationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawParticipantDeclarationsClient
        """
        return self._raw_client

    async def retrieve_multiple_participant_declarations(
        self,
        *,
        filter: typing.Optional[ListParticipantDeclarationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantDeclarationsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantDeclarationsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationsResponse
            A list of Participant declarations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.participant_declarations.retrieve_multiple_participant_declarations()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_participant_declarations(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    async def declare_a_participant_has_reached_a_milestone(
        self, *, data: ParticipantDeclarationRequestData, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        data : ParticipantDeclarationRequestData
            A participant declaration data request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The participant declaration being created

        Examples
        --------
        import asyncio
        import datetime

        from fern.participant_declarations import (
            ParticipantDeclarationRequestData,
            ParticipantDeclarationRequestDataType,
        )

        from fern import (
            AsyncFernApi,
            ParticipantDeclarationStartedRequest,
            ParticipantDeclarationStartedRequestCourseIdentifier,
            ParticipantDeclarationStartedRequestDeclarationType,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.participant_declarations.declare_a_participant_has_reached_a_milestone(
                data=ParticipantDeclarationRequestData(
                    type=ParticipantDeclarationRequestDataType.PARTICIPANT_DECLARATION,
                    attributes=ParticipantDeclarationStartedRequest(
                        participant_id="db3a7848-7308-4879-942a-c4a70ced400a",
                        declaration_type=ParticipantDeclarationStartedRequestDeclarationType.STARTED,
                        declaration_date=datetime.datetime.fromisoformat(
                            "2021-05-31 02:21:32+00:00",
                        ),
                        course_identifier=ParticipantDeclarationStartedRequestCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
                        delivery_partner_id="524df095-f9bf-4f9d-ba4c-772545a99e60",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.declare_a_participant_has_reached_a_milestone(
            data=data, request_options=request_options
        )
        return _response.data

    async def retrieve_a_single_participant_declarations(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            A single Participant declarations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.participant_declarations.retrieve_a_single_participant_declarations(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_participant_declarations(
            id, request_options=request_options
        )
        return _response.data

    async def void_a_declaration(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The participant declaration being voided

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.participant_declarations.void_a_declaration(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.void_a_declaration(id, request_options=request_options)
        return _response.data

    async def change_declaration_delivery_partner(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeclarationChangeDeliveryPartnerRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParticipantDeclarationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeclarationChangeDeliveryPartnerRequestData
            A participant declaration change delivery partner request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParticipantDeclarationResponse
            The declaration delivery partner is going to be changed

        Examples
        --------
        import asyncio

        from fern.participant_declarations import (
            ParticipantDeclarationChangeDeliveryPartnerRequestData,
            ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes,
            ParticipantDeclarationChangeDeliveryPartnerRequestDataType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.participant_declarations.change_declaration_delivery_partner(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ParticipantDeclarationChangeDeliveryPartnerRequestData(
                    type=ParticipantDeclarationChangeDeliveryPartnerRequestDataType.PARTICIPANT_DECLARATION,
                    attributes=ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes(
                        delivery_partner_id="db3a7848-7308-4879-942a-c4a70ced400a",
                        secondary_delivery_partner_id="f0de7abf-399b-4e68-83de-2c33b503810c",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_declaration_delivery_partner(
            id, data=data, request_options=request_options
        )
        return _response.data
