from jwcrypto import jwt
from jwcrypto import jwk
import json


def get_private_key(pemfile):

    in_file = open(pemfile, "rb") 
    RSAPrivatePEM = in_file.read() 
    in_file.close()

    key = jwk.JWK.from_pem(RSAPrivatePEM)

    return key

## we will add two keys to the key set and export (only the public keys) to a .json file
def genJWKSet():
    
    key = get_private_key("./sample_private_key.pem")
    key_id=key.key_id

    f = open("key_id", "w")
    f.write(key.key_id)
    f.close()

    key2 = get_private_key("./sample_private_key_2.pem")
    key_id_2=key2.key_id

    ks = jwk.JWKSet()
    ks.add(key)
    ks.add(key2)

    jwk_dict=ks.export(private_keys=False,as_dict=True)

    for curr_key in jwk_dict['keys']:
      curr_key["use"] = "sig"
      curr_key["alg"] = "RS256"

    outfile = open("jwks.json", "w")
    json.dump(jwk_dict,outfile)
    outfile.close()
    
    return ks,key_id,key_id_2

## we will use one key to sign something
def test_sign():

    key = get_private_key("sample_private_key.pem")

    payload={
      "username": "tomsawyer",
      "sub": "admin",
      "iss": "KNOXSSO",
      "aud": "DSX",
      "role": "Admin",
      "permissions": [
        "administrator",
        "can_monitor"
      ],
      "display_name": "Tom Sawyer",
    }

    Token = jwt.JWT(header={"alg": "RS256", "kid": key.key_id},
                        claims=payload)
    Token.make_signed_token(key)
    ser=Token.serialize()

    return ser

def get_jwkset():

    jwks_file = open("jwks.json", "rb") 
    jwks_jso = jwks_file.read() 
    jwks_file.close()
    ks = jwk.JWKSet.from_json(jwks_jso)
    
    return ks


def validate_token(tok,kid):
    ks = get_jwkset()

    key = ks.get_key(kid)
    print("validating with: %s " % key.key_id)

    res = jwt.JWT(key=key, jwt=tok)

    print(res.claims)


### Main

key_set,kid,kid_2=genJWKSet()
signed_token=test_sign()
print(signed_token)

## should succeed
validate_token(signed_token,kid)

## should fail
validate_token(signed_token,kid_2)
