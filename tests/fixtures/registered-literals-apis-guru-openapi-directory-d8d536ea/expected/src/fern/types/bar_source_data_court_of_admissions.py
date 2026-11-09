

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataCourtOfAdmissions(UniversalBaseModel):
    court_state_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="courtStateArray"), pydantic.Field(alias="courtStateArray")
    ]
    federal_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="federalArray"), pydantic.Field(alias="federalArray")
    ]
    other_courts_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="otherCourtsArray"), pydantic.Field(alias="otherCourtsArray")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
