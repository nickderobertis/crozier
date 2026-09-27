

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_qa_motion_sweep import TransactionRequestOperationsQaMotionSweep
from .transaction_request_operations_qa_pose_samples_item import TransactionRequestOperationsQaPoseSamplesItem


class TransactionRequestOperationsQa(UniversalBaseModel):
    poses: typing.Optional[typing.List[str]] = None
    pose_samples: typing_extensions.Annotated[
        typing.Optional[typing.List[TransactionRequestOperationsQaPoseSamplesItem]],
        FieldMetadata(alias="poseSamples"),
        pydantic.Field(alias="poseSamples"),
    ] = None
    regions: typing.Optional[typing.List[str]] = None
    width: typing.Optional[float] = None
    height: typing.Optional[float] = None
    physics: typing.Optional[bool] = None
    physics_time: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="physicsTime"), pydantic.Field(alias="physicsTime")
    ] = None
    physics_steps: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="physicsSteps"), pydantic.Field(alias="physicsSteps")
    ] = None
    min_coverage: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minCoverage"), pydantic.Field(alias="minCoverage")
    ] = None
    fail_on_edge_contact: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="failOnEdgeContact"), pydantic.Field(alias="failOnEdgeContact")
    ] = None
    expected_hashes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="expectedHashes"),
        pydantic.Field(alias="expectedHashes"),
    ] = None
    check_triangle_distortion: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="checkTriangleDistortion"),
        pydantic.Field(alias="checkTriangleDistortion"),
    ] = None
    max_triangle_stretch_ratio: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxTriangleStretchRatio"),
        pydantic.Field(alias="maxTriangleStretchRatio"),
    ] = None
    max_triangle_compression_ratio: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxTriangleCompressionRatio"),
        pydantic.Field(alias="maxTriangleCompressionRatio"),
    ] = None
    max_triangle_anisotropy: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxTriangleAnisotropy"),
        pydantic.Field(alias="maxTriangleAnisotropy"),
    ] = None
    motion_sweep: typing_extensions.Annotated[
        typing.Optional[TransactionRequestOperationsQaMotionSweep],
        FieldMetadata(alias="motionSweep"),
        pydantic.Field(alias="motionSweep"),
    ] = None
    supersample: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
