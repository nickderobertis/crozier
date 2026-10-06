

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateItemItemsItem(UniversalBaseModel):
    article_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="articleId"), pydantic.Field(alias="articleId")
    ] = None
    qte_cmd: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="qteCmd"), pydantic.Field(alias="qteCmd")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
