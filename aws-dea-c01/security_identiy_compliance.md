# Security, Identity, and Compliance
## IAM (Identity Policies and Access Management)
- IAM Policy Document that helps securely control access to AWS resources. It allows you to manage users, security credentials (like access keys), and permissions that control which AWS resource users and applications can access.
- Best practices:
  - Principle of least privilege: granting only the permissions required to perform a task
  - Regularly rotate security credentials
  - Use IAM roles for applications running on EC2 instances.

## Key Management Service (KMS)
- Data is encrypted before sending and decrypted after receiving
- Server-side encryption at rest:
  - Data is encrypted after being received by the server
  - Data is decrypted before being sent
  - It's stored in an encrypted form (usually a data key)
- Client-side encryption:
  - Data is encrypted by the client and never decrypted the server
  - Data will be decrypted by a receiving client
  - The server should not be able to decrypt the data
  - Could leverage Envelope Encryption
- KMS Keys Types
  - KMS Keys is the new name of KMS Customer Master Key
  - Symmetric (AES-256 keys)
    - Single encryption key that is used to Encrypt and Decrypt
    - AWS services that are integrated with KMS use Symmetric CMKs
  - Asymmetric (RSA and ECC key pairs)
    - Public (encrypt) and private key (decrypt) pair
    - Used for Encrypt/Decrypt, or Sign/Verify operations
    - The public key is downloadable, but you can't access the Private key uncrypted
  - AWS Owned Keys, AWS Managed Key: free
- Automatic Key rotation:
  - AWS-managed KMS Key: automatic every 1 year
  - Customer-managed KMS Key: automatic every 1 year
  - Imported KMS Key: only manual rotation possible using alias

## Amazon Macie
- Fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS.
- Macie helps identify and alert you to sensitive data, such as personally identification information (PII)
- S3 buckets --analyze--> Macie (Discover Sensitive Data) --notify--> EventBride --integration-->


## AWS Secrets Manager
- Managing, retrieving, and rotating database credentials, API keys, and other secrets throughout their lifecycle.
- Secure Storage of Secrets:
  - Secrets are encrypted using encryption keys that are created using AWS Key Management Service (KMS). This ensures that the secrets are stored securely.

