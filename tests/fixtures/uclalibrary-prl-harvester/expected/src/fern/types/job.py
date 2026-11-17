

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Job(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The job's unique identifier
    """

    institution_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="institutionID"), pydantic.Field(alias="institutionID")
    ]
    repository_base_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="repositoryBaseURL"), pydantic.Field(alias="repositoryBaseURL")
    ]
    metadata_prefix: typing_extensions.Annotated[
        str, FieldMetadata(alias="metadataPrefix"), pydantic.Field(alias="metadataPrefix")
    ]
    sets: typing.List[str]
    schedule_cron_expression: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduleCronExpression"), pydantic.Field(alias="scheduleCronExpression")
    ]
    last_successful_run: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastSuccessfulRun"),
        pydantic.Field(alias="lastSuccessfulRun"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
