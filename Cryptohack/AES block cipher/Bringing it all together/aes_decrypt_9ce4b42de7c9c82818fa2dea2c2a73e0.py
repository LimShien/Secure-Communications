from diffusion_ee6215282094b4ae8cd1b20697477712 import inv_mix_columns
from diffusion_ee6215282094b4ae8cd1b20697477712 import inv_shift_rows
from sbox_8fc04ffb95faf5a5e6959195d5e2d94e import sub_bytes
from sbox_8fc04ffb95faf5a5e6959195d5e2d94e import inv_s_box
from sbox_8fc04ffb95faf5a5e6959195d5e2d94e import s_box
N_ROUNDS = 10

key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'



def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    columns_per_iteration = len(key_columns)
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]


def decrypt(key, ciphertext):

    round_keys = expand_key(key) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix


        # Initial add round key step
    #print("round key: " , expand_key(key)[0]  )           
    state=[]
    state = add_round_key(bytes2matrix(ciphertext),round_keys[10])
    #print(bytes2matrix(ciphertext))
    state2 = [[0] * 4 for i in range(4)]
    state2 = list_to_2d(state) 
    #print("initial round key", state2)
    for i in range(N_ROUNDS-1, 0, -1):
        #print(i)
        #print(state2)
        state2=inv_shift_rows(state2)
        #print("invshiftrows", state2)
        state2 = sub_bytes(state2)
        #print("subbytes", state2)
        state2= add_round_key(state2, round_keys[i])
        #print("addroundkey: ", state2)
        state2 = list_to_2d(state2)
        state2 = inv_mix_columns(state2)
        


    state2 = inv_shift_rows(state2)
    state2 = sub_bytes(state2)
    state2 = state2= add_round_key(state2, round_keys[0]) 
    state2 = list_to_2d(state2)    

    return matrix2bytes(state2)
    
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
   """ Converts a 4x4 matrix into a 16-byte array.  """
   result = ""
   for x in matrix:
        for y in x:
            result += chr(y)    
   return result 

def add_round_key(s, k):
    l1 =[]
    l2 =[]

    for x in s:
        for y in x:
            l1.append(y)
    for i in k:
        for j in i:
            l2.append(j)
    
    count=0
    l3 =[]
    while count<len(l1):

        l3.append(l1[count] ^ l2[count])

        count+=1

    
    return l3

def list_to_2d(s):

    n = [[0] * 4 for i in range(4)]
    counter = 0
    for i in range(0,4,1):
        for j in range(0,4,1):
            n[i][j] = s[counter]
            counter +=1
    return n

#print(expand_key(key))
print(decrypt(key, ciphertext))

