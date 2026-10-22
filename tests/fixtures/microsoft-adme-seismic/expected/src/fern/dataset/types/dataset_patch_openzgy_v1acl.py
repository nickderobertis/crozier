

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetPatchOpenzgyV1Acl(UniversalBaseModel):
    """
    The access control tags associated with this entity. This structure is included by the SystemProperties "acl", which is part of all OSDU records. Not extensible.
    """

    owners: typing.List[str] = pydantic.Field()
    """
    The list of owners of this data record formatted as an email (core.common.model.storage.validation.ValidationDoc.EMAIL_REGEX).
    """

    viewers: typing.List[str] = pydantic.Field()
    """
    The list of viewers to which this data record is accessible/visible/discoverable formatted as an email (core.common.model.storage.validation.ValidationDoc.EMAIL_REGEX).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
