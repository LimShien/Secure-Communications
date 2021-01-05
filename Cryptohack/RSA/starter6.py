"""
How can you ensure that the person receiving your message knows that you wrote it?

You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.

When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!

We can protect against these attacks by signing the message.

Imagine you write a message M. You encrypt this message with your friend's public key: C = Me0 mod N0.

To sign this message, you calculate the hash of the message: H(M) and "encrypt" this with your private key: S = H(M)d1 mod N1.


Your friend can decrypt the message using their private key: m = Cd0 mod N0. Using your public key they calculate s = Se1 mod N1.

Now by computing H(m) and comparing it to s: assert H(m) == s, they can ensure that the message you sent them, is the message that they received!

Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.
"""
import hashlib

N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689
m = 'crypto{Immut4ble_m3ssag1ng}'

h = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)

s = pow(h, d, N)

print(hex(s))