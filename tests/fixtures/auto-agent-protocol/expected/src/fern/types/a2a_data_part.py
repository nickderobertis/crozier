

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class A2ADataPart(UniversalBaseModel):
    """
    A2A v1.0 DataPart. The presence of the `data` member identifies this as a DataPart; there is no `kind` field. `mediaType` advertises the AAP media type so generic A2A middleware can route or filter without parsing `data`.
    """

    data: typing.Dict[str, typing.Any]
    media_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mediaType"),
        pydantic.Field(
            alias="mediaType",
            description="AAP media type (e.g. `application/vnd.autoagent.<skill>-request+json`). Version-free; the AAP version is announced once via the agent-card extension URI.",
        ),
    ] = None
    """
    AAP media type (e.g. `application/vnd.autoagent.<skill>-request+json`). Version-free; the AAP version is announced once via the agent-card extension URI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
