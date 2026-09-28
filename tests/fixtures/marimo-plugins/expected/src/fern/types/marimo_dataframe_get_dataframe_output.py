

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MarimoDataframeGetDataframeOutput(UniversalBaseModel):
    url: str
    total_rows: float
    row_headers: typing.List[typing.List[typing.Any]]
    field_types: typing.List[typing.List[typing.Any]]
    column_types_per_step: typing.List[typing.List[typing.List[typing.Any]]]
    python_code: typing.Optional[str] = None
    sql_code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
