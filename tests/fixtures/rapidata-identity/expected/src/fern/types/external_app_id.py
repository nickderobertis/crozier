

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalAppId(enum.StrEnum):
    """
                    The third-party applications that federate on our OIDC `groups` claim and can therefore
                    be administered through a grant here. Each maps to an `external_app` object in the
                    authorization graph.
                    A closed enum rather than a free-form id on purpose: an arbitrary string would let a typo
    write a grant against an object nothing consumes, which looks like access was granted but
    silently is not. Adding an app is a value here plus a tuple — no model change.This is the app itself; the relation vocabulary defined on these objects is
    AuthorizationRelations.ExternalApp. The Id suffix here keeps the two
    distinguishable: a file with using static AuthorizationRelations imports that
    nested enum, and identical short names would make every bare mention ambiguous.
    """

    ARGO_CD = "ArgoCd"
    GRAFANA = "Grafana"

    def visit(self, argo_cd: typing.Callable[[], T_Result], grafana: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExternalAppId.ARGO_CD:
            return argo_cd()
        if self is ExternalAppId.GRAFANA:
            return grafana()
