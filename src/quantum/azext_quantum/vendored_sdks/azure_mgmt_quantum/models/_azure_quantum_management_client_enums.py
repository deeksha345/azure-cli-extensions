# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class ProvisioningStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning status field
    """

    SUCCEEDED = "Succeeded"
    PROVIDER_LAUNCHING = "ProviderLaunching"
    PROVIDER_UPDATING = "ProviderUpdating"
    PROVIDER_DELETING = "ProviderDeleting"
    PROVIDER_PROVISIONING = "ProviderProvisioning"
    FAILED = "Failed"

class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"

class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning status field
    """

    SUCCEEDED = "Succeeded"
    LAUNCHING = "Launching"
    UPDATING = "Updating"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"

class UsableStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the current workspace is ready to accept Jobs.
    """

    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"
