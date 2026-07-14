

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OperatorWebhookDbtCloud(UniversalBaseModel):
    account_id: typing_extensions.Annotated[int, FieldMetadata(alias="accountId")] = pydantic.Field()
    """
    The account id associated with the job
    """

    job_id: typing_extensions.Annotated[int, FieldMetadata(alias="jobId")] = pydantic.Field()
    """
    The job id associated with the job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
