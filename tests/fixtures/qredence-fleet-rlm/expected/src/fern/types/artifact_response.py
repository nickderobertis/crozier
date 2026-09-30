

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifact_response_kind import ArtifactResponseKind


class ArtifactResponse(UniversalBaseModel):
    """
    Public artifact metadata — no host or Volume paths.
    """

    id: str
    session_id: str
    run_id: str
    kind: ArtifactResponseKind
    title: typing.Optional[str] = None
    media_type: str
    byte_size: int
    checksum_sha256: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
