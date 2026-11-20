

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetParamsMixedQueryResponse(UniversalBaseModel):
    limit: typing.Optional[float] = None
    statuses: typing.Optional[typing.List[str]] = None
    kebab_case: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="kebab-case"), pydantic.Field(alias="kebab-case")
    ] = None
    author_ids: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
