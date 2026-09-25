

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_draft_job_job_type import CreateDraftJobJobType


class CreateDraftJob(UniversalBaseModel):
    job_type: typing_extensions.Annotated[
        CreateDraftJobJobType, FieldMetadata(alias="jobType"), pydantic.Field(alias="jobType")
    ]
    is_draft: typing_extensions.Annotated[bool, FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")]
    title: str
    description: typing.Optional[str] = None
    customer_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")
    ] = None
    customer_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customerReference"), pydantic.Field(alias="customerReference")
    ] = None
    site_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="siteId"), pydantic.Field(alias="siteId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
