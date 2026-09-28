

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_api_playback_reload_response_playback_demo import PostApiPlaybackReloadResponsePlaybackDemo
from .post_api_playback_reload_response_playback_motion import PostApiPlaybackReloadResponsePlaybackMotion


class PostApiPlaybackReloadResponsePlayback(UniversalBaseModel):
    input_contract_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputContractVersion"), pydantic.Field(alias="inputContractVersion")
    ] = None
    version: str
    session_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sessionId"),
        pydantic.Field(
            alias="sessionId", description="Changes on service restart; compare together with modelVersion."
        ),
    ]
    """
    Changes on service restart; compare together with modelVersion.
    """

    revision: int
    model_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="modelVersion"), pydantic.Field(alias="modelVersion")
    ]
    playing: bool
    physics_epoch: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="physicsEpoch"), pydantic.Field(alias="physicsEpoch")
    ] = None
    motion: typing.Optional[PostApiPlaybackReloadResponsePlaybackMotion] = None
    demo: typing.Optional[PostApiPlaybackReloadResponsePlaybackDemo] = None
    values: typing.Dict[str, float] = pydantic.Field()
    """
    Finite model parameter values. Playback also requires known IDs and values within their declared ranges.
    """

    last_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastSource"), pydantic.Field(alias="lastSource")
    ] = None
    connected_outputs: typing_extensions.Annotated[
        int, FieldMetadata(alias="connectedOutputs"), pydantic.Field(alias="connectedOutputs")
    ]
    output_acknowledged: typing_extensions.Annotated[
        str, FieldMetadata(alias="outputAcknowledged"), pydantic.Field(alias="outputAcknowledged")
    ]
    parameters: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
