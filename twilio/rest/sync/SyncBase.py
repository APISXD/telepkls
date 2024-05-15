r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from typing import Optional

from twilio.base.domain import Domain
from twilio.rest import Client
from twilio.rest.sync.v1 import V1


class SyncBase(Domain):

    def __init__(self, twilio: Client):
        """
        Initialize the Sync Domain

        :returns: Domain for Sync
        """
        super().__init__(twilio, "https://sync.twilio.com")
        self._v1: Optional[V1] = None

    @property
    def v1(self) -> V1:
        """
        :returns: Versions v1 of Sync
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Sync>"
