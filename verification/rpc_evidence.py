"""Allowlist RPC error evidence; never log raw server node configuration."""
import base64
STABLE_ERRORS={'WORKSPACE_NOT_FOUND','INVALID_COUNTERPARTY','INVALID_LABEL','INVALID_CLAUSE_COUNT','INVALID_CLAUSE','UNAUTHORIZED','ALREADY_SEALED','NOT_READY','ALREADY_RECONCILED','NOT_RECONCILED','INVALID_RELATION_INDEX','INVALID_CONSENSUS_OUTPUT'}

def safe_rpc_error(method,error):
    receipt=(error.get('data') or {}).get('receipt') or {}
    result={'rpc_method':method,'rpc_error_code':error.get('code'),'execution_result':receipt.get('execution_result'),'raw_server_detail_retained':False}
    try:
        encoded=receipt.get('result','');data=base64.b64decode(encoded,validate=True)
        text=data[1:].decode('utf-8')
        if data[0]==1 and text in STABLE_ERRORS:
            result.update({'encoded_result':encoded,'decoded_user_error':text})
    except (ValueError,UnicodeError,IndexError,TypeError):pass
    return result

class SafeRPCError(RuntimeError):
    def __init__(self,method,error):
        self.evidence=safe_rpc_error(method,error)
        super().__init__(f"{method}: code={self.evidence['rpc_error_code']} semantic={self.evidence.get('decoded_user_error','RPC_ERROR')}")
