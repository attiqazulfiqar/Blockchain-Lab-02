
import hashlib
import json

def digest(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()

def make_block(index, previous, transactions):
    block = {
        'height': index,
        'previous_hash': previous,
        'transactions': transactions
    }
    block['hash'] = digest(block)
    return block

def validate(chain):
    for i, block in enumerate(chain):
        body = {k: v for k, v in block.items() if k != 'hash'}

        if block['hash'] != digest(body):
            return False, f'block {i} content changed'

        if i and block['previous_hash'] != chain[i-1]['hash']:
            return False, f'block {i} points to wrong previous block'

    return True, 'hash links correct'

balances = {'Alice': 100, 'Bob': 10}

txs = [
    {'from': 'Alice', 'to': 'Bob', 'amount': 60, 'nonce': 1},
    {'from': 'Bob', 'to': 'Alice', 'amount': 50, 'nonce': 1}
]

accepted = []

for t in txs:
    if balances[t['from']] < t['amount']:
        print('REJECT insufficient funds:', t)
    else:
        balances[t['from']] -= t['amount']
        balances[t['to']] += t['amount']
        accepted.append(t)

chain = [make_block(0, '0' * 64, [{'genesis': True}])]
chain.append(make_block(1, chain[0]['hash'], accepted))

print('ACCEPTED:', accepted)
print('BALANCES:', balances)
print('CHAIN:', [(b['height'], b['hash'][:12]) for b in chain])
print('VALID BEFORE TAMPER:', validate(chain))

assert len(accepted) == 2
assert balances == {'Alice': 90, 'Bob': 20}
assert validate(chain)[0]

print('PASS: transaction admission and tamper evidence demonstrated.')
