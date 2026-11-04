

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.response_item_thesaurus_concept import ResponseItemThesaurusConcept
from ..types.response_item_thesaurus_concept_scheme import ResponseItemThesaurusConceptScheme
from ..types.response_page_thesaurus_concept import ResponsePageThesaurusConcept
from .raw_client import AsyncRawThesaurusClient, RawThesaurusClient
from .types.get_api2thesaurus_level_int_request_form import GetApi2ThesaurusLevelIntRequestForm
from .types.get_api2thesaurus_level_int_request_level import GetApi2ThesaurusLevelIntRequestLevel


class ThesaurusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThesaurusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThesaurusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThesaurusClient
        """
        return self._raw_client

    def retrieve_skos_concept_scheme_for_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemThesaurusConceptScheme:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemThesaurusConceptScheme
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.thesaurus.retrieve_skos_concept_scheme_for_rdamsc_thesaurus()
        """
        _response = self._raw_client.retrieve_skos_concept_scheme_for_rdamsc_thesaurus(request_options=request_options)
        return _response.data

    def retrieve_skos_concept_from_rdamsc_thesaurus(
        self,
        level: GetApi2ThesaurusLevelIntRequestLevel,
        int_: int,
        *,
        form: typing.Optional[GetApi2ThesaurusLevelIntRequestForm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemThesaurusConcept:
        """
        Parameters
        ----------
        level : GetApi2ThesaurusLevelIntRequestLevel
            String portion of the concept ID.

        int_ : int
            Numeric portion of the concept ID.

        form : typing.Optional[GetApi2ThesaurusLevelIntRequestForm]
            Level of detail to include in the entry.
            - `concept` (default) provides the relationships for just this concept.
            - `tree` recursively provides the IDs for narrower concepts of narrower concepts, and broader concepts of broader concepts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemThesaurusConcept
            Success

        Examples
        --------
        from fern.thesaurus import GetApi2ThesaurusLevelIntRequestLevel

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.thesaurus.retrieve_skos_concept_from_rdamsc_thesaurus(
            level=GetApi2ThesaurusLevelIntRequestLevel.DOMAIN,
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_skos_concept_from_rdamsc_thesaurus(
            level, int_, form=form, request_options=request_options
        )
        return _response.data

    def retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageThesaurusConcept:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageThesaurusConcept
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.thesaurus.retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus()
        """
        _response = self._raw_client.retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
            request_options=request_options
        )
        return _response.data

    def retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageThesaurusConcept:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageThesaurusConcept
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.thesaurus.retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog()
        """
        _response = self._raw_client.retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
            request_options=request_options
        )
        return _response.data


class AsyncThesaurusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThesaurusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThesaurusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThesaurusClient
        """
        return self._raw_client

    async def retrieve_skos_concept_scheme_for_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemThesaurusConceptScheme:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemThesaurusConceptScheme
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
            await client.thesaurus.retrieve_skos_concept_scheme_for_rdamsc_thesaurus()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_skos_concept_scheme_for_rdamsc_thesaurus(
            request_options=request_options
        )
        return _response.data

    async def retrieve_skos_concept_from_rdamsc_thesaurus(
        self,
        level: GetApi2ThesaurusLevelIntRequestLevel,
        int_: int,
        *,
        form: typing.Optional[GetApi2ThesaurusLevelIntRequestForm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemThesaurusConcept:
        """
        Parameters
        ----------
        level : GetApi2ThesaurusLevelIntRequestLevel
            String portion of the concept ID.

        int_ : int
            Numeric portion of the concept ID.

        form : typing.Optional[GetApi2ThesaurusLevelIntRequestForm]
            Level of detail to include in the entry.
            - `concept` (default) provides the relationships for just this concept.
            - `tree` recursively provides the IDs for narrower concepts of narrower concepts, and broader concepts of broader concepts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemThesaurusConcept
            Success

        Examples
        --------
        import asyncio

        from fern.thesaurus import GetApi2ThesaurusLevelIntRequestLevel

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.thesaurus.retrieve_skos_concept_from_rdamsc_thesaurus(
                level=GetApi2ThesaurusLevelIntRequestLevel.DOMAIN,
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_skos_concept_from_rdamsc_thesaurus(
            level, int_, form=form, request_options=request_options
        )
        return _response.data

    async def retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageThesaurusConcept:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageThesaurusConcept
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
            await client.thesaurus.retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_array_of_all_concepts_in_the_rdamsc_thesaurus(
            request_options=request_options
        )
        return _response.data

    async def retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageThesaurusConcept:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageThesaurusConcept
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
            await client.thesaurus.retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_array_of_concepts_in_the_rdamsc_thesaurus_that_are_currently_in_use_in_the_catalog(
            request_options=request_options
        )
        return _response.data
