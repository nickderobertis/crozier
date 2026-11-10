

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VerifiablePresentation(UniversalBaseModel):
    hash: str
    id: str
    policy_id: typing_extensions.Annotated[str, FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId")]
    signature: str
    status: str
    tag: str
    type: str
    update_date: typing_extensions.Annotated[str, FieldMetadata(alias="updateDate"), pydantic.Field(alias="updateDate")]
    create_date: typing_extensions.Annotated[str, FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")]
    owner: str
    document: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
