import jwt
from jwt import PyJWKClient

token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjQtSlhXZzY0M2o3akxvc05ZUmo2VnUzeDBfLXdrX2tOa3h3SVlGeWhweFUifQ.eyJhdWQiOiJEU1giLCJkaXNwbGF5X25hbWUiOiJUb20gU2F3eWVyIiwiaXNzIjoiS05PWFNTTyIsInBlcm1pc3Npb25zIjpbImFkbWluaXN0cmF0b3IiLCJjYW5fbW9uaXRvciJdLCJyb2xlIjoiQWRtaW4iLCJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoidG9tc2F3eWVyIn0.wVmx9QAOQiBUT23TEG2ghjUcaD5oK7bcRL7Mb9VXCSpa845EzDFYwUynf5LaPF9PFxhjRsy3UhgYDDC1CJQGEa3yFAD-mWIhoQtRpaPrFmIQMjGLxeLsJEKgzAKYLC1fw4wiLUPF3z_ZDmtpczhkHkdPW-L8le8RbGY6rJrBM2OLwJtyY1sRAOX_OmbFsgPKF2gVftxerosZY1WUAbFiWdi2sTrUMmBlXwRSzh0V8MmP9U50xh1r6QsOu_Pq0iqTAasDBepbb0NPvrxX8urkLp2GBsdd-bEhX45DDsCpY_fPYGWEgVzRD1YB5QE5nmovf9h9INP3eWhNUb0Ft5uipA"

url="file:///Users/sriram/work/zen/zen-dev-test-utils/samples/jwks_testing/jwks.json"
jwks_client = PyJWKClient(url)
signing_key = jwks_client.get_signing_key_from_jwt(token)

data = jwt.decode(
     token,
     signing_key.key,
     algorithms=["RS256"],
     audience="DSX",
     options={"verify_exp": True})

print(data)

