

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class L2VpnTypeValue(str, enum.Enum):
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
        if self is L2VpnTypeValue.VPWS:
            return vpws()
        if self is L2VpnTypeValue.VPLS:
            return vpls()
        if self is L2VpnTypeValue.VXLAN:
            return vxlan()
        if self is L2VpnTypeValue.VXLAN_EVPN:
            return vxlan_evpn()
        if self is L2VpnTypeValue.MPLS_EVPN:
            return mpls_evpn()
        if self is L2VpnTypeValue.PBB_EVPN:
            return pbb_evpn()
        if self is L2VpnTypeValue.EPL:
            return epl()
        if self is L2VpnTypeValue.EVPL:
            return evpl()
        if self is L2VpnTypeValue.EP_LAN:
            return ep_lan()
        if self is L2VpnTypeValue.EVP_LAN:
            return evp_lan()
        if self is L2VpnTypeValue.EP_TREE:
            return ep_tree()
        if self is L2VpnTypeValue.EVP_TREE:
            return evp_tree()
