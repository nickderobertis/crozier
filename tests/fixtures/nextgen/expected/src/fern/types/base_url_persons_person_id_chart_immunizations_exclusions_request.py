

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartImmunizationsExclusionsRequest(UniversalBaseModel):
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="CvxCode"), pydantic.Field(alias="CvxCode")]
    reasons: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="Reasons"), pydantic.Field(alias="Reasons")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="StartDate"), pydantic.Field(alias="StartDate")]
    end_date: typing_extensions.Annotated[str, FieldMetadata(alias="EndDate"), pydantic.Field(alias="EndDate")]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
