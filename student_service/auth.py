import httpx
import os
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
from functools import lru_cache

"""Loading all the necessary credentials"""
load_dotenv()

URL=os.getenv("KEYCLOAK_URL")
REALM= os.getenv("KEYCLOAK_REALM")
CLIENT=os.getenv("KEYCLOAK_CLIENT_ID")
SECRET=os.getenv("KEYCLOAK_CLIENT_SECRET")

"""URL setup"""
JWKS_URL=f"{URL}/realms/{REALM}/protocol/openid-connect/certs"
TOKEN_URL=f"{URL}/realms/{REALM}/protocol/openid-connect/token"

"""Token for FastAPI connection"""
auth=OAuth2PasswordBearer(tokenUrl=TOKEN_URL)

"""JWK extraction"""
@lru_cache(maxsize=1)
def get_jwk():
    result=httpx.get(JWKS_URL)
    result.raise_for_status()
    return result.json()

"""Token Verification"""

def verify_token(token:str= Depends(auth) ):
    try:
        jwk_answer=get_jwk()
        credentials=jwt.decode(
            token, jwk_answer, algorithms=["RS256"], audience=CLIENT,
            issuer=f"{URL}/realms/{REALM}"
        )
        return credentials
    
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid access")
    
"""Role Handling"""

def require_role(role:str):
    def role_checker(credentials:dict=Depends(verify_token)):
        client_roles=(credentials
                .get("resource_access", {})
                .get("CLIENT_ID", {})
                .get("roles", [])
                )
        
        if role not in client_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        
        return credentials
    return role_checker