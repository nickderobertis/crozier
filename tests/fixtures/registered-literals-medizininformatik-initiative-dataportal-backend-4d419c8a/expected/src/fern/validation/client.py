

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ccdl import Ccdl
from ..types.criterion_list import CriterionList
from ..types.crtdl import Crtdl
from ..types.data_extraction_query import DataExtractionQuery
from .raw_client import AsyncRawValidationClient, RawValidationClient


OMIT = typing.cast(typing.Any, ...)


class ValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationClient
        """
        return self._raw_client

    def validate_crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validation.validate_crtdl()
        """
        _response = self._raw_client.validate_crtdl(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data

    def validate_ccdl(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Criterion, FernApi, TermCode

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validation.validate_ccdl(
            version="http://to_be_decided.com/draft-1/schema#",
            inclusion_criteria=[
                [
                    Criterion(
                        term_codes=[
                            TermCode(
                                code="code",
                                system="http://snomed.info/sct",
                                display="Amniotic fluid specimen (specimen)",
                            )
                        ],
                    )
                ]
            ],
        )
        """
        _response = self._raw_client.validate_ccdl(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data

    def validate_dataquery(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Crtdl, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validation.validate_dataquery(
            content=Crtdl(),
        )
        """
        _response = self._raw_client.validate_dataquery(
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data


class AsyncValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationClient
        """
        return self._raw_client

    async def validate_crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validation.validate_crtdl()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_crtdl(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data

    async def validate_ccdl(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Criterion, TermCode

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validation.validate_ccdl(
                version="http://to_be_decided.com/draft-1/schema#",
                inclusion_criteria=[
                    [
                        Criterion(
                            term_codes=[
                                TermCode(
                                    code="code",
                                    system="http://snomed.info/sct",
                                    display="Amniotic fluid specimen (specimen)",
                                )
                            ],
                        )
                    ]
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_ccdl(
            version=version,
            inclusion_criteria=inclusion_criteria,
            display=display,
            exclusion_criteria=exclusion_criteria,
            request_options=request_options,
        )
        return _response.data

    async def validate_dataquery(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Crtdl

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validation.validate_dataquery(
                content=Crtdl(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_dataquery(
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data
