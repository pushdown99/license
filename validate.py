from truepy import License


# Load the certificate
with open('certificate.pem', 'rb') as f:
    certificate = f.read()

# Load the license
with open('license.key', 'rb') as f:
    license = License.load(f, b'LicensePassword')

# Verify the license; this will raise License.InvalidSignatureException if
# the signature is incorrect
license.verify(certificate)