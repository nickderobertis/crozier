

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .label_user import LabelUser


class LabelCard(UniversalBaseModel):
    expiry_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date this card will expire.
    """

    label_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The owner of this card.
    """

    second_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The second line on the card.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the card.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the card.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="The public UUID.")
    ] = None
    """
    The public UUID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
