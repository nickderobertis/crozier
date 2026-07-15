

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class Choice(UniversalBaseModel):
    """
    `Choice`
    """

    choose: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of items to pick from the list.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the choice to be made.
    """

    from_: typing_extensions.Annotated[typing.Optional["OptionSet"], FieldMetadata(alias="from")] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the resources to choose from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .option_set import OptionSet

update_forward_refs(Choice)
