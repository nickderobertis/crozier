

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.activities_filter import ActivitiesFilter
from ..types.activity_attendee import ActivityAttendee
from ..types.activity_show_as import ActivityShowAs
from ..types.activity_type import ActivityType
from ..types.address import Address
from ..types.create_activity_response import CreateActivityResponse
from ..types.custom_field import CustomField
from ..types.delete_activity_response import DeleteActivityResponse
from ..types.get_activities_response import GetActivitiesResponse
from ..types.get_activity_response import GetActivityResponse
from ..types.update_activity_response import UpdateActivityResponse
from .raw_client import AsyncRawActivitiesClient, RawActivitiesClient


OMIT = typing.cast(typing.Any, ...)


class ActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivitiesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ActivitiesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetActivitiesResponse:
        """
        List activities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ActivitiesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActivitiesResponse
            Activities

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.activities.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, filter=filter, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateActivityResponse:
        """
        Create activity

        Parameters
        ----------
        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateActivityResponse
            Activity created

        Examples
        --------
        from fern import ActivityType, FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.activities.add(
            type=ActivityType.CALL,
        )
        """
        _response = self._raw_client.add(
            type=type,
            raw=raw,
            account_id=account_id,
            activity_date=activity_date,
            activity_datetime=activity_datetime,
            all_day_event=all_day_event,
            archived=archived,
            asset_id=asset_id,
            attendees=attendees,
            campaign_id=campaign_id,
            case_id=case_id,
            child=child,
            company_id=company_id,
            contact_id=contact_id,
            contract_id=contract_id,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            custom_object_id=custom_object_id,
            deleted=deleted,
            description=description,
            done=done,
            downstream_id=downstream_id,
            duration_minutes=duration_minutes,
            duration_seconds=duration_seconds,
            end_date=end_date,
            end_datetime=end_datetime,
            event_sub_type=event_sub_type,
            group_event=group_event,
            group_event_type=group_event_type,
            id=id,
            lead_id=lead_id,
            location=location,
            location_address=location_address,
            note=note,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            private=private,
            product_id=product_id,
            recurrent=recurrent,
            reminder_datetime=reminder_datetime,
            reminder_set=reminder_set,
            show_as=show_as,
            solution_id=solution_id,
            start_datetime=start_datetime,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            user_id=user_id,
            video_conference_id=video_conference_id,
            video_conference_url=video_conference_url,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetActivityResponse:
        """
        Get activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActivityResponse
            Activity

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.activities.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteActivityResponse:
        """
        Delete activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteActivityResponse
            Activity deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.activities.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateActivityResponse:
        """
        Update activity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateActivityResponse
            Activity updated

        Examples
        --------
        from fern import ActivityType, FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.activities.update(
            id_="id",
            type=ActivityType.CALL,
        )
        """
        _response = self._raw_client.update(
            id_,
            type=type,
            raw=raw,
            account_id=account_id,
            activity_date=activity_date,
            activity_datetime=activity_datetime,
            all_day_event=all_day_event,
            archived=archived,
            asset_id=asset_id,
            attendees=attendees,
            campaign_id=campaign_id,
            case_id=case_id,
            child=child,
            company_id=company_id,
            contact_id=contact_id,
            contract_id=contract_id,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            custom_object_id=custom_object_id,
            deleted=deleted,
            description=description,
            done=done,
            downstream_id=downstream_id,
            duration_minutes=duration_minutes,
            duration_seconds=duration_seconds,
            end_date=end_date,
            end_datetime=end_datetime,
            event_sub_type=event_sub_type,
            group_event=group_event,
            group_event_type=group_event_type,
            id=id,
            lead_id=lead_id,
            location=location,
            location_address=location_address,
            note=note,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            private=private,
            product_id=product_id,
            recurrent=recurrent,
            reminder_datetime=reminder_datetime,
            reminder_set=reminder_set,
            show_as=show_as,
            solution_id=solution_id,
            start_datetime=start_datetime,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            user_id=user_id,
            video_conference_id=video_conference_id,
            video_conference_url=video_conference_url,
            request_options=request_options,
        )
        return _response.data


class AsyncActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivitiesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ActivitiesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetActivitiesResponse:
        """
        List activities

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ActivitiesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActivitiesResponse
            Activities

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activities.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, filter=filter, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateActivityResponse:
        """
        Create activity

        Parameters
        ----------
        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateActivityResponse
            Activity created

        Examples
        --------
        import asyncio

        from fern import ActivityType, AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activities.add(
                type=ActivityType.CALL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            type=type,
            raw=raw,
            account_id=account_id,
            activity_date=activity_date,
            activity_datetime=activity_datetime,
            all_day_event=all_day_event,
            archived=archived,
            asset_id=asset_id,
            attendees=attendees,
            campaign_id=campaign_id,
            case_id=case_id,
            child=child,
            company_id=company_id,
            contact_id=contact_id,
            contract_id=contract_id,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            custom_object_id=custom_object_id,
            deleted=deleted,
            description=description,
            done=done,
            downstream_id=downstream_id,
            duration_minutes=duration_minutes,
            duration_seconds=duration_seconds,
            end_date=end_date,
            end_datetime=end_datetime,
            event_sub_type=event_sub_type,
            group_event=group_event,
            group_event_type=group_event_type,
            id=id,
            lead_id=lead_id,
            location=location,
            location_address=location_address,
            note=note,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            private=private,
            product_id=product_id,
            recurrent=recurrent,
            reminder_datetime=reminder_datetime,
            reminder_set=reminder_set,
            show_as=show_as,
            solution_id=solution_id,
            start_datetime=start_datetime,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            user_id=user_id,
            video_conference_id=video_conference_id,
            video_conference_url=video_conference_url,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetActivityResponse:
        """
        Get activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActivityResponse
            Activity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activities.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteActivityResponse:
        """
        Delete activity

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteActivityResponse
            Activity deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activities.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        type: ActivityType,
        raw: typing.Optional[bool] = None,
        account_id: typing.Optional[str] = OMIT,
        activity_date: typing.Optional[str] = OMIT,
        activity_datetime: typing.Optional[str] = OMIT,
        all_day_event: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        attendees: typing.Optional[typing.Sequence[ActivityAttendee]] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        case_id: typing.Optional[str] = OMIT,
        child: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        contract_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        custom_object_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        done: typing.Optional[bool] = OMIT,
        downstream_id: typing.Optional[str] = OMIT,
        duration_minutes: typing.Optional[int] = OMIT,
        duration_seconds: typing.Optional[int] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        end_datetime: typing.Optional[str] = OMIT,
        event_sub_type: typing.Optional[str] = OMIT,
        group_event: typing.Optional[bool] = OMIT,
        group_event_type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        location_address: typing.Optional[Address] = OMIT,
        note: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        private: typing.Optional[bool] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        recurrent: typing.Optional[bool] = OMIT,
        reminder_datetime: typing.Optional[str] = OMIT,
        reminder_set: typing.Optional[bool] = OMIT,
        show_as: typing.Optional[ActivityShowAs] = OMIT,
        solution_id: typing.Optional[str] = OMIT,
        start_datetime: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        video_conference_id: typing.Optional[str] = OMIT,
        video_conference_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateActivityResponse:
        """
        Update activity

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        type : ActivityType

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account_id : typing.Optional[str]

        activity_date : typing.Optional[str]

        activity_datetime : typing.Optional[str]

        all_day_event : typing.Optional[bool]

        archived : typing.Optional[bool]

        asset_id : typing.Optional[str]

        attendees : typing.Optional[typing.Sequence[ActivityAttendee]]

        campaign_id : typing.Optional[str]

        case_id : typing.Optional[str]

        child : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        contract_id : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        custom_object_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        done : typing.Optional[bool]
            Whether the Activity is done or not

        downstream_id : typing.Optional[str]
            The third-party API ID of original entity

        duration_minutes : typing.Optional[int]

        duration_seconds : typing.Optional[int]

        end_date : typing.Optional[str]

        end_datetime : typing.Optional[str]

        event_sub_type : typing.Optional[str]

        group_event : typing.Optional[bool]

        group_event_type : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        location : typing.Optional[str]

        location_address : typing.Optional[Address]

        note : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        private : typing.Optional[bool]

        product_id : typing.Optional[str]

        recurrent : typing.Optional[bool]

        reminder_datetime : typing.Optional[str]

        reminder_set : typing.Optional[bool]

        show_as : typing.Optional[ActivityShowAs]

        solution_id : typing.Optional[str]

        start_datetime : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        user_id : typing.Optional[str]

        video_conference_id : typing.Optional[str]

        video_conference_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateActivityResponse
            Activity updated

        Examples
        --------
        import asyncio

        from fern import ActivityType, AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.activities.update(
                id_="id",
                type=ActivityType.CALL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            type=type,
            raw=raw,
            account_id=account_id,
            activity_date=activity_date,
            activity_datetime=activity_datetime,
            all_day_event=all_day_event,
            archived=archived,
            asset_id=asset_id,
            attendees=attendees,
            campaign_id=campaign_id,
            case_id=case_id,
            child=child,
            company_id=company_id,
            contact_id=contact_id,
            contract_id=contract_id,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            custom_object_id=custom_object_id,
            deleted=deleted,
            description=description,
            done=done,
            downstream_id=downstream_id,
            duration_minutes=duration_minutes,
            duration_seconds=duration_seconds,
            end_date=end_date,
            end_datetime=end_datetime,
            event_sub_type=event_sub_type,
            group_event=group_event,
            group_event_type=group_event_type,
            id=id,
            lead_id=lead_id,
            location=location,
            location_address=location_address,
            note=note,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            private=private,
            product_id=product_id,
            recurrent=recurrent,
            reminder_datetime=reminder_datetime,
            reminder_set=reminder_set,
            show_as=show_as,
            solution_id=solution_id,
            start_datetime=start_datetime,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            user_id=user_id,
            video_conference_id=video_conference_id,
            video_conference_url=video_conference_url,
            request_options=request_options,
        )
        return _response.data
