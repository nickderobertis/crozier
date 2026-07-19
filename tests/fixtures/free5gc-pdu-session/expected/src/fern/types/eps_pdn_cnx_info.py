

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EpsPdnCnxInfo(UniversalBaseModel):
    pgw_s8c_fteid: typing_extensions.Annotated[
        str, FieldMetadata(alias="pgwS8cFteid"), pydantic.Field(alias="pgwS8cFteid")
    ]
    pgw_node_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pgwNodeName"), pydantic.Field(alias="pgwNodeName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
