

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.anonymized import Anonymized
from ..types.applicant_social_links_item import ApplicantSocialLinksItem
from ..types.applicant_websites_item import ApplicantWebsitesItem
from ..types.archived import Archived
from ..types.create_applicant_response import CreateApplicantResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.custom_field import CustomField
from ..types.deleted import Deleted
from ..types.deleted_at import DeletedAt
from ..types.deleted_by import DeletedBy
from ..types.email import Email
from ..types.get_applicant_response import GetApplicantResponse
from ..types.get_applicants_response import GetApplicantsResponse
from ..types.id import Id
from ..types.initials import Initials
from ..types.jobs_filter import JobsFilter
from ..types.last_interaction_at import LastInteractionAt
from ..types.owner_id import OwnerId
from ..types.phone_number import PhoneNumber
from ..types.record_url import RecordUrl
from ..types.tags import Tags
from ..types.title import Title
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawApplicantsClient, RawApplicantsClient


OMIT = typing.cast(typing.Any, ...)


class ApplicantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicantsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[JobsFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApplicantsResponse:
        """
        List applicants

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[JobsFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicantsResponse
            Applicants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.applicants.all_(
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        anonymized: typing.Optional[Anonymized] = OMIT,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        archived: typing.Optional[Archived] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        confidential: typing.Optional[bool] = OMIT,
        coordinator_id: typing.Optional[str] = OMIT,
        cover_letter: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        cv_url: typing.Optional[str] = OMIT,
        deleted: typing.Optional[Deleted] = OMIT,
        deleted_at: typing.Optional[DeletedAt] = OMIT,
        deleted_by: typing.Optional[DeletedBy] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        followers: typing.Optional[typing.Sequence[str]] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[Initials] = OMIT,
        job_url: typing.Optional[str] = OMIT,
        last_interaction_at: typing.Optional[LastInteractionAt] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[OwnerId] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        position_id: typing.Optional[str] = OMIT,
        record_url: typing.Optional[RecordUrl] = OMIT,
        recruiter_id: typing.Optional[str] = OMIT,
        rejected_at: typing.Optional[dt.datetime] = OMIT,
        social_links: typing.Optional[typing.Sequence[ApplicantSocialLinksItem]] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        sourced_by: typing.Optional[str] = OMIT,
        sources: typing.Optional[typing.Sequence[str]] = OMIT,
        stage_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[ApplicantWebsitesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApplicantResponse:
        """
        Create applicant

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        anonymized : typing.Optional[Anonymized]

        applications : typing.Optional[typing.Sequence[str]]

        archived : typing.Optional[Archived]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        confidential : typing.Optional[bool]

        coordinator_id : typing.Optional[str]

        cover_letter : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        cv_url : typing.Optional[str]

        deleted : typing.Optional[Deleted]

        deleted_at : typing.Optional[DeletedAt]

        deleted_by : typing.Optional[DeletedBy]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[str]
            The first name of the person.

        followers : typing.Optional[typing.Sequence[str]]

        headline : typing.Optional[str]
            Typically a list of previous companies where the contact has worked or schools that the contact has attended

        id : typing.Optional[Id]

        initials : typing.Optional[Initials]

        job_url : typing.Optional[str]

        last_interaction_at : typing.Optional[LastInteractionAt]

        last_name : typing.Optional[str]
            The last name of the person.

        middle_name : typing.Optional[str]
            Middle name of the person.

        name : typing.Optional[str]
            The name of an applicant.

        owner_id : typing.Optional[OwnerId]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        position_id : typing.Optional[str]
            The PositionId the applicant applied for.

        record_url : typing.Optional[RecordUrl]

        recruiter_id : typing.Optional[str]

        rejected_at : typing.Optional[dt.datetime]

        social_links : typing.Optional[typing.Sequence[ApplicantSocialLinksItem]]

        source_id : typing.Optional[str]

        sourced_by : typing.Optional[str]

        sources : typing.Optional[typing.Sequence[str]]

        stage_id : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[ApplicantWebsitesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApplicantResponse
            Applicants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.applicants.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            addresses=addresses,
            anonymized=anonymized,
            applications=applications,
            archived=archived,
            birthday=birthday,
            confidential=confidential,
            coordinator_id=coordinator_id,
            cover_letter=cover_letter,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            cv_url=cv_url,
            deleted=deleted,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            emails=emails,
            first_name=first_name,
            followers=followers,
            headline=headline,
            id=id,
            initials=initials,
            job_url=job_url,
            last_interaction_at=last_interaction_at,
            last_name=last_name,
            middle_name=middle_name,
            name=name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            position_id=position_id,
            record_url=record_url,
            recruiter_id=recruiter_id,
            rejected_at=rejected_at,
            social_links=social_links,
            source_id=source_id,
            sourced_by=sourced_by,
            sources=sources,
            stage_id=stage_id,
            tags=tags,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
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
    ) -> GetApplicantResponse:
        """
        Get applicant

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
        GetApplicantResponse
            Applicants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.applicants.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data


class AsyncApplicantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicantsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[JobsFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApplicantsResponse:
        """
        List applicants

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[JobsFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicantsResponse
            Applicants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.applicants.all_(
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
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        anonymized: typing.Optional[Anonymized] = OMIT,
        applications: typing.Optional[typing.Sequence[str]] = OMIT,
        archived: typing.Optional[Archived] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        confidential: typing.Optional[bool] = OMIT,
        coordinator_id: typing.Optional[str] = OMIT,
        cover_letter: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        cv_url: typing.Optional[str] = OMIT,
        deleted: typing.Optional[Deleted] = OMIT,
        deleted_at: typing.Optional[DeletedAt] = OMIT,
        deleted_by: typing.Optional[DeletedBy] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        followers: typing.Optional[typing.Sequence[str]] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[Id] = OMIT,
        initials: typing.Optional[Initials] = OMIT,
        job_url: typing.Optional[str] = OMIT,
        last_interaction_at: typing.Optional[LastInteractionAt] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[OwnerId] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        position_id: typing.Optional[str] = OMIT,
        record_url: typing.Optional[RecordUrl] = OMIT,
        recruiter_id: typing.Optional[str] = OMIT,
        rejected_at: typing.Optional[dt.datetime] = OMIT,
        social_links: typing.Optional[typing.Sequence[ApplicantSocialLinksItem]] = OMIT,
        source_id: typing.Optional[str] = OMIT,
        sourced_by: typing.Optional[str] = OMIT,
        sources: typing.Optional[typing.Sequence[str]] = OMIT,
        stage_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[ApplicantWebsitesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApplicantResponse:
        """
        Create applicant

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        anonymized : typing.Optional[Anonymized]

        applications : typing.Optional[typing.Sequence[str]]

        archived : typing.Optional[Archived]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        confidential : typing.Optional[bool]

        coordinator_id : typing.Optional[str]

        cover_letter : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        cv_url : typing.Optional[str]

        deleted : typing.Optional[Deleted]

        deleted_at : typing.Optional[DeletedAt]

        deleted_by : typing.Optional[DeletedBy]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[str]
            The first name of the person.

        followers : typing.Optional[typing.Sequence[str]]

        headline : typing.Optional[str]
            Typically a list of previous companies where the contact has worked or schools that the contact has attended

        id : typing.Optional[Id]

        initials : typing.Optional[Initials]

        job_url : typing.Optional[str]

        last_interaction_at : typing.Optional[LastInteractionAt]

        last_name : typing.Optional[str]
            The last name of the person.

        middle_name : typing.Optional[str]
            Middle name of the person.

        name : typing.Optional[str]
            The name of an applicant.

        owner_id : typing.Optional[OwnerId]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        position_id : typing.Optional[str]
            The PositionId the applicant applied for.

        record_url : typing.Optional[RecordUrl]

        recruiter_id : typing.Optional[str]

        rejected_at : typing.Optional[dt.datetime]

        social_links : typing.Optional[typing.Sequence[ApplicantSocialLinksItem]]

        source_id : typing.Optional[str]

        sourced_by : typing.Optional[str]

        sources : typing.Optional[typing.Sequence[str]]

        stage_id : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[ApplicantWebsitesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateApplicantResponse
            Applicants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.applicants.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            addresses=addresses,
            anonymized=anonymized,
            applications=applications,
            archived=archived,
            birthday=birthday,
            confidential=confidential,
            coordinator_id=coordinator_id,
            cover_letter=cover_letter,
            created_at=created_at,
            created_by=created_by,
            custom_fields=custom_fields,
            cv_url=cv_url,
            deleted=deleted,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            emails=emails,
            first_name=first_name,
            followers=followers,
            headline=headline,
            id=id,
            initials=initials,
            job_url=job_url,
            last_interaction_at=last_interaction_at,
            last_name=last_name,
            middle_name=middle_name,
            name=name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            position_id=position_id,
            record_url=record_url,
            recruiter_id=recruiter_id,
            rejected_at=rejected_at,
            social_links=social_links,
            source_id=source_id,
            sourced_by=sourced_by,
            sources=sources,
            stage_id=stage_id,
            tags=tags,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
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
    ) -> GetApplicantResponse:
        """
        Get applicant

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
        GetApplicantResponse
            Applicants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.applicants.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data
