r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ComplianceRegistrationInquiriesInstance(InstanceResource):

    class BusinessIdentityType(object):
        DIRECT_CUSTOMER = "direct_customer"
        ISV_RESELLER_OR_PARTNER = "isv_reseller_or_partner"
        UNKNOWN = "unknown"

    class BusinessRegistrationAuthority(object):
        UK_CRN = "UK:CRN"
        US_EIN = "US:EIN"
        CA_CBN = "CA:CBN"
        AU_ACN = "AU:ACN"
        OTHER = "Other"

    class EndUserType(object):
        INDIVIDUAL = "Individual"
        BUSINESS = "Business"

    class PhoneNumberType(object):
        LOCAL = "local"
        NATIONAL = "national"
        MOBILE = "mobile"
        TOLL_FREE = "toll-free"

    """
    :ivar inquiry_id: The unique ID used to start an embedded compliance registration session.
    :ivar inquiry_session_token: The session token used to start an embedded compliance registration session.
    :ivar registration_id: The RegistrationId matching the Registration Profile that should be resumed or resubmitted for editing.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        registration_id: Optional[str] = None,
    ):
        super().__init__(version)

        self.inquiry_id: Optional[str] = payload.get("inquiry_id")
        self.inquiry_session_token: Optional[str] = payload.get("inquiry_session_token")
        self.registration_id: Optional[str] = payload.get("registration_id")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "registration_id": registration_id or self.registration_id,
        }
        self._context: Optional[ComplianceRegistrationInquiriesContext] = None

    @property
    def _proxy(self) -> "ComplianceRegistrationInquiriesContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ComplianceRegistrationInquiriesContext for this ComplianceRegistrationInquiriesInstance
        """
        if self._context is None:
            self._context = ComplianceRegistrationInquiriesContext(
                self._version,
                registration_id=self._solution["registration_id"],
            )
        return self._context

    def update(
        self,
        is_isv_embed: Union[bool, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> "ComplianceRegistrationInquiriesInstance":
        """
        Update the ComplianceRegistrationInquiriesInstance

        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The updated ComplianceRegistrationInquiriesInstance
        """
        return self._proxy.update(
            is_isv_embed=is_isv_embed,
            theme_set_id=theme_set_id,
        )

    async def update_async(
        self,
        is_isv_embed: Union[bool, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> "ComplianceRegistrationInquiriesInstance":
        """
        Asynchronous coroutine to update the ComplianceRegistrationInquiriesInstance

        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The updated ComplianceRegistrationInquiriesInstance
        """
        return await self._proxy.update_async(
            is_isv_embed=is_isv_embed,
            theme_set_id=theme_set_id,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.ComplianceRegistrationInquiriesInstance {}>".format(
            context
        )


class ComplianceRegistrationInquiriesContext(InstanceContext):

    def __init__(self, version: Version, registration_id: str):
        """
        Initialize the ComplianceRegistrationInquiriesContext

        :param version: Version that contains the resource
        :param registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation call.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "registration_id": registration_id,
        }
        self._uri = "/ComplianceInquiries/Registration/{registration_id}/RegulatoryCompliance/GB/Initialize".format(
            **self._solution
        )

    def update(
        self,
        is_isv_embed: Union[bool, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Update the ComplianceRegistrationInquiriesInstance

        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The updated ComplianceRegistrationInquiriesInstance
        """
        data = values.of(
            {
                "IsIsvEmbed": serialize.boolean_to_string(is_isv_embed),
                "ThemeSetId": theme_set_id,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(
            self._version, payload, registration_id=self._solution["registration_id"]
        )

    async def update_async(
        self,
        is_isv_embed: Union[bool, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Asynchronous coroutine to update the ComplianceRegistrationInquiriesInstance

        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The updated ComplianceRegistrationInquiriesInstance
        """
        data = values.of(
            {
                "IsIsvEmbed": serialize.boolean_to_string(is_isv_embed),
                "ThemeSetId": theme_set_id,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(
            self._version, payload, registration_id=self._solution["registration_id"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.ComplianceRegistrationInquiriesContext {}>".format(
            context
        )


class ComplianceRegistrationInquiriesList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ComplianceRegistrationInquiriesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = (
            "/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize"
        )

    def create(
        self,
        end_user_type: "ComplianceRegistrationInquiriesInstance.EndUserType",
        phone_number_type: "ComplianceRegistrationInquiriesInstance.PhoneNumberType",
        business_identity_type: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessIdentityType", object
        ] = values.unset,
        business_registration_authority: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessRegistrationAuthority",
            object,
        ] = values.unset,
        business_legal_name: Union[str, object] = values.unset,
        notification_email: Union[str, object] = values.unset,
        accepted_notification_receipt: Union[bool, object] = values.unset,
        business_registration_number: Union[str, object] = values.unset,
        business_website_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        authorized_representative1_first_name: Union[str, object] = values.unset,
        authorized_representative1_last_name: Union[str, object] = values.unset,
        authorized_representative1_phone: Union[str, object] = values.unset,
        authorized_representative1_email: Union[str, object] = values.unset,
        authorized_representative1_date_of_birth: Union[str, object] = values.unset,
        address_street: Union[str, object] = values.unset,
        address_street_secondary: Union[str, object] = values.unset,
        address_city: Union[str, object] = values.unset,
        address_subdivision: Union[str, object] = values.unset,
        address_postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        emergency_address_street: Union[str, object] = values.unset,
        emergency_address_street_secondary: Union[str, object] = values.unset,
        emergency_address_city: Union[str, object] = values.unset,
        emergency_address_subdivision: Union[str, object] = values.unset,
        emergency_address_postal_code: Union[str, object] = values.unset,
        emergency_address_country_code: Union[str, object] = values.unset,
        use_address_as_emergency_address: Union[bool, object] = values.unset,
        file_name: Union[str, object] = values.unset,
        file: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
        individual_email: Union[str, object] = values.unset,
        individual_phone: Union[str, object] = values.unset,
        is_isv_embed: Union[bool, object] = values.unset,
        isv_registering_for_self_or_tenant: Union[str, object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Create the ComplianceRegistrationInquiriesInstance

        :param end_user_type:
        :param phone_number_type:
        :param business_identity_type:
        :param business_registration_authority:
        :param business_legal_name: he name of the business or organization using the Tollfree number.
        :param notification_email: he email address to receive the notification about the verification result.
        :param accepted_notification_receipt: The email address to receive the notification about the verification result.
        :param business_registration_number: Business registration number of the business
        :param business_website_url: The URL of the business website
        :param friendly_name: Friendly name for your business information
        :param authorized_representative1_first_name: First name of the authorized representative
        :param authorized_representative1_last_name: Last name of the authorized representative
        :param authorized_representative1_phone: Phone number of the authorized representative
        :param authorized_representative1_email: Email address of the authorized representative
        :param authorized_representative1_date_of_birth: Birthdate of the authorized representative
        :param address_street: Street address of the business
        :param address_street_secondary: Street address of the business
        :param address_city: City of the business
        :param address_subdivision: State or province of the business
        :param address_postal_code: Postal code of the business
        :param address_country_code: Country code of the business
        :param emergency_address_street: Street address of the business
        :param emergency_address_street_secondary: Street address of the business
        :param emergency_address_city: City of the business
        :param emergency_address_subdivision: State or province of the business
        :param emergency_address_postal_code: Postal code of the business
        :param emergency_address_country_code: Country code of the business
        :param use_address_as_emergency_address: Use the business address as the emergency address
        :param file_name: The name of the verification document to upload
        :param file: The verification document to upload
        :param first_name: The first name of the Individual User.
        :param last_name: The last name of the Individual User.
        :param date_of_birth: The date of birth of the Individual User.
        :param individual_email: The email address of the Individual User.
        :param individual_phone: The phone number of the Individual User.
        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
        :param status_callback_url: The url we call to inform you of bundle changes.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The created ComplianceRegistrationInquiriesInstance
        """

        data = values.of(
            {
                "EndUserType": end_user_type,
                "PhoneNumberType": phone_number_type,
                "BusinessIdentityType": business_identity_type,
                "BusinessRegistrationAuthority": business_registration_authority,
                "BusinessLegalName": business_legal_name,
                "NotificationEmail": notification_email,
                "AcceptedNotificationReceipt": serialize.boolean_to_string(
                    accepted_notification_receipt
                ),
                "BusinessRegistrationNumber": business_registration_number,
                "BusinessWebsiteUrl": business_website_url,
                "FriendlyName": friendly_name,
                "AuthorizedRepresentative1FirstName": authorized_representative1_first_name,
                "AuthorizedRepresentative1LastName": authorized_representative1_last_name,
                "AuthorizedRepresentative1Phone": authorized_representative1_phone,
                "AuthorizedRepresentative1Email": authorized_representative1_email,
                "AuthorizedRepresentative1DateOfBirth": authorized_representative1_date_of_birth,
                "AddressStreet": address_street,
                "AddressStreetSecondary": address_street_secondary,
                "AddressCity": address_city,
                "AddressSubdivision": address_subdivision,
                "AddressPostalCode": address_postal_code,
                "AddressCountryCode": address_country_code,
                "EmergencyAddressStreet": emergency_address_street,
                "EmergencyAddressStreetSecondary": emergency_address_street_secondary,
                "EmergencyAddressCity": emergency_address_city,
                "EmergencyAddressSubdivision": emergency_address_subdivision,
                "EmergencyAddressPostalCode": emergency_address_postal_code,
                "EmergencyAddressCountryCode": emergency_address_country_code,
                "UseAddressAsEmergencyAddress": serialize.boolean_to_string(
                    use_address_as_emergency_address
                ),
                "FileName": file_name,
                "File": file,
                "FirstName": first_name,
                "LastName": last_name,
                "DateOfBirth": date_of_birth,
                "IndividualEmail": individual_email,
                "IndividualPhone": individual_phone,
                "IsIsvEmbed": serialize.boolean_to_string(is_isv_embed),
                "IsvRegisteringForSelfOrTenant": isv_registering_for_self_or_tenant,
                "StatusCallbackUrl": status_callback_url,
                "ThemeSetId": theme_set_id,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(self._version, payload)

    async def create_async(
        self,
        end_user_type: "ComplianceRegistrationInquiriesInstance.EndUserType",
        phone_number_type: "ComplianceRegistrationInquiriesInstance.PhoneNumberType",
        business_identity_type: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessIdentityType", object
        ] = values.unset,
        business_registration_authority: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessRegistrationAuthority",
            object,
        ] = values.unset,
        business_legal_name: Union[str, object] = values.unset,
        notification_email: Union[str, object] = values.unset,
        accepted_notification_receipt: Union[bool, object] = values.unset,
        business_registration_number: Union[str, object] = values.unset,
        business_website_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        authorized_representative1_first_name: Union[str, object] = values.unset,
        authorized_representative1_last_name: Union[str, object] = values.unset,
        authorized_representative1_phone: Union[str, object] = values.unset,
        authorized_representative1_email: Union[str, object] = values.unset,
        authorized_representative1_date_of_birth: Union[str, object] = values.unset,
        address_street: Union[str, object] = values.unset,
        address_street_secondary: Union[str, object] = values.unset,
        address_city: Union[str, object] = values.unset,
        address_subdivision: Union[str, object] = values.unset,
        address_postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        emergency_address_street: Union[str, object] = values.unset,
        emergency_address_street_secondary: Union[str, object] = values.unset,
        emergency_address_city: Union[str, object] = values.unset,
        emergency_address_subdivision: Union[str, object] = values.unset,
        emergency_address_postal_code: Union[str, object] = values.unset,
        emergency_address_country_code: Union[str, object] = values.unset,
        use_address_as_emergency_address: Union[bool, object] = values.unset,
        file_name: Union[str, object] = values.unset,
        file: Union[str, object] = values.unset,
        first_name: Union[str, object] = values.unset,
        last_name: Union[str, object] = values.unset,
        date_of_birth: Union[str, object] = values.unset,
        individual_email: Union[str, object] = values.unset,
        individual_phone: Union[str, object] = values.unset,
        is_isv_embed: Union[bool, object] = values.unset,
        isv_registering_for_self_or_tenant: Union[str, object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        theme_set_id: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Asynchronously create the ComplianceRegistrationInquiriesInstance

        :param end_user_type:
        :param phone_number_type:
        :param business_identity_type:
        :param business_registration_authority:
        :param business_legal_name: he name of the business or organization using the Tollfree number.
        :param notification_email: he email address to receive the notification about the verification result.
        :param accepted_notification_receipt: The email address to receive the notification about the verification result.
        :param business_registration_number: Business registration number of the business
        :param business_website_url: The URL of the business website
        :param friendly_name: Friendly name for your business information
        :param authorized_representative1_first_name: First name of the authorized representative
        :param authorized_representative1_last_name: Last name of the authorized representative
        :param authorized_representative1_phone: Phone number of the authorized representative
        :param authorized_representative1_email: Email address of the authorized representative
        :param authorized_representative1_date_of_birth: Birthdate of the authorized representative
        :param address_street: Street address of the business
        :param address_street_secondary: Street address of the business
        :param address_city: City of the business
        :param address_subdivision: State or province of the business
        :param address_postal_code: Postal code of the business
        :param address_country_code: Country code of the business
        :param emergency_address_street: Street address of the business
        :param emergency_address_street_secondary: Street address of the business
        :param emergency_address_city: City of the business
        :param emergency_address_subdivision: State or province of the business
        :param emergency_address_postal_code: Postal code of the business
        :param emergency_address_country_code: Country code of the business
        :param use_address_as_emergency_address: Use the business address as the emergency address
        :param file_name: The name of the verification document to upload
        :param file: The verification document to upload
        :param first_name: The first name of the Individual User.
        :param last_name: The last name of the Individual User.
        :param date_of_birth: The date of birth of the Individual User.
        :param individual_email: The email address of the Individual User.
        :param individual_phone: The phone number of the Individual User.
        :param is_isv_embed: Indicates if the inquiry is being started from an ISV embedded component.
        :param isv_registering_for_self_or_tenant: Indicates if the isv registering for self or tenant.
        :param status_callback_url: The url we call to inform you of bundle changes.
        :param theme_set_id: Theme id for styling the inquiry form.

        :returns: The created ComplianceRegistrationInquiriesInstance
        """

        data = values.of(
            {
                "EndUserType": end_user_type,
                "PhoneNumberType": phone_number_type,
                "BusinessIdentityType": business_identity_type,
                "BusinessRegistrationAuthority": business_registration_authority,
                "BusinessLegalName": business_legal_name,
                "NotificationEmail": notification_email,
                "AcceptedNotificationReceipt": serialize.boolean_to_string(
                    accepted_notification_receipt
                ),
                "BusinessRegistrationNumber": business_registration_number,
                "BusinessWebsiteUrl": business_website_url,
                "FriendlyName": friendly_name,
                "AuthorizedRepresentative1FirstName": authorized_representative1_first_name,
                "AuthorizedRepresentative1LastName": authorized_representative1_last_name,
                "AuthorizedRepresentative1Phone": authorized_representative1_phone,
                "AuthorizedRepresentative1Email": authorized_representative1_email,
                "AuthorizedRepresentative1DateOfBirth": authorized_representative1_date_of_birth,
                "AddressStreet": address_street,
                "AddressStreetSecondary": address_street_secondary,
                "AddressCity": address_city,
                "AddressSubdivision": address_subdivision,
                "AddressPostalCode": address_postal_code,
                "AddressCountryCode": address_country_code,
                "EmergencyAddressStreet": emergency_address_street,
                "EmergencyAddressStreetSecondary": emergency_address_street_secondary,
                "EmergencyAddressCity": emergency_address_city,
                "EmergencyAddressSubdivision": emergency_address_subdivision,
                "EmergencyAddressPostalCode": emergency_address_postal_code,
                "EmergencyAddressCountryCode": emergency_address_country_code,
                "UseAddressAsEmergencyAddress": serialize.boolean_to_string(
                    use_address_as_emergency_address
                ),
                "FileName": file_name,
                "File": file,
                "FirstName": first_name,
                "LastName": last_name,
                "DateOfBirth": date_of_birth,
                "IndividualEmail": individual_email,
                "IndividualPhone": individual_phone,
                "IsIsvEmbed": serialize.boolean_to_string(is_isv_embed),
                "IsvRegisteringForSelfOrTenant": isv_registering_for_self_or_tenant,
                "StatusCallbackUrl": status_callback_url,
                "ThemeSetId": theme_set_id,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(self._version, payload)

    def get(self, registration_id: str) -> ComplianceRegistrationInquiriesContext:
        """
        Constructs a ComplianceRegistrationInquiriesContext

        :param registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation call.
        """
        return ComplianceRegistrationInquiriesContext(
            self._version, registration_id=registration_id
        )

    def __call__(self, registration_id: str) -> ComplianceRegistrationInquiriesContext:
        """
        Constructs a ComplianceRegistrationInquiriesContext

        :param registration_id: The unique RegistrationId matching the Regulatory Compliance Inquiry that should be resumed or resubmitted. This value will have been returned by the initial Regulatory Compliance Inquiry creation call.
        """
        return ComplianceRegistrationInquiriesContext(
            self._version, registration_id=registration_id
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.ComplianceRegistrationInquiriesList>"
