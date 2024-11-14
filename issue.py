from cryptography.hazmat import backends
from cryptography.hazmat.primitives import serialization

from truepy import LicenseData, License


# Load the certificate
with open('certificate.pem', 'rb') as f:
    certificate = f.read()

# Load the private key
with open('key.pem', 'rb') as f:
    key = serialization.load_pem_private_key(
        f.read(),
        password=b'MySecretPassword',
        backend=backends.default_backend())

# Issue the license
license = License.issue(
    certificate,
    key,
    license_data=LicenseData(
        '2016-10-01T00:00:00',
        '2020-10-01T00:00:00'))

# Store the license
with open('license.key', 'wb') as f:
    license.store(f, b'LicensePassword')