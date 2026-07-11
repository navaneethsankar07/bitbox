# tool: rgb_to_hex
# description: Converts rgb value to hex code
# author: @persianflower
# example: rgb_to_hex "255" "87" "51" -> "#ff5733"


def run(*args) -> str:
    if len(args) < 3:
        return "Error: rgb_to_hex requires 3 arguments: Red, Blue and Green code"
    
    R,G,B=int(args[0]),int(args[1]),int(args[2])
    Rq=str(hex(R%16))
    Rd=str(hex(R//16))
    Gq=str(hex(G%16))
    Gd=str(hex(G//16))
    Bq=str(hex(B%16))
    Bd=str(hex(B//16))
    code="#"+Rd+Rq+Gd+Gq+Bd+Bq
    code=code.replace("0x","")
    return code