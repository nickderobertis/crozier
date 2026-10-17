

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCrewsClient, RawCrewsClient
from .types.crew_request_roster import CrewRequestRoster


OMIT = typing.cast(typing.Any, ...)


class CrewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrewsClient
        """
        return self._raw_client

    def register_crew(
        self,
        *,
        vessel: str,
        roster: typing.Optional[CrewRequestRoster] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        vessel : str

        roster : typing.Optional[CrewRequestRoster]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.crews import CrewRequestRoster, CrewRequestRosterRolesValue

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crews.register_crew(
            vessel="Sea Lark",
            roster=CrewRequestRoster(
                roles={
                    "skipper": CrewRequestRosterRolesValue(
                        name="Ada",
                    ),
                    "mate": CrewRequestRosterRolesValue(
                        name="Rui",
                    ),
                    "engineer": CrewRequestRosterRolesValue(
                        name="Lin",
                    ),
                },
            ),
        )
        """
        _response = self._raw_client.register_crew(vessel=vessel, roster=roster, request_options=request_options)
        return _response.data


class AsyncCrewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrewsClient
        """
        return self._raw_client

    async def register_crew(
        self,
        *,
        vessel: str,
        roster: typing.Optional[CrewRequestRoster] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        vessel : str

        roster : typing.Optional[CrewRequestRoster]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.crews import CrewRequestRoster, CrewRequestRosterRolesValue

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crews.register_crew(
                vessel="Sea Lark",
                roster=CrewRequestRoster(
                    roles={
                        "skipper": CrewRequestRosterRolesValue(
                            name="Ada",
                        ),
                        "mate": CrewRequestRosterRolesValue(
                            name="Rui",
                        ),
                        "engineer": CrewRequestRosterRolesValue(
                            name="Lin",
                        ),
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_crew(vessel=vessel, roster=roster, request_options=request_options)
        return _response.data
