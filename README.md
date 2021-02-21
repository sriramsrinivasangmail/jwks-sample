# JWKS example


## Background

JSON Web Key reference: https://tools.ietf.org/html/rfc7517

### Python references

for jwcrypto: https://jwcrypto.readthedocs.io/en/latest/jwk.html

for pyjwt: https://pyjwt.readthedocs.io/en/stable/usage.html#retrieve-rsa-signing-keys-from-a-jwks-endpoint

## Description of the sample

`jwks.py` - generates a jwks.json file that can be exposed via a JWKS end-point as well as the first (perhaps a current default ) key_id file

This sample also signs a token with one of the keys, verifies it and for a negative test, fails to verify it with a different key)

`test_pyjwt.py` - is a test to simulate a different client program that relies on just the JWKS end-point (and not even using the same JWKCrypto package) to validate a token.


### Example jwks.json

```
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "4-JXWg643j7jLosNYRj6Vu3x0_-wk_kNkxwIYFyhpxU",
      "n": "1RDxdh1_atulWOF9W1jbgYK8k7C4e-cop30BQLGrPr0IXq0t1qf2JbS_5LqIr8YRRjHVdqOWFUkgt8gD3q9qnyiX0IS1LZaXutB_-9t5EdLddo0GGa8PGMu7RM-8G1H0hVs8Cl62sukQUN81yap_ukKYJNtx_UQOYXID_fSZWRgYo8P4NL1OnKwugaQcJBRGW8KTMbfzZSdeTjk0B2ei9OMt71uIoMDgs9m5s-m_OyVfjeqQ56bvd7Ba-ZPHEGn_SLJ1OEcPGhpXXE_uiMEfZJAm46Oj__BK8wrsTqQlHX-M74XkQllgJ4s91YhPxcm9ENbm7TAMsad9KwNDX-PUOw",
      "e": "AQAB",
      "use": "sig",
      "alg": "RS256"
    },
    {
      "kty": "RSA",
      "kid": "bYyHwLNUZA3N28ik8McMULx0Nf_rejL1z5TWacJNF9k",
      "n": "odwng4zjDdx-PhkAzovpXFXT6mr0NYkV9rtmQS-WLWWN3LDR0KWr7zvV49u8ieszjkqlJhHQYJeH9cMNvSovOfHTPQFry35uQcvZ4RdFzlTnOjdxV03OZtv_UrIm2Zz_f-5MVWcN2-iaatWzVav5heI6XX3nhpqcub33s745-27CDigiSqmJKEmxjBlh3tF8M9y-vofpfMsnNzmuIeK4J8NY9lzpVuSWp85csNS7aGBH5P0Omf53N1b2RGewqfsqSc571ruioR-VPUeXBkVOZquJb6nPl03GtPyqJjr35sXnjgNph8QKBXwz66uO4xi7UkBFyDnO7MGPcQlXHqvVUQ",
      "e": "AQAB",
      "use": "sig",
      "alg": "RS256"
    }
  ]
}
```
