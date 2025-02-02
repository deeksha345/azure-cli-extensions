# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterInventoryItem
    from ._models_py3 import ClustersList
    from ._models_py3 import Condition
    from ._models_py3 import Datastore
    from ._models_py3 import DatastoreInventoryItem
    from ._models_py3 import DatastoresList
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExtendedLocation
    from ._models_py3 import GuestAgent
    from ._models_py3 import GuestAgentList
    from ._models_py3 import GuestAgentProfile
    from ._models_py3 import GuestCredential
    from ._models_py3 import HardwareProfile
    from ._models_py3 import Host
    from ._models_py3 import HostsList
    from ._models_py3 import HttpProxyConfiguration
    from ._models_py3 import HybridIdentityMetadata
    from ._models_py3 import HybridIdentityMetadataList
    from ._models_py3 import Identity
    from ._models_py3 import InventoryItem
    from ._models_py3 import InventoryItemDetails
    from ._models_py3 import InventoryItemProperties
    from ._models_py3 import InventoryItemsList
    from ._models_py3 import MachineExtension
    from ._models_py3 import MachineExtensionInstanceView
    from ._models_py3 import MachineExtensionInstanceViewStatus
    from ._models_py3 import MachineExtensionPropertiesInstanceView
    from ._models_py3 import MachineExtensionUpdate
    from ._models_py3 import MachineExtensionsListResult
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceUpdate
    from ._models_py3 import NetworkProfile
    from ._models_py3 import NetworkProfileUpdate
    from ._models_py3 import NicIPAddressSettings
    from ._models_py3 import NicIPSettings
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationsList
    from ._models_py3 import OsProfile
    from ._models_py3 import PlacementProfile
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourcePatch
    from ._models_py3 import ResourcePool
    from ._models_py3 import ResourcePoolInventoryItem
    from ._models_py3 import ResourcePoolsList
    from ._models_py3 import ResourceStatus
    from ._models_py3 import StopVirtualMachineOptions
    from ._models_py3 import StorageProfile
    from ._models_py3 import StorageProfileUpdate
    from ._models_py3 import SystemData
    from ._models_py3 import VCenter
    from ._models_py3 import VCentersList
    from ._models_py3 import VICredential
    from ._models_py3 import VirtualDisk
    from ._models_py3 import VirtualDiskUpdate
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineInventoryItem
    from ._models_py3 import VirtualMachineTemplate
    from ._models_py3 import VirtualMachineTemplateInventoryItem
    from ._models_py3 import VirtualMachineTemplatesList
    from ._models_py3 import VirtualMachineUpdate
    from ._models_py3 import VirtualMachinesList
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkInventoryItem
    from ._models_py3 import VirtualNetworksList
    from ._models_py3 import VirtualSCSIController
except (SyntaxError, ImportError):
    from ._models import Cluster  # type: ignore
    from ._models import ClusterInventoryItem  # type: ignore
    from ._models import ClustersList  # type: ignore
    from ._models import Condition  # type: ignore
    from ._models import Datastore  # type: ignore
    from ._models import DatastoreInventoryItem  # type: ignore
    from ._models import DatastoresList  # type: ignore
    from ._models import ErrorDefinition  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExtendedLocation  # type: ignore
    from ._models import GuestAgent  # type: ignore
    from ._models import GuestAgentList  # type: ignore
    from ._models import GuestAgentProfile  # type: ignore
    from ._models import GuestCredential  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import Host  # type: ignore
    from ._models import HostsList  # type: ignore
    from ._models import HttpProxyConfiguration  # type: ignore
    from ._models import HybridIdentityMetadata  # type: ignore
    from ._models import HybridIdentityMetadataList  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import InventoryItem  # type: ignore
    from ._models import InventoryItemDetails  # type: ignore
    from ._models import InventoryItemProperties  # type: ignore
    from ._models import InventoryItemsList  # type: ignore
    from ._models import MachineExtension  # type: ignore
    from ._models import MachineExtensionInstanceView  # type: ignore
    from ._models import MachineExtensionInstanceViewStatus  # type: ignore
    from ._models import MachineExtensionPropertiesInstanceView  # type: ignore
    from ._models import MachineExtensionUpdate  # type: ignore
    from ._models import MachineExtensionsListResult  # type: ignore
    from ._models import NetworkInterface  # type: ignore
    from ._models import NetworkInterfaceUpdate  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import NetworkProfileUpdate  # type: ignore
    from ._models import NicIPAddressSettings  # type: ignore
    from ._models import NicIPSettings  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationsList  # type: ignore
    from ._models import OsProfile  # type: ignore
    from ._models import PlacementProfile  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourcePatch  # type: ignore
    from ._models import ResourcePool  # type: ignore
    from ._models import ResourcePoolInventoryItem  # type: ignore
    from ._models import ResourcePoolsList  # type: ignore
    from ._models import ResourceStatus  # type: ignore
    from ._models import StopVirtualMachineOptions  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import StorageProfileUpdate  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import VCenter  # type: ignore
    from ._models import VCentersList  # type: ignore
    from ._models import VICredential  # type: ignore
    from ._models import VirtualDisk  # type: ignore
    from ._models import VirtualDiskUpdate  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineInventoryItem  # type: ignore
    from ._models import VirtualMachineTemplate  # type: ignore
    from ._models import VirtualMachineTemplateInventoryItem  # type: ignore
    from ._models import VirtualMachineTemplatesList  # type: ignore
    from ._models import VirtualMachineUpdate  # type: ignore
    from ._models import VirtualMachinesList  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkInventoryItem  # type: ignore
    from ._models import VirtualNetworksList  # type: ignore
    from ._models import VirtualSCSIController  # type: ignore

from ._azure_arc_vmware_management_service_api_enums import (
    CreatedByType,
    DiskMode,
    DiskType,
    IPAddressAllocationMethod,
    IdentityType,
    InventoryType,
    NICType,
    OsType,
    PowerOnBootOption,
    ProvisioningAction,
    ProvisioningState,
    SCSIControllerType,
    StatusLevelTypes,
    StatusTypes,
    VirtualSCSISharing,
)

__all__ = [
    'Cluster',
    'ClusterInventoryItem',
    'ClustersList',
    'Condition',
    'Datastore',
    'DatastoreInventoryItem',
    'DatastoresList',
    'ErrorDefinition',
    'ErrorDetail',
    'ErrorResponse',
    'ExtendedLocation',
    'GuestAgent',
    'GuestAgentList',
    'GuestAgentProfile',
    'GuestCredential',
    'HardwareProfile',
    'Host',
    'HostsList',
    'HttpProxyConfiguration',
    'HybridIdentityMetadata',
    'HybridIdentityMetadataList',
    'Identity',
    'InventoryItem',
    'InventoryItemDetails',
    'InventoryItemProperties',
    'InventoryItemsList',
    'MachineExtension',
    'MachineExtensionInstanceView',
    'MachineExtensionInstanceViewStatus',
    'MachineExtensionPropertiesInstanceView',
    'MachineExtensionUpdate',
    'MachineExtensionsListResult',
    'NetworkInterface',
    'NetworkInterfaceUpdate',
    'NetworkProfile',
    'NetworkProfileUpdate',
    'NicIPAddressSettings',
    'NicIPSettings',
    'Operation',
    'OperationDisplay',
    'OperationsList',
    'OsProfile',
    'PlacementProfile',
    'ProxyResource',
    'Resource',
    'ResourcePatch',
    'ResourcePool',
    'ResourcePoolInventoryItem',
    'ResourcePoolsList',
    'ResourceStatus',
    'StopVirtualMachineOptions',
    'StorageProfile',
    'StorageProfileUpdate',
    'SystemData',
    'VCenter',
    'VCentersList',
    'VICredential',
    'VirtualDisk',
    'VirtualDiskUpdate',
    'VirtualMachine',
    'VirtualMachineInventoryItem',
    'VirtualMachineTemplate',
    'VirtualMachineTemplateInventoryItem',
    'VirtualMachineTemplatesList',
    'VirtualMachineUpdate',
    'VirtualMachinesList',
    'VirtualNetwork',
    'VirtualNetworkInventoryItem',
    'VirtualNetworksList',
    'VirtualSCSIController',
    'CreatedByType',
    'DiskMode',
    'DiskType',
    'IPAddressAllocationMethod',
    'IdentityType',
    'InventoryType',
    'NICType',
    'OsType',
    'PowerOnBootOption',
    'ProvisioningAction',
    'ProvisioningState',
    'SCSIControllerType',
    'StatusLevelTypes',
    'StatusTypes',
    'VirtualSCSISharing',
]
