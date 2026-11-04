

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identifier import Identifier
from .location import Location
from .metadata_scheme_versions_item_samples_item import MetadataSchemeVersionsItemSamplesItem
from .metadata_scheme_versions_item_valid import MetadataSchemeVersionsItemValid
from .namespace import Namespace


class MetadataSchemeVersionsItem(UniversalBaseModel):
    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number, code or other string used to identify the version, omitting any initial “v”, “v.” or “ver.”.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full, human understandable name of this version of the metadata scheme. This should be provided only if it differs from the title given for the scheme as a whole.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this version requires some explanation, give it here.
    """

    available: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which this version was made available as a draft or proposal. A version with an `available` date but no `issued` date is assumed not to be approved by its maintainer for use. (This element is provided to allow schemes or versions to be entered into the MSC prior to official approval; retrospectively uncovering this information for versions that have been issued is not encouraged.)
    """

    issued: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which the version was released or published. This also implies the date on which the version was approved for use by its maintainer, unless an explicit `valid` date is also given.
    """

    valid: typing.Optional[MetadataSchemeVersionsItemValid] = pydantic.Field(default=None)
    """
    A version of a scheme is assumed to be approved for use by its maintainer from its `issued` date until the issued date of a subsequent version. If this is not the case, (for example, where multiple versions are approved simultaneously), `valid` expresses the period for which a version is approved for use. If an end date is provided, this indicates the date on which approval was withdrawn; otherwise the version is still considered approved for use, despite the issue of subsequent versions.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about this version of the scheme may be accessed.
    """

    namespaces: typing.Optional[typing.List[Namespace]] = pydantic.Field(default=None)
    """
    Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify this version of the scheme.
    """

    samples: typing.Optional[typing.List[MetadataSchemeVersionsItemSamplesItem]] = pydantic.Field(default=None)
    """
    Metadata records conforming to the scheme.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
