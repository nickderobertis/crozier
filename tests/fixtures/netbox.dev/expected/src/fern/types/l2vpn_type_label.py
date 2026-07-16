

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class L2VpnTypeLabel(str, enum.Enum):
    VPWS = "VPWS"
    VPLS = "VPLS"
    VXLAN = "VXLAN"
    VXLAN_EVPN = "VXLAN-EVPN"
    MPLS_EVPN = "MPLS EVPN"
    PBB_EVPN = "PBB EVPN"
    EPL = "EPL"
    EVPL = "EVPL"
    ETHERNET_PRIVATE_LAN = "Ethernet Private LAN"
    ETHERNET_VIRTUAL_PRIVATE_LAN = "Ethernet Virtual Private LAN"
    ETHERNET_PRIVATE_TREE = "Ethernet Private Tree"
    ETHERNET_VIRTUAL_PRIVATE_TREE = "Ethernet Virtual Private Tree"

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
        ethernet_private_lan: typing.Callable[[], T_Result],
        ethernet_virtual_private_lan: typing.Callable[[], T_Result],
        ethernet_private_tree: typing.Callable[[], T_Result],
        ethernet_virtual_private_tree: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is L2VpnTypeLabel.VPWS:
            return vpws()
        if self is L2VpnTypeLabel.VPLS:
            return vpls()
        if self is L2VpnTypeLabel.VXLAN:
            return vxlan()
        if self is L2VpnTypeLabel.VXLAN_EVPN:
            return vxlan_evpn()
        if self is L2VpnTypeLabel.MPLS_EVPN:
            return mpls_evpn()
        if self is L2VpnTypeLabel.PBB_EVPN:
            return pbb_evpn()
        if self is L2VpnTypeLabel.EPL:
            return epl()
        if self is L2VpnTypeLabel.EVPL:
            return evpl()
        if self is L2VpnTypeLabel.ETHERNET_PRIVATE_LAN:
            return ethernet_private_lan()
        if self is L2VpnTypeLabel.ETHERNET_VIRTUAL_PRIVATE_LAN:
            return ethernet_virtual_private_lan()
        if self is L2VpnTypeLabel.ETHERNET_PRIVATE_TREE:
            return ethernet_private_tree()
        if self is L2VpnTypeLabel.ETHERNET_VIRTUAL_PRIVATE_TREE:
            return ethernet_virtual_private_tree()
