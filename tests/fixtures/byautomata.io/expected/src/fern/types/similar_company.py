

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SimilarCompany(UniversalBaseModel):
    company_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ] = None
    description: typing.Optional[str] = None
    employee: typing.Optional[str] = None
    industry: typing.Optional[str] = None
    linkedin: typing.Optional[str] = None
    title: typing.Optional[str] = None
    twitter: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
