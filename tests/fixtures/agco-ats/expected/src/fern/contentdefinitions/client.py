

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_content_definition import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.api_paged_response_content_submission_shared_business_entities_content_definition_attribute import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
)
from ..types.content_submission_shared_business_entities_content_definition import (
    ContentSubmissionSharedBusinessEntitiesContentDefinition,
)
from ..types.content_submission_shared_business_entities_content_definition_attribute import (
    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
)
from .raw_client import AsyncRawContentdefinitionsClient, RawContentdefinitionsClient


OMIT = typing.cast(typing.Any, ...)


class ContentdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentdefinitionsClient
        """
        return self._raw_client

    def putcontentdefinitionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
            FernApi,
        )

        client = FernApi()
        client.contentdefinitions.putcontentdefinitionattributes(
            request=[
                ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.putcontentdefinitionattributes(request=request, request_options=request_options)
        return _response.data

    def putcontentdefinitionattributeasync(
        self,
        content_definition_attribute_id: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
        client.contentdefinitions.putcontentdefinitionattributeasync(
            content_definition_attribute_id=1,
            name="Name",
        )
        """
        _response = self._raw_client.putcontentdefinitionattributeasync(
            content_definition_attribute_id,
            name=name,
            content_definition_id=content_definition_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def deletecontentdefinitionattribute(
        self, content_definition_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
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
        client.contentdefinitions.deletecontentdefinitionattribute(
            content_definition_attribute_id=1,
        )
        """
        _response = self._raw_client.deletecontentdefinitionattribute(
            content_definition_attribute_id, request_options=request_options
        )
        return _response.data

    def getcontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_id: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition:
        """
        Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        name : typing.Optional[str]
            Optional. Filter by Name. Supports beginning and ending wildcard (*).

        type_id : typing.Optional[int]
            Optional. Filter by TypeID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentdefinitions.getcontentdefinitions()
        """
        _response = self._raw_client.getcontentdefinitions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            include_attributes=include_attributes,
            name=name,
            type_id=type_id,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    def postcontentdefinition(
        self,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.
                    The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the JobID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

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
        client.contentdefinitions.postcontentdefinition(
            description="Description",
        )
        """
        _response = self._raw_client.postcontentdefinition(
            description=description,
            attributes=attributes,
            content_definition_id=content_definition_id,
            name=name,
            package_type_id=package_type_id,
            type_id=type_id,
            request_options=request_options,
        )
        return _response.data

    def getcontentdefinition(
        self,
        content_definition_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSubmissionSharedBusinessEntitiesContentDefinition:
        """
        Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentdefinitions.getcontentdefinition(
            content_definition_id=1,
        )
        """
        _response = self._raw_client.getcontentdefinition(
            content_definition_id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    def putcontentdefinition(
        self,
        content_definition_id_: int,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition to update

        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentdefinitions.putcontentdefinition(
            content_definition_id_=1,
            description="Description",
        )
        """
        _response = self._raw_client.putcontentdefinition(
            content_definition_id_,
            description=description,
            attributes=attributes,
            content_definition_id=content_definition_id,
            name=name,
            package_type_id=package_type_id,
            type_id=type_id,
            request_options=request_options,
        )
        return _response.data

    def deletecontentdefinition(
        self, content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentdefinitions.deletecontentdefinition(
            content_definition_id=1,
        )
        """
        _response = self._raw_client.deletecontentdefinition(content_definition_id, request_options=request_options)
        return _response.data

    def getcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition.

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
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentdefinitions.getcontentdefinitionattributes(
            content_definition_id=1,
        )
        """
        _response = self._raw_client.getcontentdefinitionattributes(
            content_definition_id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    def postcontentdefinitionattribute(
        self,
        content_definition_id_: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
        client.contentdefinitions.postcontentdefinitionattribute(
            content_definition_id_=1,
            name="Name",
        )
        """
        _response = self._raw_client.postcontentdefinitionattribute(
            content_definition_id_,
            name=name,
            content_definition_id=content_definition_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    def postcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
            FernApi,
        )

        client = FernApi()
        client.contentdefinitions.postcontentdefinitionattributes(
            content_definition_id=1,
            request=[
                ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.postcontentdefinitionattributes(
            content_definition_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncContentdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentdefinitionsClient
        """
        return self._raw_client

    async def putcontentdefinitionattributes(
        self,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

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
            ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentdefinitions.putcontentdefinitionattributes(
                request=[
                    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentdefinitionattributes(
            request=request, request_options=request_options
        )
        return _response.data

    async def putcontentdefinitionattributeasync(
        self,
        content_definition_attribute_id: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
            The ID of the Attribute to update.

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            await client.contentdefinitions.putcontentdefinitionattributeasync(
                content_definition_attribute_id=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentdefinitionattributeasync(
            content_definition_attribute_id,
            name=name,
            content_definition_id=content_definition_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentdefinitionattribute(
        self, content_definition_attribute_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_attribute_id : int
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
            await client.contentdefinitions.deletecontentdefinitionattribute(
                content_definition_attribute_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentdefinitionattribute(
            content_definition_attribute_id, request_options=request_options
        )
        return _response.data

    async def getcontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_id: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition:
        """
        Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        name : typing.Optional[str]
            Optional. Filter by Name. Supports beginning and ending wildcard (*).

        type_id : typing.Optional[int]
            Optional. Filter by TypeID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentdefinitions.getcontentdefinitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentdefinitions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            include_attributes=include_attributes,
            name=name,
            type_id=type_id,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    async def postcontentdefinition(
        self,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.
                    The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the JobID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

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
            await client.contentdefinitions.postcontentdefinition(
                description="Description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentdefinition(
            description=description,
            attributes=attributes,
            content_definition_id=content_definition_id,
            name=name,
            package_type_id=package_type_id,
            type_id=type_id,
            request_options=request_options,
        )
        return _response.data

    async def getcontentdefinition(
        self,
        content_definition_id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSubmissionSharedBusinessEntitiesContentDefinition:
        """
        Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to get.

        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentdefinitions.getcontentdefinition(
                content_definition_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentdefinition(
            content_definition_id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    async def putcontentdefinition(
        self,
        content_definition_id_: int,
        *,
        description: str,
        attributes: typing.Optional[
            typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]
        ] = OMIT,
        content_definition_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        type_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition to update

        description : str
            The description used on the package type in the AGCO Update System

        attributes : typing.Optional[typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]]
            Attributes of this ContentDefinition

        content_definition_id : typing.Optional[int]
            The ID of this content definition.

        name : typing.Optional[str]
            The name of this content. Name must be valid for Attribute on PackageType.

        package_type_id : typing.Optional[str]
            Read Only. The ID of the package type used for this content.

        type_id : typing.Optional[int]
            The type of content.

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
            await client.contentdefinitions.putcontentdefinition(
                content_definition_id_=1,
                description="Description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentdefinition(
            content_definition_id_,
            description=description,
            attributes=attributes,
            content_definition_id=content_definition_id,
            name=name,
            package_type_id=package_type_id,
            type_id=type_id,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentdefinition(
        self, content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition to delete

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
            await client.contentdefinitions.deletecontentdefinition(
                content_definition_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentdefinition(
            content_definition_id, request_options=request_options
        )
        return _response.data

    async def getcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int
            The ID of the ContentDefinition.

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
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentdefinitions.getcontentdefinitionattributes(
                content_definition_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentdefinitionattributes(
            content_definition_id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    async def postcontentdefinitionattribute(
        self,
        content_definition_id_: int,
        *,
        name: str,
        content_definition_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id_ : int
            The ID of the ContentDefinition

        name : str
            The name of this Attribute.

        content_definition_id : typing.Optional[int]
            The ID of the content definition to which this attribute belongs.

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
            await client.contentdefinitions.postcontentdefinitionattribute(
                content_definition_id_=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentdefinitionattribute(
            content_definition_id_,
            name=name,
            content_definition_id=content_definition_id,
            id=id,
            value=value,
            request_options=request_options,
        )
        return _response.data

    async def postcontentdefinitionattributes(
        self,
        content_definition_id: int,
        *,
        request: typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        content_definition_id : int

        request : typing.Sequence[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]

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
            ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentdefinitions.postcontentdefinitionattributes(
                content_definition_id=1,
                request=[
                    ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentdefinitionattributes(
            content_definition_id, request=request, request_options=request_options
        )
        return _response.data
