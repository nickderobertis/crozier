

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bounding_box import BoundingBox
from ..types.connected_symbols_item import ConnectedSymbolsItem
from ..types.image_details import ImageDetails
from ..types.inference_result import InferenceResult
from ..types.label import Label
from ..types.symbol_and_text_associated import SymbolAndTextAssociated
from ..types.symbol_detection_inference_response import SymbolDetectionInferenceResponse
from ..types.text_detection_inference_response import TextDetectionInferenceResponse
from ..types.text_recognized import TextRecognized
from .raw_client import AsyncRawPidDigitizationClient, RawPidDigitizationClient
from .types.get_inference_results_api_pid_digitization_inference_result_type_pid_id_get_response import (
    GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
)


OMIT = typing.cast(typing.Any, ...)


class PidDigitizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPidDigitizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPidDigitizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPidDigitizationClient
        """
        return self._raw_client

    def detect_symbols(
        self,
        pid_id: str,
        *,
        file: core.File,
        bounding_box_inclusive_str: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SymbolDetectionInferenceResponse:
        """
        Detects symbols in an image and returns the bounding boxes of the detected symbols.

        param pid: The PID.
        param bounding_box_inclusive_str: The bounding box of the P&ID image without extraneous legend information.
        param file: The image to detect symbols in.
        return: The bounding boxes of the detected symbols.
        rtype: symbol_detection.ObjectDetectionPrediction

        Parameters
        ----------
        pid_id : str

        file : core.File
            See core.File for more documentation

        bounding_box_inclusive_str : typing.Optional[typing.Any]
            The bounding box of the P&ID image without extraneous legend information.This should be provided as a JSON string with the following format: {"topX": 0.0, "topY": 0.0, "bottomX": 1.0, "bottomY": 1.0}.  The coordinates should be normalized to the range [0, 1]. The default value is the entire image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SymbolDetectionInferenceResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.detect_symbols(
            pid_id="pid_id",
        )
        """
        _response = self._raw_client.detect_symbols(
            pid_id, file=file, bounding_box_inclusive_str=bounding_box_inclusive_str, request_options=request_options
        )
        return _response.data

    def detect_text(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        label: typing.Sequence[Label],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TextDetectionInferenceResponse:
        """
        This endpoint takes in the P&ID image id to download the original image and recognize the texts of the image.
        Additionally, it takes in the corrected symbol detected inference results which will be stored and used to
        associate a text with a symbol.

        Returns the text detection inference results, which includes all text detected and
        the text and symbols associated on a P&ID image.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        label : typing.Sequence[Label]

        bounding_box_inclusive : typing.Optional[BoundingBox]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextDetectionInferenceResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, ImageDetails, Label

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.detect_text(
            pid_id="pid_id",
            image_url="image_url",
            image_details=ImageDetails(
                width=1,
                height=1,
            ),
            label=[
                Label(
                    top_x=1.1,
                    top_y=1.1,
                    bottom_x=1.1,
                    bottom_y=1.1,
                    id=1,
                    label="label",
                )
            ],
        )
        """
        _response = self._raw_client.detect_text(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            label=label,
            bounding_box_inclusive=bounding_box_inclusive,
            request_options=request_options,
        )
        return _response.data

    def detect_lines_and_construct_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        all_text_list: typing.Sequence[TextRecognized],
        text_and_symbols_associated_list: typing.Sequence[SymbolAndTextAssociated],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        hough_threshold: typing.Optional[int] = OMIT,
        hough_min_line_length: typing.Optional[int] = OMIT,
        hough_max_line_gap: typing.Optional[int] = OMIT,
        hough_rho: typing.Optional[float] = OMIT,
        hough_theta: typing.Optional[int] = OMIT,
        thinning_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint takes in the P&ID image id and the text response and then will build an asset connected
        graph based on the line segments, text detection results and symbol associations.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        all_text_list : typing.Sequence[TextRecognized]

        text_and_symbols_associated_list : typing.Sequence[SymbolAndTextAssociated]

        bounding_box_inclusive : typing.Optional[BoundingBox]

        hough_threshold : typing.Optional[int]

        hough_min_line_length : typing.Optional[int]

        hough_max_line_gap : typing.Optional[int]

        hough_rho : typing.Optional[float]

        hough_theta : typing.Optional[int]

        thinning_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, ImageDetails, SymbolAndTextAssociated, TextRecognized

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.detect_lines_and_construct_graph(
            pid_id="pid_id",
            image_url="image_url",
            image_details=ImageDetails(
                width=1,
                height=1,
            ),
            all_text_list=[
                TextRecognized(
                    top_x=1.1,
                    top_y=1.1,
                    bottom_x=1.1,
                    bottom_y=1.1,
                    text="text",
                )
            ],
            text_and_symbols_associated_list=[
                SymbolAndTextAssociated(
                    top_x=1.1,
                    top_y=1.1,
                    bottom_x=1.1,
                    bottom_y=1.1,
                    id=1,
                    label="label",
                )
            ],
        )
        """
        _response = self._raw_client.detect_lines_and_construct_graph(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            all_text_list=all_text_list,
            text_and_symbols_associated_list=text_and_symbols_associated_list,
            bounding_box_inclusive=bounding_box_inclusive,
            hough_threshold=hough_threshold,
            hough_min_line_length=hough_min_line_length,
            hough_max_line_gap=hough_max_line_gap,
            hough_rho=hough_rho,
            hough_theta=hough_theta,
            thinning_enabled=thinning_enabled,
            request_options=request_options,
        )
        return _response.data

    def persist_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        connected_symbols: typing.Sequence[ConnectedSymbolsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        For the given P&ID image id, the graph output (if any) from the prior step is persisted in the graph database.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        connected_symbols : typing.Sequence[ConnectedSymbolsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import (
            BoundingBox,
            ConnectedSymbolsConnectionItem,
            ConnectedSymbolsItem,
            FernApi,
            ImageDetails,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.persist_graph(
            pid_id="pid_id",
            image_url="image_url",
            image_details=ImageDetails(
                width=1,
                height=1,
            ),
            connected_symbols=[
                ConnectedSymbolsItem(
                    id=1,
                    label="label",
                    text_associated="text_associated",
                    bounding_box=BoundingBox(
                        top_x=1.1,
                        top_y=1.1,
                        bottom_x=1.1,
                        bottom_y=1.1,
                    ),
                    connections=[
                        ConnectedSymbolsConnectionItem(
                            id=1,
                            label="label",
                            text_associated="text_associated",
                            bounding_box=BoundingBox(
                                top_x=1.1,
                                top_y=1.1,
                                bottom_x=1.1,
                                bottom_y=1.1,
                            ),
                            flow_direction="unknown",
                            segments=[
                                BoundingBox(
                                    top_x=1.1,
                                    top_y=1.1,
                                    bottom_x=1.1,
                                    bottom_y=1.1,
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.persist_graph(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            connected_symbols=connected_symbols,
            request_options=request_options,
        )
        return _response.data

    def get_inference_results(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse:
        """
        Gets the inference results for a given pid id and inference result type.

        param pid: The PID id.
        param inference_result_type: The inference result type.
        return: The inference results.
        rtype: symbol_detection.InferenceResponse

        Parameters
        ----------
        inference_result_type : InferenceResult

        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.get_inference_results(
            inference_result_type="symbol-detection",
            pid_id="pid_id",
        )
        """
        _response = self._raw_client.get_inference_results(
            inference_result_type, pid_id, request_options=request_options
        )
        return _response.data

    def get_job_status(self, pid_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Gets the inference job status for a given pid id .
        param pid: The PID id.
        return: The JobStatus of pid_id.
        rtype: JobStatus

        Parameters
        ----------
        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.get_job_status(
            pid_id="pid_id",
        )
        """
        _response = self._raw_client.get_job_status(pid_id, request_options=request_options)
        return _response.data

    def get_output_inference_images(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Gets the inference output image for a given pid id and inference result type.
        param pid: The PID id.
        param inference_result_type: The inference result type.
        rtype: ImageResponse
        The inference output image has information overlayed on the original image
        that provides user insight into what was done in the inferencing service.

        Parameters
        ----------
        inference_result_type : InferenceResult

        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pid_digitization.get_output_inference_images(
            inference_result_type="symbol-detection",
            pid_id="pid_id",
        )
        """
        _response = self._raw_client.get_output_inference_images(
            inference_result_type, pid_id, request_options=request_options
        )
        return _response.data


class AsyncPidDigitizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPidDigitizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPidDigitizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPidDigitizationClient
        """
        return self._raw_client

    async def detect_symbols(
        self,
        pid_id: str,
        *,
        file: core.File,
        bounding_box_inclusive_str: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SymbolDetectionInferenceResponse:
        """
        Detects symbols in an image and returns the bounding boxes of the detected symbols.

        param pid: The PID.
        param bounding_box_inclusive_str: The bounding box of the P&ID image without extraneous legend information.
        param file: The image to detect symbols in.
        return: The bounding boxes of the detected symbols.
        rtype: symbol_detection.ObjectDetectionPrediction

        Parameters
        ----------
        pid_id : str

        file : core.File
            See core.File for more documentation

        bounding_box_inclusive_str : typing.Optional[typing.Any]
            The bounding box of the P&ID image without extraneous legend information.This should be provided as a JSON string with the following format: {"topX": 0.0, "topY": 0.0, "bottomX": 1.0, "bottomY": 1.0}.  The coordinates should be normalized to the range [0, 1]. The default value is the entire image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SymbolDetectionInferenceResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.detect_symbols(
                pid_id="pid_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detect_symbols(
            pid_id, file=file, bounding_box_inclusive_str=bounding_box_inclusive_str, request_options=request_options
        )
        return _response.data

    async def detect_text(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        label: typing.Sequence[Label],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TextDetectionInferenceResponse:
        """
        This endpoint takes in the P&ID image id to download the original image and recognize the texts of the image.
        Additionally, it takes in the corrected symbol detected inference results which will be stored and used to
        associate a text with a symbol.

        Returns the text detection inference results, which includes all text detected and
        the text and symbols associated on a P&ID image.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        label : typing.Sequence[Label]

        bounding_box_inclusive : typing.Optional[BoundingBox]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextDetectionInferenceResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ImageDetails, Label

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.detect_text(
                pid_id="pid_id",
                image_url="image_url",
                image_details=ImageDetails(
                    width=1,
                    height=1,
                ),
                label=[
                    Label(
                        top_x=1.1,
                        top_y=1.1,
                        bottom_x=1.1,
                        bottom_y=1.1,
                        id=1,
                        label="label",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detect_text(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            label=label,
            bounding_box_inclusive=bounding_box_inclusive,
            request_options=request_options,
        )
        return _response.data

    async def detect_lines_and_construct_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        all_text_list: typing.Sequence[TextRecognized],
        text_and_symbols_associated_list: typing.Sequence[SymbolAndTextAssociated],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        hough_threshold: typing.Optional[int] = OMIT,
        hough_min_line_length: typing.Optional[int] = OMIT,
        hough_max_line_gap: typing.Optional[int] = OMIT,
        hough_rho: typing.Optional[float] = OMIT,
        hough_theta: typing.Optional[int] = OMIT,
        thinning_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint takes in the P&ID image id and the text response and then will build an asset connected
        graph based on the line segments, text detection results and symbol associations.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        all_text_list : typing.Sequence[TextRecognized]

        text_and_symbols_associated_list : typing.Sequence[SymbolAndTextAssociated]

        bounding_box_inclusive : typing.Optional[BoundingBox]

        hough_threshold : typing.Optional[int]

        hough_min_line_length : typing.Optional[int]

        hough_max_line_gap : typing.Optional[int]

        hough_rho : typing.Optional[float]

        hough_theta : typing.Optional[int]

        thinning_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ImageDetails,
            SymbolAndTextAssociated,
            TextRecognized,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.detect_lines_and_construct_graph(
                pid_id="pid_id",
                image_url="image_url",
                image_details=ImageDetails(
                    width=1,
                    height=1,
                ),
                all_text_list=[
                    TextRecognized(
                        top_x=1.1,
                        top_y=1.1,
                        bottom_x=1.1,
                        bottom_y=1.1,
                        text="text",
                    )
                ],
                text_and_symbols_associated_list=[
                    SymbolAndTextAssociated(
                        top_x=1.1,
                        top_y=1.1,
                        bottom_x=1.1,
                        bottom_y=1.1,
                        id=1,
                        label="label",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detect_lines_and_construct_graph(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            all_text_list=all_text_list,
            text_and_symbols_associated_list=text_and_symbols_associated_list,
            bounding_box_inclusive=bounding_box_inclusive,
            hough_threshold=hough_threshold,
            hough_min_line_length=hough_min_line_length,
            hough_max_line_gap=hough_max_line_gap,
            hough_rho=hough_rho,
            hough_theta=hough_theta,
            thinning_enabled=thinning_enabled,
            request_options=request_options,
        )
        return _response.data

    async def persist_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        connected_symbols: typing.Sequence[ConnectedSymbolsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        For the given P&ID image id, the graph output (if any) from the prior step is persisted in the graph database.

        Parameters
        ----------
        pid_id : str
            The P&ID image id

        image_url : str

        image_details : ImageDetails

        connected_symbols : typing.Sequence[ConnectedSymbolsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BoundingBox,
            ConnectedSymbolsConnectionItem,
            ConnectedSymbolsItem,
            ImageDetails,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.persist_graph(
                pid_id="pid_id",
                image_url="image_url",
                image_details=ImageDetails(
                    width=1,
                    height=1,
                ),
                connected_symbols=[
                    ConnectedSymbolsItem(
                        id=1,
                        label="label",
                        text_associated="text_associated",
                        bounding_box=BoundingBox(
                            top_x=1.1,
                            top_y=1.1,
                            bottom_x=1.1,
                            bottom_y=1.1,
                        ),
                        connections=[
                            ConnectedSymbolsConnectionItem(
                                id=1,
                                label="label",
                                text_associated="text_associated",
                                bounding_box=BoundingBox(
                                    top_x=1.1,
                                    top_y=1.1,
                                    bottom_x=1.1,
                                    bottom_y=1.1,
                                ),
                                flow_direction="unknown",
                                segments=[
                                    BoundingBox(
                                        top_x=1.1,
                                        top_y=1.1,
                                        bottom_x=1.1,
                                        bottom_y=1.1,
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.persist_graph(
            pid_id,
            image_url=image_url,
            image_details=image_details,
            connected_symbols=connected_symbols,
            request_options=request_options,
        )
        return _response.data

    async def get_inference_results(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse:
        """
        Gets the inference results for a given pid id and inference result type.

        param pid: The PID id.
        param inference_result_type: The inference result type.
        return: The inference results.
        rtype: symbol_detection.InferenceResponse

        Parameters
        ----------
        inference_result_type : InferenceResult

        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.get_inference_results(
                inference_result_type="symbol-detection",
                pid_id="pid_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inference_results(
            inference_result_type, pid_id, request_options=request_options
        )
        return _response.data

    async def get_job_status(
        self, pid_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Gets the inference job status for a given pid id .
        param pid: The PID id.
        return: The JobStatus of pid_id.
        rtype: JobStatus

        Parameters
        ----------
        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.get_job_status(
                pid_id="pid_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_status(pid_id, request_options=request_options)
        return _response.data

    async def get_output_inference_images(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Gets the inference output image for a given pid id and inference result type.
        param pid: The PID id.
        param inference_result_type: The inference result type.
        rtype: ImageResponse
        The inference output image has information overlayed on the original image
        that provides user insight into what was done in the inferencing service.

        Parameters
        ----------
        inference_result_type : InferenceResult

        pid_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pid_digitization.get_output_inference_images(
                inference_result_type="symbol-detection",
                pid_id="pid_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_output_inference_images(
            inference_result_type, pid_id, request_options=request_options
        )
        return _response.data
