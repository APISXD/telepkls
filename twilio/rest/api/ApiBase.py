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
from twilio.rest.api.v2010 import V2010


class ApiBase(Domain):

    def __init__(self, twilio: Client):
        """
        Initialize the Api Domain

        :returns: Domain for Api
        """
        super().__init__(twilio, "https://api.twilio.com")
        self._v2010: Optional[V2010] = None

    @property
    def v2010(self) -> V2010:
        """
        :returns: Versions v2010 of Api
        """
        if self._v2010 is None:
            self._v2010 = V2010(self)
        return self._v2010

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Api>"