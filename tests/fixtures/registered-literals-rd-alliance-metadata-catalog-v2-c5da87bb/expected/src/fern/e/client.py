

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.creator import Creator
from ..types.endorsement_related_entities_item import EndorsementRelatedEntitiesItem
from ..types.endorsement_valid import EndorsementValid
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mscid import Mscid
from ..types.response_item_endorsement import ResponseItemEndorsement
from ..types.response_page_endorsement import ResponsePageEndorsement
from ..types.response_success_endorsement import ResponseSuccessEndorsement
from ..types.slug import Slug
from ..types.uri import Uri
from .raw_client import AsyncRawEClient, RawEClient


OMIT = typing.cast(typing.Any, ...)


class EClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEClient
        """
        return self._raw_client

    def list_all_endorsements(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageEndorsement:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageEndorsement
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.e.list_all_endorsements()
        """
        _response = self._raw_client.list_all_endorsements(q=q, request_options=request_options)
        return _response.data

    def submit_a_new_endorsement_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessEndorsement:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessEndorsement
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.e.submit_a_new_endorsement_record()
        """
        _response = self._raw_client.submit_a_new_endorsement_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            creators=creators,
            publication=publication,
            issued=issued,
            valid=valid,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    def retrieve_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemEndorsement:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemEndorsement
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.e.retrieve_an_existing_endorsement_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_endorsement_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_endorsement_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessEndorsement:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessEndorsement
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.e.modify_an_existing_endorsement_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_endorsement_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            creators=creators,
            publication=publication,
            issued=issued,
            valid=valid,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.e.remove_an_existing_endorsement_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_endorsement_record(int_, request_options=request_options)
        return _response.data


class AsyncEClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEClient
        """
        return self._raw_client

    async def list_all_endorsements(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageEndorsement:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageEndorsement
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.e.list_all_endorsements()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_endorsements(q=q, request_options=request_options)
        return _response.data

    async def submit_a_new_endorsement_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessEndorsement:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessEndorsement
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.e.submit_a_new_endorsement_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_endorsement_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            creators=creators,
            publication=publication,
            issued=issued,
            valid=valid,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemEndorsement:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemEndorsement
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.e.retrieve_an_existing_endorsement_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_endorsement_record(
            int_, request_options=request_options
        )
        return _response.data

    async def modify_an_existing_endorsement_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        publication: typing.Optional[str] = OMIT,
        issued: typing.Optional[str] = OMIT,
        valid: typing.Optional[EndorsementValid] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessEndorsement:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The title of the endorsement document.

        description : typing.Optional[str]
            Description of the endorsement document.
            - Use this to record any caveats to the endorsement.
            - This could indicate if only certain versions of the scheme(s) are endorsed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Authors of the endorsement document

        publication : typing.Optional[str]
            Other bibliographic information (excluding date).

        issued : typing.Optional[str]
            The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.

        valid : typing.Optional[EndorsementValid]
            The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
            If an end date is provided, it expresses the date on which the endorsement was withdrawn.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the endorsement may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the endorsement.

        related_entities : typing.Optional[typing.Sequence[EndorsementRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessEndorsement
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.e.modify_an_existing_endorsement_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_endorsement_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            creators=creators,
            publication=publication,
            issued=issued,
            valid=valid,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_endorsement_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.e.remove_an_existing_endorsement_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_endorsement_record(int_, request_options=request_options)
        return _response.data
