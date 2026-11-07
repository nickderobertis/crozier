

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bot_summary import BotSummary


class BotCreateResponse(UniversalBaseModel):
    bots: typing.List[BotSummary]
    failed_indexes: typing_extensions.Annotated[
        typing.List[int], FieldMetadata(alias="failedIndexes"), pydantic.Field(alias="failedIndexes")
    ]
    job_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jobId"),
        pydantic.Field(
            alias="jobId", description="Present only when existing channels need background bot provisioning."
        ),
    ] = None
    """
    Present only when existing channels need background bot provisioning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
