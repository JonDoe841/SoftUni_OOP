import secrets
ok = secrets.token_hex(100)
for i in range(1000000):
    ok = secrets.token_hex(100)
    print("\033[92m",ok)