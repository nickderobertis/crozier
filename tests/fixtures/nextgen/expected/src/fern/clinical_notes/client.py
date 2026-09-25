

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok12 import Ok12
from ..types.ok15 import Ok15
from ..types.ok16 import Ok16
from .raw_client import AsyncRawClinicalNotesClient, RawClinicalNotesClient


OMIT = typing.cast(typing.Any, ...)


class ClinicalNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClinicalNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClinicalNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClinicalNotesClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_clinical_notes(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of clinical notes after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_clinical_notes(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_clinical_notes(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
        self,
        person_id: str,
        encounter_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of clinical notes for a given encounter.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        encounter_id : str

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
            person_id="personId",
            encounter_id="encounterId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
            person_id,
            encounter_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_documents(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of documents for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_documents(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_documents(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_documents_document_id(
        self, person_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok15:
        """
        Gets the document details for the given person id and document id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose document is being retrieved

        document_id : str
            (Required) (Required) The id of the document being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok15
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_documents_document_id(
            person_id="personId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_documents_document_id(
            person_id, document_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_documents_document_id_pdf(
        self, person_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok16:
        """
        Gets the full document in pdf format for the given person id and document id.

        Response will include PDF encoded binary content:

        %PDF
        ...
        %EOF)

        200 response details show JSON component of response.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose document is being retrieved.

        document_id : str
            (Required) (Required) The id of the document being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok16
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_documents_document_id_pdf(
            person_id="personId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_documents_document_id_pdf(
            person_id, document_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_documents(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a document for the specified person and encounter.

        This POST route does not use a simple JSON request body - this route requires a multipart/form-data request structure (and a Content-Type header of multipart/form-data that also includes a boundary definition).
        Comments (which each begin with //DELETE ME) have been inserted into the POST body in this documentation. Removing each of these comment lines will result in a valid request body schema.

        When comments are removed and values are entered for each variable request element, this will result in a request body with the structure shown in the example below:

        Example Request Header:

        "Content-Type": "multipart/form data; boundary=threequarksformustermark"

        Example Multipart Request Body:

        --thr33quarks4mustermark
        Content-Disposition: form-data; name="request"
        Content-Type: application/json
        {
        "documentType": "EHRImage",
        "fileDescription": "Text Description of Document to Appear in UI"
        }

        --thr33quarks4mustermark
        Content-Disposition: form-data; name="file"; filename="this-will-be-the-filename.PDF"
        Content-Type: application/pdf

        %PDF-1.7
        %µµµµ
          //truncated for brevity;
        %%EOF

        --thr33quarks4mustermark--

        Parameters
        ----------
        person_id : str
            (Required) (Required) The person identifier.

        encounter_id : str
            (Required) (Required) The encounter id to associate this document with.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_documents(
            person_id="personId",
            encounter_id="encounterId",
            request="<string>",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_documents(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncClinicalNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClinicalNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClinicalNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClinicalNotesClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_clinical_notes(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of clinical notes after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_clinical_notes(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_clinical_notes(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
        self,
        person_id: str,
        encounter_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of clinical notes for a given encounter.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        encounter_id : str

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
                person_id="personId",
                encounter_id="encounterId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
            person_id,
            encounter_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_documents(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok12:
        """
        Gets a list of documents for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose documents are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok12
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_documents(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_documents(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_documents_document_id(
        self, person_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok15:
        """
        Gets the document details for the given person id and document id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose document is being retrieved

        document_id : str
            (Required) (Required) The id of the document being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok15
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_documents_document_id(
                person_id="personId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_documents_document_id(
            person_id, document_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_documents_document_id_pdf(
        self, person_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok16:
        """
        Gets the full document in pdf format for the given person id and document id.

        Response will include PDF encoded binary content:

        %PDF
        ...
        %EOF)

        200 response details show JSON component of response.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose document is being retrieved.

        document_id : str
            (Required) (Required) The id of the document being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok16
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_documents_document_id_pdf(
                person_id="personId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_documents_document_id_pdf(
            person_id, document_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_documents(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a document for the specified person and encounter.

        This POST route does not use a simple JSON request body - this route requires a multipart/form-data request structure (and a Content-Type header of multipart/form-data that also includes a boundary definition).
        Comments (which each begin with //DELETE ME) have been inserted into the POST body in this documentation. Removing each of these comment lines will result in a valid request body schema.

        When comments are removed and values are entered for each variable request element, this will result in a request body with the structure shown in the example below:

        Example Request Header:

        "Content-Type": "multipart/form data; boundary=threequarksformustermark"

        Example Multipart Request Body:

        --thr33quarks4mustermark
        Content-Disposition: form-data; name="request"
        Content-Type: application/json
        {
        "documentType": "EHRImage",
        "fileDescription": "Text Description of Document to Appear in UI"
        }

        --thr33quarks4mustermark
        Content-Disposition: form-data; name="file"; filename="this-will-be-the-filename.PDF"
        Content-Type: application/pdf

        %PDF-1.7
        %µµµµ
          //truncated for brevity;
        %%EOF

        --thr33quarks4mustermark--

        Parameters
        ----------
        person_id : str
            (Required) (Required) The person identifier.

        encounter_id : str
            (Required) (Required) The encounter id to associate this document with.

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_documents(
                person_id="personId",
                encounter_id="encounterId",
                request="<string>",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_documents(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data
