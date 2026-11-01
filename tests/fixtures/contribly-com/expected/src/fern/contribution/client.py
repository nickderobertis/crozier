

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assignment import Assignment
from ..types.contribution import Contribution
from ..types.export import Export
from ..types.export_summary import ExportSummary
from ..types.flag import Flag
from ..types.media_usage import MediaUsage
from ..types.moderation_action import ModerationAction
from ..types.moderation_history_item import ModerationHistoryItem
from ..types.place import Place
from ..types.via import Via
from .raw_client import AsyncRawContributionClient, RawContributionClient


OMIT = typing.cast(typing.Any, ...)


class ContributionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContributionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContributionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContributionClient
        """
        return self._raw_client

    def list_valid_contribution_refinement_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            An array of refinement types. These are the possible values of the get contribution refinements parameter.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.list_valid_contribution_refinement_types()
        """
        _response = self._raw_client.list_valid_contribution_refinement_types(request_options=request_options)
        return _response.data

    def list_contribution_refinement_options(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        refinements: typing.Optional[str] = None,
        refinement_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.List[str]]:
        """
        Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        refinements : typing.Optional[str]
            Comma seperated list of refinement names.

        refinement_size : typing.Optional[float]
            Number of refinement options to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[str]]
            A map of refinement names to lists of options

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.list_contribution_refinement_options()
        """
        _response = self._raw_client.list_contribution_refinement_options(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            refinements=refinements,
            refinement_size=refinement_size,
            request_options=request_options,
        )
        return _response.data

    def list_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_day: typing.Optional[dt.date] = None,
        created_month: typing.Optional[str] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Contribution]:
        """
        Retrieve contributions.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        created_day : typing.Optional[dt.date]
            Limit results to contributions created on this day.

        created_month : typing.Optional[str]
            Limit results to contributions created during this month.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        ids : typing.Optional[str]
            Restrict results to a list of specific contributions identified by a comma seperated list of ids.

        format : typing.Optional[str]
            Select output format. 'json' or 'rss'. Defaults to JSON.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Contribution]
            A list of contributions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.list_contributions()
        """
        _response = self._raw_client.list_contributions(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            created_day=created_day,
            created_month=created_month,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            ids=ids,
            format=format,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_contribution(
        self,
        *,
        assignment: typing.Optional[Assignment] = OMIT,
        attribution: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_usages: typing.Optional[typing.Sequence[MediaUsage]] = OMIT,
        moderation_history: typing.Optional[typing.Sequence[ModerationHistoryItem]] = OMIT,
        place: typing.Optional[Place] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        via: typing.Optional[Via] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contribution:
        """
        Parameters
        ----------
        assignment : typing.Optional[Assignment]

        attribution : typing.Optional[str]
            The public attribution for this contribution. This will be the display name of the registered user or the contributor's first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.

        body : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        id : typing.Optional[str]

        media_usages : typing.Optional[typing.Sequence[MediaUsage]]

        moderation_history : typing.Optional[typing.Sequence[ModerationHistoryItem]]

        place : typing.Optional[Place]

        url_words : typing.Optional[str]

        via : typing.Optional[Via]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            Contribution created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.create_a_new_contribution()
        """
        _response = self._raw_client.create_a_new_contribution(
            assignment=assignment,
            attribution=attribution,
            body=body,
            created=created,
            headline=headline,
            id=id,
            media_usages=media_usages,
            moderation_history=moderation_history,
            place=place,
            url_words=url_words,
            via=via,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_contribution_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Contribution:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            Successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.get_a_single_contribution_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_contribution_by_id(id, request_options=request_options)
        return _response.data

    def delete_this_contribution(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Contribution:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            The deletion request has been accepted and will be processed in the background.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.delete_this_contribution(
            id="id",
        )
        """
        _response = self._raw_client.delete_this_contribution(id, request_options=request_options)
        return _response.data

    def raise_a_flag_against_this_contribution(
        self,
        id_: str,
        *,
        date: typing.Optional[dt.datetime] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Flag:
        """
        Allows end users to bring potential issues with publicly visible content to the attention of moderators.

        Parameters
        ----------
        id_ : str
            Id of the contribution to flag

        date : typing.Optional[dt.datetime]

        email : typing.Optional[str]

        id : typing.Optional[str]

        notes : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Flag
            Flag created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.raise_a_flag_against_this_contribution(
            id_="id",
        )
        """
        _response = self._raw_client.raise_a_flag_against_this_contribution(
            id_, date=date, email=email, id=id, notes=notes, type=type, request_options=request_options
        )
        return _response.data

    def allows_a_user_to_mark_a_contribution_as_liked(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            The updated like count for this contribution.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.allows_a_user_to_mark_a_contribution_as_liked(
            id="id",
        )
        """
        _response = self._raw_client.allows_a_user_to_mark_a_contribution_as_liked(id, request_options=request_options)
        return _response.data

    def list_users_who_have_liked_this_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns a list of user ids of users who have liked this conribution

        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            A list of user ids.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.list_users_who_have_liked_this_contributions(
            id="id",
        )
        """
        _response = self._raw_client.list_users_who_have_liked_this_contributions(id, request_options=request_options)
        return _response.data

    def perform_a_moderation_action_on_this_contribution(
        self,
        id: str,
        *,
        action: typing.Optional[ModerationAction] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Allows the contribution to approved of rejected.

        Parameters
        ----------
        id : str
            Id of the contribution to moderate

        action : typing.Optional[ModerationAction]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The moderation action was successfully applied

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.perform_a_moderation_action_on_this_contribution(
            id="id",
        )
        """
        _response = self._raw_client.perform_a_moderation_action_on_this_contribution(
            id, action=action, notes=notes, request_options=request_options
        )
        return _response.data

    def export_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        tagged: typing.Optional[bool] = None,
        combined: typing.Optional[bool] = None,
        individual: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        json: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Export:
        """
        Begin an export job. Returns a export job which can be polled to follow the progress of an export.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        tagged : typing.Optional[bool]
            Should exported media files be tagged with metadata. Deprecated; use format instead.

        combined : typing.Optional[bool]
            Included a combined file with all contribution text.

        individual : typing.Optional[bool]
            Include individual text files for each contribution.

        format : typing.Optional[str]
            Media format to export; none, fullsize, tagged or original.

        json : typing.Optional[bool]
            Include raw JSON for each contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export
            An export job describing the state of an export job.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.export_contributions()
        """
        _response = self._raw_client.export_contributions(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            tagged=tagged,
            combined=combined,
            individual=individual,
            format=format,
            json=json,
            request_options=request_options,
        )
        return _response.data

    def export_contributions_preflight_summary(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportSummary:
        """
        Provide a preflight summary of an export request.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportSummary
            A summary of the number of contributions, media files and approximate total size of media files.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.export_contributions_preflight_summary()
        """
        _response = self._raw_client.export_contributions_preflight_summary(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_export_job_poll_to_follow_export_progress(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Export:
        """
        Parameters
        ----------
        id : str
            Id of the export job to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export
            Successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contribution.get_a_single_export_job_poll_to_follow_export_progress(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_export_job_poll_to_follow_export_progress(
            id, request_options=request_options
        )
        return _response.data


class AsyncContributionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContributionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContributionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContributionClient
        """
        return self._raw_client

    async def list_valid_contribution_refinement_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            An array of refinement types. These are the possible values of the get contribution refinements parameter.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.list_valid_contribution_refinement_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_valid_contribution_refinement_types(request_options=request_options)
        return _response.data

    async def list_contribution_refinement_options(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        refinements: typing.Optional[str] = None,
        refinement_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.List[str]]:
        """
        Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        refinements : typing.Optional[str]
            Comma seperated list of refinement names.

        refinement_size : typing.Optional[float]
            Number of refinement options to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[str]]
            A map of refinement names to lists of options

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.list_contribution_refinement_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_contribution_refinement_options(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            refinements=refinements,
            refinement_size=refinement_size,
            request_options=request_options,
        )
        return _response.data

    async def list_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_day: typing.Optional[dt.date] = None,
        created_month: typing.Optional[str] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Contribution]:
        """
        Retrieve contributions.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        created_day : typing.Optional[dt.date]
            Limit results to contributions created on this day.

        created_month : typing.Optional[str]
            Limit results to contributions created during this month.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        ids : typing.Optional[str]
            Restrict results to a list of specific contributions identified by a comma seperated list of ids.

        format : typing.Optional[str]
            Select output format. 'json' or 'rss'. Defaults to JSON.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Contribution]
            A list of contributions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.list_contributions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_contributions(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            created_day=created_day,
            created_month=created_month,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            ids=ids,
            format=format,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_contribution(
        self,
        *,
        assignment: typing.Optional[Assignment] = OMIT,
        attribution: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_usages: typing.Optional[typing.Sequence[MediaUsage]] = OMIT,
        moderation_history: typing.Optional[typing.Sequence[ModerationHistoryItem]] = OMIT,
        place: typing.Optional[Place] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        via: typing.Optional[Via] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contribution:
        """
        Parameters
        ----------
        assignment : typing.Optional[Assignment]

        attribution : typing.Optional[str]
            The public attribution for this contribution. This will be the display name of the registered user or the contributor's first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.

        body : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        id : typing.Optional[str]

        media_usages : typing.Optional[typing.Sequence[MediaUsage]]

        moderation_history : typing.Optional[typing.Sequence[ModerationHistoryItem]]

        place : typing.Optional[Place]

        url_words : typing.Optional[str]

        via : typing.Optional[Via]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            Contribution created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.create_a_new_contribution()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_contribution(
            assignment=assignment,
            attribution=attribution,
            body=body,
            created=created,
            headline=headline,
            id=id,
            media_usages=media_usages,
            moderation_history=moderation_history,
            place=place,
            url_words=url_words,
            via=via,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_contribution_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Contribution:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            Successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.get_a_single_contribution_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_contribution_by_id(id, request_options=request_options)
        return _response.data

    async def delete_this_contribution(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Contribution:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contribution
            The deletion request has been accepted and will be processed in the background.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.delete_this_contribution(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_this_contribution(id, request_options=request_options)
        return _response.data

    async def raise_a_flag_against_this_contribution(
        self,
        id_: str,
        *,
        date: typing.Optional[dt.datetime] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Flag:
        """
        Allows end users to bring potential issues with publicly visible content to the attention of moderators.

        Parameters
        ----------
        id_ : str
            Id of the contribution to flag

        date : typing.Optional[dt.datetime]

        email : typing.Optional[str]

        id : typing.Optional[str]

        notes : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Flag
            Flag created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.raise_a_flag_against_this_contribution(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.raise_a_flag_against_this_contribution(
            id_, date=date, email=email, id=id, notes=notes, type=type, request_options=request_options
        )
        return _response.data

    async def allows_a_user_to_mark_a_contribution_as_liked(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            The updated like count for this contribution.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.allows_a_user_to_mark_a_contribution_as_liked(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.allows_a_user_to_mark_a_contribution_as_liked(
            id, request_options=request_options
        )
        return _response.data

    async def list_users_who_have_liked_this_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns a list of user ids of users who have liked this conribution

        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            A list of user ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.list_users_who_have_liked_this_contributions(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users_who_have_liked_this_contributions(
            id, request_options=request_options
        )
        return _response.data

    async def perform_a_moderation_action_on_this_contribution(
        self,
        id: str,
        *,
        action: typing.Optional[ModerationAction] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Allows the contribution to approved of rejected.

        Parameters
        ----------
        id : str
            Id of the contribution to moderate

        action : typing.Optional[ModerationAction]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The moderation action was successfully applied

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.perform_a_moderation_action_on_this_contribution(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_a_moderation_action_on_this_contribution(
            id, action=action, notes=notes, request_options=request_options
        )
        return _response.data

    async def export_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        tagged: typing.Optional[bool] = None,
        combined: typing.Optional[bool] = None,
        individual: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        json: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Export:
        """
        Begin an export job. Returns a export job which can be polled to follow the progress of an export.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        tagged : typing.Optional[bool]
            Should exported media files be tagged with metadata. Deprecated; use format instead.

        combined : typing.Optional[bool]
            Included a combined file with all contribution text.

        individual : typing.Optional[bool]
            Include individual text files for each contribution.

        format : typing.Optional[str]
            Media format to export; none, fullsize, tagged or original.

        json : typing.Optional[bool]
            Include raw JSON for each contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export
            An export job describing the state of an export job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.export_contributions()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_contributions(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            tagged=tagged,
            combined=combined,
            individual=individual,
            format=format,
            json=json,
            request_options=request_options,
        )
        return _response.data

    async def export_contributions_preflight_summary(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportSummary:
        """
        Provide a preflight summary of an export request.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportSummary
            A summary of the number of contributions, media files and approximate total size of media files.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.export_contributions_preflight_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_contributions_preflight_summary(
            assignment=assignment,
            country=country,
            created_before=created_before,
            created_after=created_after,
            geohash=geohash,
            has_location=has_location,
            lat_long=lat_long,
            radius=radius,
            media_type=media_type,
            owned_by=owned_by,
            q=q,
            url_words=url_words,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_export_job_poll_to_follow_export_progress(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Export:
        """
        Parameters
        ----------
        id : str
            Id of the export job to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export
            Successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contribution.get_a_single_export_job_poll_to_follow_export_progress(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_export_job_poll_to_follow_export_progress(
            id, request_options=request_options
        )
        return _response.data
