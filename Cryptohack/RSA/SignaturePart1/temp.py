import binascii
from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes
N = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525181014287214350136557941201445475540830225059514652125310445352175047408966028497316806142156338927162621004774769949534239479839334209147097793526879762417526445739552772039876568156469224491682030314994880247983332964121759307658270083947005466578077153185206199759569902810832114058818478518470715726064960617482910172035743003538122402440142861494899725720505181663738931151677884218457824676140190841393217857683627886497104915390385283364971133316672332846071665082777884028170668140862010444247560019193505999704028222347577

e = 3

a = "VOTE FOR PEDRO"
a = str.encode(a)
print(binascii.hexlify(a))

vote = int(a, 16)

verified_vote = long_to_bytes(pow(vote, ALICE_E, ALICE_N))
print(verified_vote)