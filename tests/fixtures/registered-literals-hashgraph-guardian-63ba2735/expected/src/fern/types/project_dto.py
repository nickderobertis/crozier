

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProjectDto(UniversalBaseModel):
    id: str
    policy_id: typing_extensions.Annotated[str, FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId")]
    policy_name: typing_extensions.Annotated[str, FieldMetadata(alias="policyName"), pydantic.Field(alias="policyName")]
    registered: str
    title: str
    company_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ]
    sectoral_scope: typing_extensions.Annotated[
        str, FieldMetadata(alias="sectoralScope"), pydantic.Field(alias="sectoralScope")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
