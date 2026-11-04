

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_list import EventList
from ..types.fine_tune import FineTune
from ..types.fine_tune_list import FineTuneList
from .raw_client import AsyncRawFineTunesClient, RawFineTunesClient


OMIT = typing.cast(typing.Any, ...)


class FineTunesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFineTunesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFineTunesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFineTunesClient
        """
        return self._raw_client

    def fine_tunes_list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuneList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuneList
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_list(
            api_version="api-version",
        )
        """
        _response = self._raw_client.fine_tunes_list(api_version=api_version, request_options=request_options)
        return _response.data

    def fine_tunes_create(
        self,
        *,
        api_version: str,
        model: str,
        training_file: str,
        validation_file: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        n_epochs: typing.Optional[int] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        learning_rate_multiplier: typing.Optional[float] = OMIT,
        prompt_loss_weight: typing.Optional[float] = OMIT,
        compute_classification_metrics: typing.Optional[bool] = OMIT,
        classification_n_classes: typing.Optional[int] = OMIT,
        classification_positive_class: typing.Optional[str] = OMIT,
        classification_betas: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FineTune:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        model : str
            The identifier (model-id) of the base model used for this fine-tune.

        training_file : str
            The file identity (file-id) that is used for training this fine tuned model.

        validation_file : typing.Optional[str]
            The file identity (file-id) that is used to evaluate the fine tuned model during training.

        suffix : typing.Optional[str]
            The suffix used to identify the fine-tuned model. The suffix can contain up to 40 characters (a-z, A-Z, 0-9,- and _) that will be added to your fine-tuned model name.

        n_epochs : typing.Optional[int]
            The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

        batch_size : typing.Optional[int]
            The batch size to use for training. The batch size is the number of training examples used to train a single forward and backward pass.
            In general, we've found that larger batch sizes tend to work better for larger datasets.
            The default value as well as the maximum value for this property are specific to a base model.

        learning_rate_multiplier : typing.Optional[float]
            The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value.
            Larger learning rates tend to perform better with larger batch sizes.
            We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results.

        prompt_loss_weight : typing.Optional[float]
            The weight to use for loss on the prompt tokens. This controls how much the model tries to learn to generate the prompt
            (as compared to the completion which always has a weight of 1.0), and can add a stabilizing effect to training when completions are short.
            If prompts are extremely long (relative to completions), it may make sense to reduce this weight so as to avoid over-prioritizing learning the prompt.

        compute_classification_metrics : typing.Optional[bool]
            A value indicating whether to compute classification metrics.
            If set, we calculate classification-specific metrics such as accuracy and F-1 score using the validation set at the end of every epoch.
            These metrics can be viewed in the results file. In order to compute classification metrics, you must provide a validation_file.Additionally,
            you must specify classification_n_classes for multiclass classification or classification_positive_class for binary classification.

        classification_n_classes : typing.Optional[int]
            The number of classes in a classification task.
            This parameter is required for multiclass classification.

        classification_positive_class : typing.Optional[str]
            The positive class in binary classification.
            This parameter is needed to generate precision, recall, and F1 metrics when doing binary classification.

        classification_betas : typing.Optional[typing.Sequence[float]]
            The classification beta values. If this is provided, we calculate F-beta scores at the specified beta values.
            The F-beta score is a generalization of F-1 score. This is only used for binary classification.
            With a beta of 1 (i.e.the F-1 score), precision and recall are given the same weight.
            A larger beta score puts more weight on recall and less on precision. A smaller beta score puts more weight on precision and less on recall.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            The fine tune has been successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_create(
            api_version="api-version",
            model="model",
            training_file="training_file",
        )
        """
        _response = self._raw_client.fine_tunes_create(
            api_version=api_version,
            model=model,
            training_file=training_file,
            validation_file=validation_file,
            suffix=suffix,
            n_epochs=n_epochs,
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
            prompt_loss_weight=prompt_loss_weight,
            compute_classification_metrics=compute_classification_metrics,
            classification_n_classes=classification_n_classes,
            classification_positive_class=classification_positive_class,
            classification_betas=classification_betas,
            request_options=request_options,
        )
        return _response.data

    def fine_tunes_get(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTune:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_get(
            fine_tune_id="fine-tune-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.fine_tunes_get(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data

    def fine_tunes_delete(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_delete(
            fine_tune_id="fine-tune-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.fine_tunes_delete(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data

    def fine_tunes_get_events(
        self,
        fine_tune_id: str,
        *,
        api_version: str,
        stream: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventList:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        stream : typing.Optional[bool]
            A flag indicating whether to stream events for the fine-tune job. If set to true,
            events will be sent as data-only server-sent events as they become available. The stream will terminate with
               a data: [DONE] message when the job is finished (succeeded, cancelled, or failed).
            If set to false, only events generated so far will be returned..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventList
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_get_events(
            fine_tune_id="fine-tune-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.fine_tunes_get_events(
            fine_tune_id, api_version=api_version, stream=stream, request_options=request_options
        )
        return _response.data

    def fine_tunes_cancel(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTune:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            The fine tune has been successfully canceled

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fine_tunes.fine_tunes_cancel(
            fine_tune_id="fine-tune-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.fine_tunes_cancel(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data


class AsyncFineTunesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFineTunesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFineTunesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFineTunesClient
        """
        return self._raw_client

    async def fine_tunes_list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTuneList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTuneList
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_list(
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_list(api_version=api_version, request_options=request_options)
        return _response.data

    async def fine_tunes_create(
        self,
        *,
        api_version: str,
        model: str,
        training_file: str,
        validation_file: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        n_epochs: typing.Optional[int] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        learning_rate_multiplier: typing.Optional[float] = OMIT,
        prompt_loss_weight: typing.Optional[float] = OMIT,
        compute_classification_metrics: typing.Optional[bool] = OMIT,
        classification_n_classes: typing.Optional[int] = OMIT,
        classification_positive_class: typing.Optional[str] = OMIT,
        classification_betas: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FineTune:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        model : str
            The identifier (model-id) of the base model used for this fine-tune.

        training_file : str
            The file identity (file-id) that is used for training this fine tuned model.

        validation_file : typing.Optional[str]
            The file identity (file-id) that is used to evaluate the fine tuned model during training.

        suffix : typing.Optional[str]
            The suffix used to identify the fine-tuned model. The suffix can contain up to 40 characters (a-z, A-Z, 0-9,- and _) that will be added to your fine-tuned model name.

        n_epochs : typing.Optional[int]
            The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

        batch_size : typing.Optional[int]
            The batch size to use for training. The batch size is the number of training examples used to train a single forward and backward pass.
            In general, we've found that larger batch sizes tend to work better for larger datasets.
            The default value as well as the maximum value for this property are specific to a base model.

        learning_rate_multiplier : typing.Optional[float]
            The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value.
            Larger learning rates tend to perform better with larger batch sizes.
            We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results.

        prompt_loss_weight : typing.Optional[float]
            The weight to use for loss on the prompt tokens. This controls how much the model tries to learn to generate the prompt
            (as compared to the completion which always has a weight of 1.0), and can add a stabilizing effect to training when completions are short.
            If prompts are extremely long (relative to completions), it may make sense to reduce this weight so as to avoid over-prioritizing learning the prompt.

        compute_classification_metrics : typing.Optional[bool]
            A value indicating whether to compute classification metrics.
            If set, we calculate classification-specific metrics such as accuracy and F-1 score using the validation set at the end of every epoch.
            These metrics can be viewed in the results file. In order to compute classification metrics, you must provide a validation_file.Additionally,
            you must specify classification_n_classes for multiclass classification or classification_positive_class for binary classification.

        classification_n_classes : typing.Optional[int]
            The number of classes in a classification task.
            This parameter is required for multiclass classification.

        classification_positive_class : typing.Optional[str]
            The positive class in binary classification.
            This parameter is needed to generate precision, recall, and F1 metrics when doing binary classification.

        classification_betas : typing.Optional[typing.Sequence[float]]
            The classification beta values. If this is provided, we calculate F-beta scores at the specified beta values.
            The F-beta score is a generalization of F-1 score. This is only used for binary classification.
            With a beta of 1 (i.e.the F-1 score), precision and recall are given the same weight.
            A larger beta score puts more weight on recall and less on precision. A smaller beta score puts more weight on precision and less on recall.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            The fine tune has been successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_create(
                api_version="api-version",
                model="model",
                training_file="training_file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_create(
            api_version=api_version,
            model=model,
            training_file=training_file,
            validation_file=validation_file,
            suffix=suffix,
            n_epochs=n_epochs,
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
            prompt_loss_weight=prompt_loss_weight,
            compute_classification_metrics=compute_classification_metrics,
            classification_n_classes=classification_n_classes,
            classification_positive_class=classification_positive_class,
            classification_betas=classification_betas,
            request_options=request_options,
        )
        return _response.data

    async def fine_tunes_get(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTune:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_get(
                fine_tune_id="fine-tune-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_get(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data

    async def fine_tunes_delete(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_delete(
                fine_tune_id="fine-tune-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_delete(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data

    async def fine_tunes_get_events(
        self,
        fine_tune_id: str,
        *,
        api_version: str,
        stream: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventList:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        stream : typing.Optional[bool]
            A flag indicating whether to stream events for the fine-tune job. If set to true,
            events will be sent as data-only server-sent events as they become available. The stream will terminate with
               a data: [DONE] message when the job is finished (succeeded, cancelled, or failed).
            If set to false, only events generated so far will be returned..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventList
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_get_events(
                fine_tune_id="fine-tune-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_get_events(
            fine_tune_id, api_version=api_version, stream=stream, request_options=request_options
        )
        return _response.data

    async def fine_tunes_cancel(
        self, fine_tune_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FineTune:
        """
        Parameters
        ----------
        fine_tune_id : str
            The identifier of the fine-tune job.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FineTune
            The fine tune has been successfully canceled

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fine_tunes.fine_tunes_cancel(
                fine_tune_id="fine-tune-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fine_tunes_cancel(
            fine_tune_id, api_version=api_version, request_options=request_options
        )
        return _response.data
