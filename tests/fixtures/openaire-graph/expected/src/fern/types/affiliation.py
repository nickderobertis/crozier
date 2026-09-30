

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organization_pid import OrganizationPid


class Affiliation(UniversalBaseModel):
    legal_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="legalName"), pydantic.Field(alias="legalName")
    ] = None
    acronym: typing.Optional[str] = None
    id: typing.Optional[str] = None
    pids: typing.Optional[typing.List[OrganizationPid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
