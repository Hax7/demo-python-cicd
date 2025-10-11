# This file contains fake secrets for testing Gitleaks detection
# DO NOT use real secrets here!

# Fake AWS credentials (for testing secret detection)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Fake API key
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz123456"

# Fake database connection string
DATABASE_URL = "postgresql://admin:P@ssw0rd123!@localhost:5432/mydb"

# Fake private key
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
-----END RSA PRIVATE KEY-----"""

print("This file is for testing secret detection only!")
