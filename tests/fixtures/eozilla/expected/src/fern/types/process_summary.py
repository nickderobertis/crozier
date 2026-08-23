

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .description_type import DescriptionType
from .job_control_options import JobControlOptions
from .link import Link
from .transmission_mode import TransmissionMode


class ProcessSummary(DescriptionType):
    id: str
    version: str
    job_control_options: typing_extensions.Annotated[
        typing.Optional[typing.List[JobControlOptions]],
        FieldMetadata(alias="jobControlOptions"),
        pydantic.Field(alias="jobControlOptions"),
    ] = None
    output_transmission: typing_extensions.Annotated[
        typing.Optional[typing.List[TransmissionMode]],
        FieldMetadata(alias="outputTransmission"),
        pydantic.Field(alias="outputTransmission"),
    ] = None
    links: typing.Optional[typing.List[Link]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
