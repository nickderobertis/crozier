

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fine_tuning_job import FineTuningJob
from ..types.list_fine_tuning_job_checkpoints_response import ListFineTuningJobCheckpointsResponse
from ..types.list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse
from ..types.list_paginated_fine_tuning_jobs_response import ListPaginatedFineTuningJobsResponse
from .raw_client import AsyncRawFineTuningClient, RawFineTuningClient
from .types.create_fine_tuning_job_request_hyperparameters import CreateFineTuningJobRequestHyperparameters
from .types.create_fine_tuning_job_request_integrations_item import CreateFineTuningJobRequestIntegrationsItem
from .types.create_fine_tuning_job_request_model import CreateFineTuningJobRequestModel


OMIT = typing.cast(typing.Any, ...)


class FineTuningClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFineTuningClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFineTuningClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFineTuningClient
        """
        return self._raw_client

    def list_paginated_fine_tuning_jobs(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPaginatedFineTuningJobsResponse:
        """
        Parameters
        ----------
        after : typing.Optional[str]
            Identifier for the last job from the previous pagination request.

        limit : typing.Optional[int]
            Number of fine-tuning jobs to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaginatedFineTuningJobsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.list_paginated_fine_tuning_jobs()
        """
        _response = self._raw_client.list_paginated_fine_tuning_jobs(
            after=after, limit=limit, request_options=request_options
        )
        return _response.data

    def create_fine_tuning_job(
        self,
        *,
        model: CreateFineTuningJobRequestModel,
        training_file: str,
        hyperparameters: typing.Optional[CreateFineTuningJobRequestHyperparameters] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        validation_file: typing.Optional[str] = OMIT,
        integrations: typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        model : CreateFineTuningJobRequestModel
            The name of the model to fine-tune. You can select one of the
            [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

        training_file : str
            The ID of an uploaded file that contains training data.

            See [upload file](/docs/api-reference/files/upload) for how to upload a file.

            Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        hyperparameters : typing.Optional[CreateFineTuningJobRequestHyperparameters]
            The hyperparameters used for the fine-tuning job.

        suffix : typing.Optional[str]
            A string of up to 18 characters that will be added to your fine-tuned model name.

            For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

        validation_file : typing.Optional[str]
            The ID of an uploaded file that contains validation data.

            If you provide this file, the data is used to generate validation
            metrics periodically during fine-tuning. These metrics can be viewed in
            the fine-tuning results file.
            The same data should not be present in both train and validation files.

            Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        integrations : typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]]
            A list of integrations to enable for your fine-tuning job.

        seed : typing.Optional[int]
            The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
            If a seed is not specified, one will be generated for you.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.create_fine_tuning_job(
            model="babbage-002",
            training_file="file-abc123",
        )
        """
        _response = self._raw_client.create_fine_tuning_job(
            model=model,
            training_file=training_file,
            hyperparameters=hyperparameters,
            suffix=suffix,
            validation_file=validation_file,
            integrations=integrations,
            seed=seed,
            request_options=request_options,
        )
        return _response.data

    def retrieve_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.retrieve_fine_tuning_job(
            fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        """
        _response = self._raw_client.retrieve_fine_tuning_job(fine_tuning_job_id, request_options=request_options)
        return _response.data

    def list_fine_tuning_events(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFineTuningJobEventsResponse:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get events for.

        after : typing.Optional[str]
            Identifier for the last event from the previous pagination request.

        limit : typing.Optional[int]
            Number of events to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFineTuningJobEventsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.list_fine_tuning_events(
            fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        """
        _response = self._raw_client.list_fine_tuning_events(
            fine_tuning_job_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    def cancel_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.cancel_fine_tuning_job(
            fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        """
        _response = self._raw_client.cancel_fine_tuning_job(fine_tuning_job_id, request_options=request_options)
        return _response.data

    def list_fine_tuning_job_checkpoints(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFineTuningJobCheckpointsResponse:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get checkpoints for.

        after : typing.Optional[str]
            Identifier for the last checkpoint ID from the previous pagination request.

        limit : typing.Optional[int]
            Number of checkpoints to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFineTuningJobCheckpointsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.fine_tuning.list_fine_tuning_job_checkpoints(
            fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        """
        _response = self._raw_client.list_fine_tuning_job_checkpoints(
            fine_tuning_job_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncFineTuningClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFineTuningClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFineTuningClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFineTuningClient
        """
        return self._raw_client

    async def list_paginated_fine_tuning_jobs(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPaginatedFineTuningJobsResponse:
        """
        Parameters
        ----------
        after : typing.Optional[str]
            Identifier for the last job from the previous pagination request.

        limit : typing.Optional[int]
            Number of fine-tuning jobs to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaginatedFineTuningJobsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.list_paginated_fine_tuning_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_paginated_fine_tuning_jobs(
            after=after, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_fine_tuning_job(
        self,
        *,
        model: CreateFineTuningJobRequestModel,
        training_file: str,
        hyperparameters: typing.Optional[CreateFineTuningJobRequestHyperparameters] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        validation_file: typing.Optional[str] = OMIT,
        integrations: typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        model : CreateFineTuningJobRequestModel
            The name of the model to fine-tune. You can select one of the
            [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

        training_file : str
            The ID of an uploaded file that contains training data.

            See [upload file](/docs/api-reference/files/upload) for how to upload a file.

            Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        hyperparameters : typing.Optional[CreateFineTuningJobRequestHyperparameters]
            The hyperparameters used for the fine-tuning job.

        suffix : typing.Optional[str]
            A string of up to 18 characters that will be added to your fine-tuned model name.

            For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

        validation_file : typing.Optional[str]
            The ID of an uploaded file that contains validation data.

            If you provide this file, the data is used to generate validation
            metrics periodically during fine-tuning. These metrics can be viewed in
            the fine-tuning results file.
            The same data should not be present in both train and validation files.

            Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        integrations : typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]]
            A list of integrations to enable for your fine-tuning job.

        seed : typing.Optional[int]
            The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
            If a seed is not specified, one will be generated for you.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.create_fine_tuning_job(
                model="babbage-002",
                training_file="file-abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_fine_tuning_job(
            model=model,
            training_file=training_file,
            hyperparameters=hyperparameters,
            suffix=suffix,
            validation_file=validation_file,
            integrations=integrations,
            seed=seed,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.retrieve_fine_tuning_job(
                fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_fine_tuning_job(fine_tuning_job_id, request_options=request_options)
        return _response.data

    async def list_fine_tuning_events(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFineTuningJobEventsResponse:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get events for.

        after : typing.Optional[str]
            Identifier for the last event from the previous pagination request.

        limit : typing.Optional[int]
            Number of events to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFineTuningJobEventsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.list_fine_tuning_events(
                fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_fine_tuning_events(
            fine_tuning_job_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    async def cancel_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuningJob:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuningJob
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.cancel_fine_tuning_job(
                fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_fine_tuning_job(fine_tuning_job_id, request_options=request_options)
        return _response.data

    async def list_fine_tuning_job_checkpoints(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListFineTuningJobCheckpointsResponse:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get checkpoints for.

        after : typing.Optional[str]
            Identifier for the last checkpoint ID from the previous pagination request.

        limit : typing.Optional[int]
            Number of checkpoints to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFineTuningJobCheckpointsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fine_tuning.list_fine_tuning_job_checkpoints(
                fine_tuning_job_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_fine_tuning_job_checkpoints(
            fine_tuning_job_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data
