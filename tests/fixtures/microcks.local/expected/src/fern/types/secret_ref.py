

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SecretRef(UniversalBaseModel):
    """
    Lightweight reference for an existing Secret
    """

    name: str = pydantic.Field()
    """
    Distinct name of the referenced Secret
    """

    secret_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="secretId"),
        pydantic.Field(alias="secretId", description="Unique identifier or referenced Secret"),
    ]
    """
    Unique identifier or referenced Secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
