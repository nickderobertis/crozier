

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PeriodicJobTemplate(UniversalBaseModel):
    kind: str
    label: str
    description: str
    default_id: typing_extensions.Annotated[str, FieldMetadata(alias="defaultId"), pydantic.Field(alias="defaultId")]
    default_args: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="defaultArgs"), pydantic.Field(alias="defaultArgs")
    ]
    default_queue: typing_extensions.Annotated[
        str, FieldMetadata(alias="defaultQueue"), pydantic.Field(alias="defaultQueue")
    ]
    recommended_cron: typing_extensions.Annotated[
        str, FieldMetadata(alias="recommendedCron"), pydantic.Field(alias="recommendedCron")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
