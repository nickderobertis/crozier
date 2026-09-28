

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.http_chaos_profile import HttpChaosProfile


class PutMockserverChaosExperimentRequestStagesItem(UniversalBaseModel):
    duration_millis: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="durationMillis"),
        pydantic.Field(
            alias="durationMillis", description="how long this stage runs before advancing (max 86400000 = 24h)"
        ),
    ]
    """
    how long this stage runs before advancing (max 86400000 = 24h)
    """

    profiles: typing.Dict[str, HttpChaosProfile] = pydantic.Field()
    """
    map of host -> chaos profile to apply during this stage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
