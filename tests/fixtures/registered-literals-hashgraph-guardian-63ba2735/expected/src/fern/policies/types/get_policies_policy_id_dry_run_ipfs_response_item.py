

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetPoliciesPolicyIdDryRunIpfsResponseItem(UniversalBaseModel):
    create_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ] = None
    document_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentURL"), pydantic.Field(alias="documentURL")
    ] = None
    document: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
