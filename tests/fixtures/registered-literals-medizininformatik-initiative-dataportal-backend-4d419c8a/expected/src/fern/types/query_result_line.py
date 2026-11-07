

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryResultLine(UniversalBaseModel):
    site_name: typing_extensions.Annotated[str, FieldMetadata(alias="siteName"), pydantic.Field(alias="siteName")]
    number_of_patients: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfPatients"), pydantic.Field(alias="numberOfPatients")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
