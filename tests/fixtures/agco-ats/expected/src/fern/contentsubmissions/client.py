

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_content_submission import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission,
)
from ..types.api_paged_response_content_submission_shared_business_entities_content_submission_attribute import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
)
from ..types.build_system_shared_interfaces_i_job_run import BuildSystemSharedInterfacesIJobRun
from ..types.content_submission_shared_business_entities_content_definition import (
    ContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.content_submission_shared_business_entities_content_submission import (
    ContentSubmissionSharedBusinessEntitiesContentSubmission,
)
from ..types.content_submission_shared_business_entities_content_submission_attribute import (
    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
)
from .raw_client import AsyncRawContentsubmissionsClient, RawContentsubmissionsClient


OMIT = typing.cast(typing.Any, ...)


class ContentsubmissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentsubmissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentsubmissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentsubmissionsClient
        """
        return self._raw_client

    def putcontentsubmissionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
            FernApi,
        )

        client = FernApi()
        client.contentsubmissions.putcontentsubmissionattributes(
            request=[
                ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.putcontentsubmissionattributes(request=request, request_options=request_options)
        return _response.data

    def putcontentsubmissionattributeasync(
        self,
        content_submission_attribute_id: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.putcontentsubmissionattributeasync(
            content_submission_attribute_id=1,
            name="Name",
        )
        """
        _response = self._raw_client.putcontentsubmissionattributeasync(
            content_submission_attribute_id,
            name=name,
            content_submission_id=content_submission_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def deletecontentsubmissionattribute(
        self, content_submission_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.deletecontentsubmissionattribute(
            content_submission_attribute_id=1,
        )
        """
        _response = self._raw_client.deletecontentsubmissionattribute(
            content_submission_attribute_id, request_options=request_options
        )
        return _response.data

    def getcontentsubmissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        release_id: typing.Optional[int] = None,
        type_id: typing.Optional[int] = None,
        version: typing.Optional[int] = None,
        include_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission:
        """
        Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]=Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        release_id : typing.Optional[int]
            Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.

        type_id : typing.Optional[int]
            Optional. Filter submissions by their ContentDefinition's Type ID.

        version : typing.Optional[int]
            Optional. Filter submissions by their Version.

        include_definition : typing.Optional[bool]
            Optional. If true, includes the ContentDefinition for each submission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.getcontentsubmissions()
        """
        _response = self._raw_client.getcontentsubmissions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            content_definition_id=content_definition_id,
            include_attributes=include_attributes,
            release_id=release_id,
            type_id=type_id,
            version=version,
            include_definition=include_definition,
            request_options=request_options,
        )
        return _response.data

    def postcontentsubmission(
        self,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.
                    The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response
                    is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.postcontentsubmission()
        """
        _response = self._raw_client.postcontentsubmission(
            attributes=attributes,
            build_id=build_id,
            content_definition_id=content_definition_id,
            content_submission_id=content_submission_id,
            definition=definition,
            job_run_id=job_run_id,
            package_id=package_id,
            release_notes=release_notes,
            repository=repository,
            revision=revision,
            submission_date=submission_date,
            user_id=user_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def getcontentsubmission(
        self,
        content_submission_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSubmissionSharedBusinessEntitiesContentSubmission:
        """
        Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentSubmission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.getcontentsubmission(
            content_submission_id=1,
        )
        """
        _response = self._raw_client.getcontentsubmission(
            content_submission_id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    def putcontentsubmission(
        self,
        content_submission_id_: int,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission to update

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.putcontentsubmission(
            content_submission_id_=1,
        )
        """
        _response = self._raw_client.putcontentsubmission(
            content_submission_id_,
            attributes=attributes,
            build_id=build_id,
            content_definition_id=content_definition_id,
            content_submission_id=content_submission_id,
            definition=definition,
            job_run_id=job_run_id,
            package_id=package_id,
            release_notes=release_notes,
            repository=repository,
            revision=revision,
            submission_date=submission_date,
            user_id=user_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def deletecontentsubmission(
        self, content_submission_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.deletecontentsubmission(
            content_submission_id=1,
        )
        """
        _response = self._raw_client.deletecontentsubmission(content_submission_id, request_options=request_options)
        return _response.data

    def getcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        name : typing.Optional[str]
            Optional. Filter the attributes by Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.getcontentsubmissionattributes(
            content_submission_id=1,
        )
        """
        _response = self._raw_client.getcontentsubmissionattributes(
            content_submission_id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    def postcontentsubmissionattribute(
        self,
        content_submission_id_: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.postcontentsubmissionattribute(
            content_submission_id_=1,
            name="Name",
        )
        """
        _response = self._raw_client.postcontentsubmissionattribute(
            content_submission_id_,
            name=name,
            content_submission_id=content_submission_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def postcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
            FernApi,
        )

        client = FernApi()
        client.contentsubmissions.postcontentsubmissionattributes(
            content_submission_id=1,
            request=[
                ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.postcontentsubmissionattributes(
            content_submission_id, request=request, request_options=request_options
        )
        return _response.data

    def getcontentsubmissionstatus(
        self,
        content_submission_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedInterfacesIJobRun:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_activity_run_details : typing.Optional[bool]
            True to include all status details if JobRun. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedInterfacesIJobRun
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissions.getcontentsubmissionstatus(
            content_submission_id=1,
        )
        """
        _response = self._raw_client.getcontentsubmissionstatus(
            content_submission_id,
            include_activity_run_details=include_activity_run_details,
            request_options=request_options,
        )
        return _response.data


class AsyncContentsubmissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentsubmissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentsubmissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentsubmissionsClient
        """
        return self._raw_client

    async def putcontentsubmissionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.putcontentsubmissionattributes(
                request=[
                    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentsubmissionattributes(
            request=request, request_options=request_options
        )
        return _response.data

    async def putcontentsubmissionattributeasync(
        self,
        content_submission_attribute_id: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

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
            await client.contentsubmissions.putcontentsubmissionattributeasync(
                content_submission_attribute_id=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentsubmissionattributeasync(
            content_submission_attribute_id,
            name=name,
            content_submission_id=content_submission_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentsubmissionattribute(
        self, content_submission_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_attribute_id : int
            The ID of the Attribute to remove.

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
            await client.contentsubmissions.deletecontentsubmissionattribute(
                content_submission_attribute_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentsubmissionattribute(
            content_submission_attribute_id, request_options=request_options
        )
        return _response.data

    async def getcontentsubmissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        release_id: typing.Optional[int] = None,
        type_id: typing.Optional[int] = None,
        version: typing.Optional[int] = None,
        include_definition: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission:
        """
        Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]=Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        release_id : typing.Optional[int]
            Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.

        type_id : typing.Optional[int]
            Optional. Filter submissions by their ContentDefinition's Type ID.

        version : typing.Optional[int]
            Optional. Filter submissions by their Version.

        include_definition : typing.Optional[bool]
            Optional. If true, includes the ContentDefinition for each submission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.getcontentsubmissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmissions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            content_definition_id=content_definition_id,
            include_attributes=include_attributes,
            release_id=release_id,
            type_id=type_id,
            version=version,
            include_definition=include_definition,
            request_options=request_options,
        )
        return _response.data

    async def postcontentsubmission(
        self,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.
                    The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response
                    is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.postcontentsubmission()


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentsubmission(
            attributes=attributes,
            build_id=build_id,
            content_definition_id=content_definition_id,
            content_submission_id=content_submission_id,
            definition=definition,
            job_run_id=job_run_id,
            package_id=package_id,
            release_notes=release_notes,
            repository=repository,
            revision=revision,
            submission_date=submission_date,
            user_id=user_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def getcontentsubmission(
        self,
        content_submission_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSubmissionSharedBusinessEntitiesContentSubmission:
        """
        Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentSubmission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.getcontentsubmission(
                content_submission_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmission(
            content_submission_id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    async def putcontentsubmission(
        self,
        content_submission_id_: int,
        *,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]
        ] = OMIT,
        build_id: typing.Optional[int] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        content_submission_id: typing.Optional[int] = OMIT,
        definition: typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        release_notes: typing.Optional[str] = OMIT,
        repository: typing.Optional[str] = OMIT,
        revision: typing.Optional[int] = OMIT,
        submission_date: typing.Optional[dt.datetime] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission to update

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]]
            Attributes of this ContentSubmission

        build_id : typing.Optional[int]
            ReadOnly. The ID of the Azure DevOps Build which will build the content package.

        content_definition_id : typing.Optional[int]
            The ID of the Content Definition.

        content_submission_id : typing.Optional[int]
            The ID of this Content Submission.

        definition : typing.Optional[ContentSubmissionSharedBusinessEntitiesContentDefinition]
            The ContentDefinition for this ContentSubmission

        job_run_id : typing.Optional[int]
            ReadOnly. The ID of the JobRun which will build the content package.

        package_id : typing.Optional[str]
            The ID of package generated by this content submission.

        release_notes : typing.Optional[str]
            Release Notes for this ContentSubmission

        repository : typing.Optional[str]
            The SVN repository used as the source of this content submission

        revision : typing.Optional[int]
            The SVN revision used as the source of this content submission.

        submission_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time the content submission was made.

        user_id : typing.Optional[int]
            Read Only. The ID of the user who submitted the content

        version : typing.Optional[int]
            Optional.  The version number assigned to this Content Submission and the resulting Package.
                        If not provided, version shall be 1 if it is the first content submission for the
                        ContentDefinitionID otherwise it shall be the highest content submission version for the
                        specified ContentDefinitionID incremented by 1.

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
            await client.contentsubmissions.putcontentsubmission(
                content_submission_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentsubmission(
            content_submission_id_,
            attributes=attributes,
            build_id=build_id,
            content_definition_id=content_definition_id,
            content_submission_id=content_submission_id,
            definition=definition,
            job_run_id=job_run_id,
            package_id=package_id,
            release_notes=release_notes,
            repository=repository,
            revision=revision,
            submission_date=submission_date,
            user_id=user_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentsubmission(
        self, content_submission_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to delete

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
            await client.contentsubmissions.deletecontentsubmission(
                content_submission_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentsubmission(
            content_submission_id, request_options=request_options
        )
        return _response.data

    async def getcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        name : typing.Optional[str]
            Optional. Filter the attributes by Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.getcontentsubmissionattributes(
                content_submission_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmissionattributes(
            content_submission_id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    async def postcontentsubmissionattribute(
        self,
        content_submission_id_: int,
        *,
        name: str,
        content_submission_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id_ : int
            The ID of the ContentSubmission

        name : str
            The name of this Attribute.

        content_submission_id : typing.Optional[int]
            The ID of the content submission to which this attribute belongs.

        id : typing.Optional[int]
            The ID of this attribute.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.postcontentsubmissionattribute(
                content_submission_id_=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentsubmissionattribute(
            content_submission_id_,
            name=name,
            content_submission_id=content_submission_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def postcontentsubmissionattributes(
        self,
        content_submission_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.postcontentsubmissionattributes(
                content_submission_id=1,
                request=[
                    ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentsubmissionattributes(
            content_submission_id, request=request, request_options=request_options
        )
        return _response.data

    async def getcontentsubmissionstatus(
        self,
        content_submission_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedInterfacesIJobRun:
        """
        No Documentation Found.

        Parameters
        ----------
        content_submission_id : int
            The ID of the ContentSubmission to get.

        include_activity_run_details : typing.Optional[bool]
            True to include all status details if JobRun. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedInterfacesIJobRun
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissions.getcontentsubmissionstatus(
                content_submission_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmissionstatus(
            content_submission_id,
            include_activity_run_details=include_activity_run_details,
            request_options=request_options,
        )
        return _response.data
