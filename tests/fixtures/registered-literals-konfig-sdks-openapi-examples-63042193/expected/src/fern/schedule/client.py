

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schedule_create_new_schedule_response import ScheduleCreateNewScheduleResponse
from ..types.schedule_get_all_schedules_response import ScheduleGetAllSchedulesResponse
from ..types.schedule_get_by_id_response import ScheduleGetByIdResponse
from ..types.schedule_remove_by_id_response import ScheduleRemoveByIdResponse
from ..types.schedule_update_schedule_response import ScheduleUpdateScheduleResponse
from .raw_client import AsyncRawScheduleClient, RawScheduleClient
from .types.schedule_create_new_schedule_request_attribution_actor import (
    ScheduleCreateNewScheduleRequestAttributionActor,
)
from .types.schedule_create_new_schedule_request_parameters_value import ScheduleCreateNewScheduleRequestParametersValue
from .types.schedule_create_new_schedule_request_timetable import ScheduleCreateNewScheduleRequestTimetable
from .types.schedule_update_schedule_request_attribution_actor import ScheduleUpdateScheduleRequestAttributionActor
from .types.schedule_update_schedule_request_parameters_value import ScheduleUpdateScheduleRequestParametersValue
from .types.schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable


OMIT = typing.cast(typing.Any, ...)


class ScheduleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScheduleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScheduleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScheduleClient
        """
        return self._raw_client

    def getallschedules(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleGetAllSchedulesResponse:
        """
        Returns all schedules for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleGetAllSchedulesResponse
            A sequence of schedules.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.schedule.getallschedules(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getallschedules(
            project_slug, page_token=page_token, request_options=request_options
        )
        return _response.data

    def createnewschedule(
        self,
        project_slug: str,
        *,
        parameters: typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
        name: str,
        timetable: ScheduleCreateNewScheduleRequestTimetable,
        attribution_actor: ScheduleCreateNewScheduleRequestAttributionActor,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleCreateNewScheduleResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : str
            Name of the schedule.

        timetable : ScheduleCreateNewScheduleRequestTimetable
            Timetable that specifies when a schedule triggers.

        attribution_actor : ScheduleCreateNewScheduleRequestAttributionActor
            The attribution-actor of the scheduled pipeline.

        description : typing.Optional[str]
            Description of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleCreateNewScheduleResponse
            A schedule object.

        Examples
        --------
        from fern.schedule import (
            ScheduleCreateNewScheduleRequestAttributionActor,
            ScheduleCreateNewScheduleRequestTimetableZero,
            ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.schedule.createnewschedule(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            parameters={"deploy_prod": True, "branch": "feature/design-new-api"},
            name="name",
            timetable=ScheduleCreateNewScheduleRequestTimetableZero(
                per_hour=1,
                hours_of_day=[1],
                days_of_week=[
                    ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem.TUE
                ],
            ),
            attribution_actor=ScheduleCreateNewScheduleRequestAttributionActor.CURRENT,
        )
        """
        _response = self._raw_client.createnewschedule(
            project_slug,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def getbyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleGetByIdResponse:
        """
        Get a schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleGetByIdResponse
            A schedule object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.schedule.getbyid(
            schedule_id="schedule-id",
        )
        """
        _response = self._raw_client.getbyid(schedule_id, request_options=request_options)
        return _response.data

    def removebyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleRemoveByIdResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleRemoveByIdResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.schedule.removebyid(
            schedule_id="schedule-id",
        )
        """
        _response = self._raw_client.removebyid(schedule_id, request_options=request_options)
        return _response.data

    def updateschedule(
        self,
        schedule_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]] = OMIT,
        name: typing.Optional[str] = OMIT,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = OMIT,
        attribution_actor: typing.Optional[ScheduleUpdateScheduleRequestAttributionActor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleUpdateScheduleResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        description : typing.Optional[str]
            Description of the schedule.

        parameters : typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : typing.Optional[str]
            Name of the schedule.

        timetable : typing.Optional[ScheduleUpdateScheduleRequestTimetable]
            Timetable that specifies when a schedule triggers.

        attribution_actor : typing.Optional[ScheduleUpdateScheduleRequestAttributionActor]
            The attribution-actor of the scheduled pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleUpdateScheduleResponse
            A schedule object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.schedule.updateschedule(
            schedule_id="schedule-id",
        )
        """
        _response = self._raw_client.updateschedule(
            schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
            request_options=request_options,
        )
        return _response.data


class AsyncScheduleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScheduleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScheduleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScheduleClient
        """
        return self._raw_client

    async def getallschedules(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleGetAllSchedulesResponse:
        """
        Returns all schedules for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleGetAllSchedulesResponse
            A sequence of schedules.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.schedule.getallschedules(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getallschedules(
            project_slug, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def createnewschedule(
        self,
        project_slug: str,
        *,
        parameters: typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue],
        name: str,
        timetable: ScheduleCreateNewScheduleRequestTimetable,
        attribution_actor: ScheduleCreateNewScheduleRequestAttributionActor,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleCreateNewScheduleResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : str
            Name of the schedule.

        timetable : ScheduleCreateNewScheduleRequestTimetable
            Timetable that specifies when a schedule triggers.

        attribution_actor : ScheduleCreateNewScheduleRequestAttributionActor
            The attribution-actor of the scheduled pipeline.

        description : typing.Optional[str]
            Description of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleCreateNewScheduleResponse
            A schedule object.

        Examples
        --------
        import asyncio

        from fern.schedule import (
            ScheduleCreateNewScheduleRequestAttributionActor,
            ScheduleCreateNewScheduleRequestTimetableZero,
            ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.schedule.createnewschedule(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                parameters={"deploy_prod": True, "branch": "feature/design-new-api"},
                name="name",
                timetable=ScheduleCreateNewScheduleRequestTimetableZero(
                    per_hour=1,
                    hours_of_day=[1],
                    days_of_week=[
                        ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem.TUE
                    ],
                ),
                attribution_actor=ScheduleCreateNewScheduleRequestAttributionActor.CURRENT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createnewschedule(
            project_slug,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def getbyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleGetByIdResponse:
        """
        Get a schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleGetByIdResponse
            A schedule object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.schedule.getbyid(
                schedule_id="schedule-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbyid(schedule_id, request_options=request_options)
        return _response.data

    async def removebyid(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleRemoveByIdResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleRemoveByIdResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.schedule.removebyid(
                schedule_id="schedule-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removebyid(schedule_id, request_options=request_options)
        return _response.data

    async def updateschedule(
        self,
        schedule_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]] = OMIT,
        name: typing.Optional[str] = OMIT,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = OMIT,
        attribution_actor: typing.Optional[ScheduleUpdateScheduleRequestAttributionActor] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleUpdateScheduleResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.

        Parameters
        ----------
        schedule_id : str
            The unique ID of the schedule.

        description : typing.Optional[str]
            Description of the schedule.

        parameters : typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]]
            Pipeline parameters represented as key-value pairs. Must contain branch or tag.

        name : typing.Optional[str]
            Name of the schedule.

        timetable : typing.Optional[ScheduleUpdateScheduleRequestTimetable]
            Timetable that specifies when a schedule triggers.

        attribution_actor : typing.Optional[ScheduleUpdateScheduleRequestAttributionActor]
            The attribution-actor of the scheduled pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleUpdateScheduleResponse
            A schedule object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.schedule.updateschedule(
                schedule_id="schedule-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateschedule(
            schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
            request_options=request_options,
        )
        return _response.data
