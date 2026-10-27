

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateTeamRequestGroupOdataBind(UniversalBaseModel):
    template_odata_bind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="template@odata.bind"), pydantic.Field(alias="template@odata.bind")
    ] = None
    group_odata_bind: typing_extensions.Annotated[
        str, FieldMetadata(alias="group@odata.bind"), pydantic.Field(alias="group@odata.bind")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
