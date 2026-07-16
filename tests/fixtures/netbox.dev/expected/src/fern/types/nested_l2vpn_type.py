

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NestedL2VpnType(enum.StrEnum):
    VPWS = "vpws"
    VPLS = "vpls"
    VXLAN = "vxlan"
    VXLAN_EVPN = "vxlan-evpn"
    MPLS_EVPN = "mpls-evpn"
    PBB_EVPN = "pbb-evpn"
    EPL = "epl"
    EVPL = "evpl"
    EP_LAN = "ep-lan"
    EVP_LAN = "evp-lan"
    EP_TREE = "ep-tree"
    EVP_TREE = "evp-tree"

    def visit(
        self,
        vpws: typing.Callable[[], T_Result],
        vpls: typing.Callable[[], T_Result],
        vxlan: typing.Callable[[], T_Result],
        vxlan_evpn: typing.Callable[[], T_Result],
        mpls_evpn: typing.Callable[[], T_Result],
        pbb_evpn: typing.Callable[[], T_Result],
        epl: typing.Callable[[], T_Result],
        evpl: typing.Callable[[], T_Result],
        ep_lan: typing.Callable[[], T_Result],
        evp_lan: typing.Callable[[], T_Result],
        ep_tree: typing.Callable[[], T_Result],
        evp_tree: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NestedL2VpnType.VPWS:
            return vpws()
        if self is NestedL2VpnType.VPLS:
            return vpls()
        if self is NestedL2VpnType.VXLAN:
            return vxlan()
        if self is NestedL2VpnType.VXLAN_EVPN:
            return vxlan_evpn()
        if self is NestedL2VpnType.MPLS_EVPN:
            return mpls_evpn()
        if self is NestedL2VpnType.PBB_EVPN:
            return pbb_evpn()
        if self is NestedL2VpnType.EPL:
            return epl()
        if self is NestedL2VpnType.EVPL:
            return evpl()
        if self is NestedL2VpnType.EP_LAN:
            return ep_lan()
        if self is NestedL2VpnType.EVP_LAN:
            return evp_lan()
        if self is NestedL2VpnType.EP_TREE:
            return ep_tree()
        if self is NestedL2VpnType.EVP_TREE:
            return evp_tree()
