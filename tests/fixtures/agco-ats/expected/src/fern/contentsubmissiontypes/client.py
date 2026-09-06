

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_submission_shared_business_entities_content_submission_type import (
    ContentSubmissionSharedBusinessEntitiesContentSubmissionType,
)
from .raw_client import AsyncRawContentsubmissiontypesClient, RawContentsubmissiontypesClient


OMIT = typing.cast(typing.Any, ...)


class ContentsubmissiontypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentsubmissiontypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentsubmissiontypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentsubmissiontypesClient
        """
        return self._raw_client

    def getcontentsubmissiontypes(
        self, *, enabled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]:
        """
        No Documentation Found.

        Parameters
        ----------
        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissiontypes.getcontentsubmissiontypes()
        """
        _response = self._raw_client.getcontentsubmissiontypes(enabled=enabled, request_options=request_options)
        return _response.data

    def postcontentsubmissiontype(
        self,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

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
        client.contentsubmissiontypes.postcontentsubmissiontype(
            description="Description",
            name="Name",
        )
        """
        _response = self._raw_client.postcontentsubmissiontype(
            description=description,
            name=name,
            attribute_template=attribute_template,
            build_definition_id=build_definition_id,
            category_template=category_template,
            enabled=enabled,
            id=id,
            inventory_package_id=inventory_package_id,
            job_id=job_id,
            release_notes_description=release_notes_description,
            request_options=request_options,
        )
        return _response.data

    def getcontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesContentSubmissionType:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentSubmissionType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissiontypes.getcontentsubmissiontype(
            id=1,
        )
        """
        _response = self._raw_client.getcontentsubmissiontype(id, request_options=request_options)
        return _response.data

    def putcontentsubmissiontype(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The ID of the Content Submission Type

        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissiontypes.putcontentsubmissiontype(
            id_=1,
            description="Description",
            name="Name",
        )
        """
        _response = self._raw_client.putcontentsubmissiontype(
            id_,
            description=description,
            name=name,
            attribute_template=attribute_template,
            build_definition_id=build_definition_id,
            category_template=category_template,
            enabled=enabled,
            id=id,
            inventory_package_id=inventory_package_id,
            job_id=job_id,
            release_notes_description=release_notes_description,
            request_options=request_options,
        )
        return _response.data

    def deletecontentsubmissiontype(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentsubmissiontypes.deletecontentsubmissiontype(
            id=1,
        )
        """
        _response = self._raw_client.deletecontentsubmissiontype(id, request_options=request_options)
        return _response.data


class AsyncContentsubmissiontypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentsubmissiontypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentsubmissiontypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentsubmissiontypesClient
        """
        return self._raw_client

    async def getcontentsubmissiontypes(
        self, *, enabled: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]:
        """
        No Documentation Found.

        Parameters
        ----------
        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissiontypes.getcontentsubmissiontypes()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmissiontypes(enabled=enabled, request_options=request_options)
        return _response.data

    async def postcontentsubmissiontype(
        self,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

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
            await client.contentsubmissiontypes.postcontentsubmissiontype(
                description="Description",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentsubmissiontype(
            description=description,
            name=name,
            attribute_template=attribute_template,
            build_definition_id=build_definition_id,
            category_template=category_template,
            enabled=enabled,
            id=id,
            inventory_package_id=inventory_package_id,
            job_id=job_id,
            release_notes_description=release_notes_description,
            request_options=request_options,
        )
        return _response.data

    async def getcontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesContentSubmissionType:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentSubmissionType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentsubmissiontypes.getcontentsubmissiontype(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentsubmissiontype(id, request_options=request_options)
        return _response.data

    async def putcontentsubmissiontype(
        self,
        id_: int,
        *,
        description: str,
        name: str,
        attribute_template: typing.Optional[str] = OMIT,
        build_definition_id: typing.Optional[int] = OMIT,
        category_template: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        inventory_package_id: typing.Optional[str] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        release_notes_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The ID of the Content Submission Type

        description : str
            A description for the Content Submission Type

        name : str
            The Name of the Content Submission Type

        attribute_template : typing.Optional[str]
            A template for the Attribute from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        build_definition_id : typing.Optional[int]
            The ID of the Azure DevOps Build Definition for which to create a Build. Either 'BuildDefinitionID' or 'JobID' is required.

        category_template : typing.Optional[str]
            A template for the category from which to read the version of the package installed. The following placeholders are valid: {ContentDefinitionType}, {ContentDefinitionID}, {ContentDefinitionName}

        enabled : typing.Optional[bool]
            Indicates whether this submission type is available to be used

        id : typing.Optional[int]
            The ID of the Content Submission Type

        inventory_package_id : typing.Optional[str]
            The ID of the Inventory Package from which to read the version of the package installed.

        job_id : typing.Optional[int]
            The ID of the JobDefinition for which to initiate a Job. A value of '0' will cause a submission to fail. Either 'BuildDefinitionID' or 'JobID' is required.

        release_notes_description : typing.Optional[str]
            A description of how release notes for this Content Submission Type are used

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
            await client.contentsubmissiontypes.putcontentsubmissiontype(
                id_=1,
                description="Description",
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentsubmissiontype(
            id_,
            description=description,
            name=name,
            attribute_template=attribute_template,
            build_definition_id=build_definition_id,
            category_template=category_template,
            enabled=enabled,
            id=id,
            inventory_package_id=inventory_package_id,
            job_id=job_id,
            release_notes_description=release_notes_description,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentsubmissiontype(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The ID of the Content Submission Type

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
            await client.contentsubmissiontypes.deletecontentsubmissiontype(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentsubmissiontype(id, request_options=request_options)
        return _response.data
