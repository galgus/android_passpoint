import typing
from pydantic import v1 as pydantic_v1


class SIMCred(pydantic_v1.BaseModel):
    IMSI: str
    EAPType: str


class DigitalCertificateCred(pydantic_v1.BaseModel):
    """ Defines EAP-TLS credential that is used for the network """
    CertificateType: str
    CertSHA256Fingerprint: str


class UsernamePasswordEAP(pydantic_v1.BaseModel):
    """ Defines the EAP method that will be used for username and password """
    EAPType: str
    InnerMethod: str


class UsernamePasswordCred(pydantic_v1.BaseModel):
    """ Username and password (EAP-TTLS) credential """
    Username: str
    Password: str
    EAPMethod: UsernamePasswordEAP


class CredentialData(pydantic_v1.BaseModel):
    """ Defines the credentials that will be used for the profile """
    Realm: str
    UsernamePassword: typing.Optional[UsernamePasswordCred]
    DigitalCertificate: typing.Optional[DigitalCertificateCred]
    SIM: typing.Optional[SIMCred]


class HomeServiceProviderData(pydantic_v1.BaseModel):
    """ Home service provider data """
    FriendlyName: str
    FQDN: str
    RoamingConsortiumOI: typing.Optional[str]


class Profile(pydantic_v1.BaseModel):
    """ Base for the connection profile """
    HomeSP: HomeServiceProviderData
    Credential: CredentialData

