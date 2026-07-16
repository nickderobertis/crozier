

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegisterPublisherOutput(UniversalBaseModel):
    publisher_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PublisherId")] = (
        pydantic.Field(default=None)
    )
    """
    The ID assigned this account by CloudFormation for publishing extensions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
