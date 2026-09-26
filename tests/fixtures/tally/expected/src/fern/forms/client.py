

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block import Block
from ..types.question import Question
from .raw_client import AsyncRawFormsClient, RawFormsClient
from .types.get_form_submission_response import GetFormSubmissionResponse
from .types.list_form_blocks_response import ListFormBlocksResponse
from .types.list_form_questions_response import ListFormQuestionsResponse
from .types.list_form_submissions_request_filter import ListFormSubmissionsRequestFilter
from .types.list_form_submissions_response import ListFormSubmissionsResponse


OMIT = typing.cast(typing.Any, ...)


class FormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormsClient
        """
        return self._raw_client

    def list_form_questions(
        self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFormQuestionsResponse:
        """
        Returns a list of all questions in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormQuestionsResponse
            List of questions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.list_form_questions(
            form_id="formId",
        )
        """
        _response = self._raw_client.list_form_questions(form_id, request_options=request_options)
        return _response.data

    def update_form_question(
        self,
        form_id: str,
        question_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Question:
        """
        Updates a specific question in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        question_id : str
            The ID of the question

        title : typing.Optional[str]
            The new title for the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Question
            Question updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.update_form_question(
            form_id="formId",
            question_id="questionId",
        )
        """
        _response = self._raw_client.update_form_question(
            form_id, question_id, title=title, request_options=request_options
        )
        return _response.data

    def list_form_blocks(
        self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFormBlocksResponse:
        """
        Returns a list of all blocks in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormBlocksResponse
            List of blocks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.list_form_blocks(
            form_id="formId",
        )
        """
        _response = self._raw_client.list_form_blocks(form_id, request_options=request_options)
        return _response.data

    def update_form_blocks(
        self,
        form_id: str,
        *,
        blocks: typing.Optional[typing.Sequence[Block]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Updates blocks in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        blocks : typing.Optional[typing.Sequence[Block]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Blocks updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.update_form_blocks(
            form_id="formId",
        )
        """
        _response = self._raw_client.update_form_blocks(form_id, blocks=blocks, request_options=request_options)
        return _response.data

    def list_form_submissions(
        self,
        form_id: str,
        *,
        page: typing.Optional[float] = None,
        filter: typing.Optional[ListFormSubmissionsRequestFilter] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        after_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormSubmissionsResponse:
        """
        Returns a paginated list of form submissions with their responses.

        Parameters
        ----------
        form_id : str
            The ID of the form

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        filter : typing.Optional[ListFormSubmissionsRequestFilter]
            Filter submissions by status

        start_date : typing.Optional[dt.datetime]
            Filter submissions submitted on or after this date (ISO 8601 format)

        end_date : typing.Optional[dt.datetime]
            Filter submissions submitted on or before this date (ISO 8601 format)

        after_id : typing.Optional[str]
            Get submissions that came after a specific submission ID

        limit : typing.Optional[float]
            Number of submissions to return per page (default: 50, max: 500)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormSubmissionsResponse
            List of form submissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.list_form_submissions(
            form_id="formId",
        )
        """
        _response = self._raw_client.list_form_submissions(
            form_id,
            page=page,
            filter=filter,
            start_date=start_date,
            end_date=end_date,
            after_id=after_id,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_form_submission(
        self, form_id: str, submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFormSubmissionResponse:
        """
        Returns a specific form submission with all its responses and the form questions.

        Parameters
        ----------
        form_id : str
            The ID of the form

        submission_id : str
            The ID of the submission to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormSubmissionResponse
            Form submission retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.get_form_submission(
            form_id="formId",
            submission_id="submissionId",
        )
        """
        _response = self._raw_client.get_form_submission(form_id, submission_id, request_options=request_options)
        return _response.data

    def delete_form_submission(
        self, form_id: str, submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific submission from a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        submission_id : str
            The ID of the submission to delete

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
        )
        client.forms.delete_form_submission(
            form_id="formId",
            submission_id="submissionId",
        )
        """
        _response = self._raw_client.delete_form_submission(form_id, submission_id, request_options=request_options)
        return _response.data


class AsyncFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormsClient
        """
        return self._raw_client

    async def list_form_questions(
        self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFormQuestionsResponse:
        """
        Returns a list of all questions in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormQuestionsResponse
            List of questions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.list_form_questions(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_questions(form_id, request_options=request_options)
        return _response.data

    async def update_form_question(
        self,
        form_id: str,
        question_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Question:
        """
        Updates a specific question in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        question_id : str
            The ID of the question

        title : typing.Optional[str]
            The new title for the question

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Question
            Question updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.update_form_question(
                form_id="formId",
                question_id="questionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form_question(
            form_id, question_id, title=title, request_options=request_options
        )
        return _response.data

    async def list_form_blocks(
        self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFormBlocksResponse:
        """
        Returns a list of all blocks in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormBlocksResponse
            List of blocks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.list_form_blocks(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_blocks(form_id, request_options=request_options)
        return _response.data

    async def update_form_blocks(
        self,
        form_id: str,
        *,
        blocks: typing.Optional[typing.Sequence[Block]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Updates blocks in a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        blocks : typing.Optional[typing.Sequence[Block]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Blocks updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.update_form_blocks(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form_blocks(form_id, blocks=blocks, request_options=request_options)
        return _response.data

    async def list_form_submissions(
        self,
        form_id: str,
        *,
        page: typing.Optional[float] = None,
        filter: typing.Optional[ListFormSubmissionsRequestFilter] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        after_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormSubmissionsResponse:
        """
        Returns a paginated list of form submissions with their responses.

        Parameters
        ----------
        form_id : str
            The ID of the form

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        filter : typing.Optional[ListFormSubmissionsRequestFilter]
            Filter submissions by status

        start_date : typing.Optional[dt.datetime]
            Filter submissions submitted on or after this date (ISO 8601 format)

        end_date : typing.Optional[dt.datetime]
            Filter submissions submitted on or before this date (ISO 8601 format)

        after_id : typing.Optional[str]
            Get submissions that came after a specific submission ID

        limit : typing.Optional[float]
            Number of submissions to return per page (default: 50, max: 500)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormSubmissionsResponse
            List of form submissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.list_form_submissions(
                form_id="formId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_submissions(
            form_id,
            page=page,
            filter=filter,
            start_date=start_date,
            end_date=end_date,
            after_id=after_id,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_form_submission(
        self, form_id: str, submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFormSubmissionResponse:
        """
        Returns a specific form submission with all its responses and the form questions.

        Parameters
        ----------
        form_id : str
            The ID of the form

        submission_id : str
            The ID of the submission to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormSubmissionResponse
            Form submission retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.get_form_submission(
                form_id="formId",
                submission_id="submissionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_submission(form_id, submission_id, request_options=request_options)
        return _response.data

    async def delete_form_submission(
        self, form_id: str, submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific submission from a form.

        Parameters
        ----------
        form_id : str
            The ID of the form

        submission_id : str
            The ID of the submission to delete

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
        )


        async def main() -> None:
            await client.forms.delete_form_submission(
                form_id="formId",
                submission_id="submissionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_form_submission(
            form_id, submission_id, request_options=request_options
        )
        return _response.data
