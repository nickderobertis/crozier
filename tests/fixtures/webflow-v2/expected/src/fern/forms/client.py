

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFormsClient, RawFormsClient
from .types.get_forms_response import GetFormsResponse
from .types.get_submission_forms_response import GetSubmissionFormsResponse
from .types.list_forms_response import ListFormsResponse
from .types.list_submissions_forms_response import ListSubmissionsFormsResponse
from .types.update_submission_forms_response import UpdateSubmissionFormsResponse


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

    def list(
        self,
        site_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormsResponse:
        """
        List forms for a given site.

        Required scope | `forms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def get(self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetFormsResponse:
        """
        Get information about a given form.

        Required scope | `forms:read`

        Parameters
        ----------
        form_id : str
            Unique identifier for a Form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.get(
            form_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get(form_id, request_options=request_options)
        return _response.data

    def list_submissions(
        self,
        form_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSubmissionsFormsResponse:
        """
        List form submissions for a given form

        <Note title="Forms in components">
          When a form is used in a component definition, each instance of the form is considered a unique form.

          To get a combined list of submissions for a form that appears across multiple component instances, use the [List Form Submissions by Site](/data/reference/forms/form-submissions/list-submissions-by-site) endpoint.
        </Note>

        Required scope | `forms:read`

        Parameters
        ----------
        form_id : str
            Unique identifier for a Form

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSubmissionsFormsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.list_submissions(
            form_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list_submissions(
            form_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_submission(
        self, form_submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubmissionFormsResponse:
        """
        Get information about a given form submissio.

        Required scope | `forms:read`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubmissionFormsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.get_submission(
            form_submission_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get_submission(form_submission_id, request_options=request_options)
        return _response.data

    def delete_submission(
        self, form_submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a form submission


        Required scope | `forms:write`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

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
        client.forms.delete_submission(
            form_submission_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.delete_submission(form_submission_id, request_options=request_options)
        return _response.data

    def update_submission(
        self,
        form_submission_id: str,
        *,
        form_submission_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubmissionFormsResponse:
        """
        Update hidden fields on a form submission

        Required scope | `forms:write`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

        form_submission_data : typing.Optional[typing.Dict[str, typing.Any]]
            An existing **hidden field** defined on the form schema, and the corresponding value to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSubmissionFormsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forms.update_submission(
            form_submission_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.update_submission(
            form_submission_id, form_submission_data=form_submission_data, request_options=request_options
        )
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

    async def list(
        self,
        site_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFormsResponse:
        """
        List forms for a given site.

        Required scope | `forms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFormsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def get(self, form_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetFormsResponse:
        """
        Get information about a given form.

        Required scope | `forms:read`

        Parameters
        ----------
        form_id : str
            Unique identifier for a Form

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFormsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.get(
                form_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(form_id, request_options=request_options)
        return _response.data

    async def list_submissions(
        self,
        form_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSubmissionsFormsResponse:
        """
        List form submissions for a given form

        <Note title="Forms in components">
          When a form is used in a component definition, each instance of the form is considered a unique form.

          To get a combined list of submissions for a form that appears across multiple component instances, use the [List Form Submissions by Site](/data/reference/forms/form-submissions/list-submissions-by-site) endpoint.
        </Note>

        Required scope | `forms:read`

        Parameters
        ----------
        form_id : str
            Unique identifier for a Form

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSubmissionsFormsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.list_submissions(
                form_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_submissions(
            form_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_submission(
        self, form_submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubmissionFormsResponse:
        """
        Get information about a given form submissio.

        Required scope | `forms:read`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubmissionFormsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.get_submission(
                form_submission_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_submission(form_submission_id, request_options=request_options)
        return _response.data

    async def delete_submission(
        self, form_submission_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a form submission


        Required scope | `forms:write`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

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
            await client.forms.delete_submission(
                form_submission_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_submission(form_submission_id, request_options=request_options)
        return _response.data

    async def update_submission(
        self,
        form_submission_id: str,
        *,
        form_submission_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubmissionFormsResponse:
        """
        Update hidden fields on a form submission

        Required scope | `forms:write`

        Parameters
        ----------
        form_submission_id : str
            Unique identifier for a Form Submission

        form_submission_data : typing.Optional[typing.Dict[str, typing.Any]]
            An existing **hidden field** defined on the form schema, and the corresponding value to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSubmissionFormsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.update_submission(
                form_submission_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_submission(
            form_submission_id, form_submission_data=form_submission_data, request_options=request_options
        )
        return _response.data
