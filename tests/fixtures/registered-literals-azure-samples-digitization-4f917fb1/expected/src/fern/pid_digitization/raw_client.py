

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bounding_box import BoundingBox
from ..types.connected_symbols_item import ConnectedSymbolsItem
from ..types.http_validation_error import HttpValidationError
from ..types.image_details import ImageDetails
from ..types.inference_result import InferenceResult
from ..types.label import Label
from ..types.symbol_and_text_associated import SymbolAndTextAssociated
from ..types.symbol_detection_inference_response import SymbolDetectionInferenceResponse
from ..types.text_detection_inference_response import TextDetectionInferenceResponse
from ..types.text_recognized import TextRecognized
from .types.get_inference_results_api_pid_digitization_inference_result_type_pid_id_get_response import (
    GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPidDigitizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def detect_symbols(
        self,
        pid_id: str,
        *,
        file: core.File,
        bounding_box_inclusive_str: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SymbolDetectionInferenceResponse]:
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
        HttpResponse[SymbolDetectionInferenceResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/symbol-detection/{encode_path_param(pid_id)}",
            method="POST",
            data={
                "bounding_box_inclusive_str": json.dumps(jsonable_encoder(bounding_box_inclusive_str))
                if bounding_box_inclusive_str is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SymbolDetectionInferenceResponse,
                    parse_obj_as(
                        type_=SymbolDetectionInferenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def detect_text(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        label: typing.Sequence[Label],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TextDetectionInferenceResponse]:
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
        HttpResponse[TextDetectionInferenceResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/text-detection/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "bounding_box_inclusive": convert_and_respect_annotation_metadata(
                    object_=bounding_box_inclusive, annotation=BoundingBox, direction="write"
                ),
                "label": convert_and_respect_annotation_metadata(
                    object_=label, annotation=typing.Sequence[Label], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TextDetectionInferenceResponse,
                    parse_obj_as(
                        type_=TextDetectionInferenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-construction/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "bounding_box_inclusive": convert_and_respect_annotation_metadata(
                    object_=bounding_box_inclusive, annotation=BoundingBox, direction="write"
                ),
                "all_text_list": convert_and_respect_annotation_metadata(
                    object_=all_text_list, annotation=typing.Sequence[TextRecognized], direction="write"
                ),
                "text_and_symbols_associated_list": convert_and_respect_annotation_metadata(
                    object_=text_and_symbols_associated_list,
                    annotation=typing.Sequence[SymbolAndTextAssociated],
                    direction="write",
                ),
                "hough_threshold": hough_threshold,
                "hough_min_line_length": hough_min_line_length,
                "hough_max_line_gap": hough_max_line_gap,
                "hough_rho": hough_rho,
                "hough_theta": hough_theta,
                "thinning_enabled": thinning_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def persist_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        connected_symbols: typing.Sequence[ConnectedSymbolsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-persistence/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "connected_symbols": convert_and_respect_annotation_metadata(
                    object_=connected_symbols, annotation=typing.Sequence[ConnectedSymbolsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_inference_results(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse]:
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
        HttpResponse[GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/{encode_path_param(inference_result_type)}/{encode_path_param(pid_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
                    parse_obj_as(
                        type_=GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_job_status(
        self, pid_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-construction/{encode_path_param(pid_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_output_inference_images(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/{encode_path_param(inference_result_type)}/{encode_path_param(pid_id)}/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPidDigitizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def detect_symbols(
        self,
        pid_id: str,
        *,
        file: core.File,
        bounding_box_inclusive_str: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SymbolDetectionInferenceResponse]:
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
        AsyncHttpResponse[SymbolDetectionInferenceResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/symbol-detection/{encode_path_param(pid_id)}",
            method="POST",
            data={
                "bounding_box_inclusive_str": json.dumps(jsonable_encoder(bounding_box_inclusive_str))
                if bounding_box_inclusive_str is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SymbolDetectionInferenceResponse,
                    parse_obj_as(
                        type_=SymbolDetectionInferenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def detect_text(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        label: typing.Sequence[Label],
        bounding_box_inclusive: typing.Optional[BoundingBox] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TextDetectionInferenceResponse]:
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
        AsyncHttpResponse[TextDetectionInferenceResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/text-detection/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "bounding_box_inclusive": convert_and_respect_annotation_metadata(
                    object_=bounding_box_inclusive, annotation=BoundingBox, direction="write"
                ),
                "label": convert_and_respect_annotation_metadata(
                    object_=label, annotation=typing.Sequence[Label], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TextDetectionInferenceResponse,
                    parse_obj_as(
                        type_=TextDetectionInferenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-construction/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "bounding_box_inclusive": convert_and_respect_annotation_metadata(
                    object_=bounding_box_inclusive, annotation=BoundingBox, direction="write"
                ),
                "all_text_list": convert_and_respect_annotation_metadata(
                    object_=all_text_list, annotation=typing.Sequence[TextRecognized], direction="write"
                ),
                "text_and_symbols_associated_list": convert_and_respect_annotation_metadata(
                    object_=text_and_symbols_associated_list,
                    annotation=typing.Sequence[SymbolAndTextAssociated],
                    direction="write",
                ),
                "hough_threshold": hough_threshold,
                "hough_min_line_length": hough_min_line_length,
                "hough_max_line_gap": hough_max_line_gap,
                "hough_rho": hough_rho,
                "hough_theta": hough_theta,
                "thinning_enabled": thinning_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def persist_graph(
        self,
        pid_id: str,
        *,
        image_url: str,
        image_details: ImageDetails,
        connected_symbols: typing.Sequence[ConnectedSymbolsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-persistence/{encode_path_param(pid_id)}",
            method="POST",
            json={
                "image_url": image_url,
                "image_details": convert_and_respect_annotation_metadata(
                    object_=image_details, annotation=ImageDetails, direction="write"
                ),
                "connected_symbols": convert_and_respect_annotation_metadata(
                    object_=connected_symbols, annotation=typing.Sequence[ConnectedSymbolsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_inference_results(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse]:
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
        AsyncHttpResponse[GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/{encode_path_param(inference_result_type)}/{encode_path_param(pid_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
                    parse_obj_as(
                        type_=GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_job_status(
        self, pid_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/graph-construction/{encode_path_param(pid_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_output_inference_images(
        self,
        inference_result_type: InferenceResult,
        pid_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pid-digitization/{encode_path_param(inference_result_type)}/{encode_path_param(pid_id)}/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
