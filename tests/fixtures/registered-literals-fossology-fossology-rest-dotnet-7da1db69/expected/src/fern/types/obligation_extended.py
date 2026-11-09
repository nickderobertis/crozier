

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .obligation import Obligation


class ObligationExtended(Obligation):
    modification: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Applies on modified text?
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Obligation is active/inactive
    """

    text_updatable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="textUpdatable"),
        pydantic.Field(alias="textUpdatable", description="Obligation text can be updated?"),
    ] = None
    """
    Obligation text can be updated?
    """

    licenses: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of associated licenses with obligation
    """

    candidate_licenses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="candidateLicenses"),
        pydantic.Field(alias="candidateLicenses", description="List of associated candidate licenses with obligation"),
    ] = None
    """
    List of associated candidate licenses with obligation
    """

    hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    MD5 hash of obligation text
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
