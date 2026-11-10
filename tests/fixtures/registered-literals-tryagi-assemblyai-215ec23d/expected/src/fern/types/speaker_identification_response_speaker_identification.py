

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpeakerIdentificationResponseSpeakerIdentification(UniversalBaseModel):
    mapping: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    A mapping of the original generic speaker labels (e.g., "A", "B") to the identified speaker names or roles.
    """

    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
