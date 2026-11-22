# Blockchain Lab 02
## Transactions, Blocks, and Integrity Validation

### Introduction
This project demonstrates the basic working of blockchain technology using Python.

### Objectives
- Understand blockchain transactions.
- Validate account balances.
- Create blocks.
- Generate SHA-256 hashes.
- Link blocks using previous hashes.
- Detect data tampering.

### Technologies Used
- Python 3
- Google Colab
- hashlib
- JSON

### Transaction Details

| Transaction | Amount | Status |
|---|---:|---|
| Alice to Bob | 60 | Accepted |
| Bob to Alice | 50 | Accepted |

### Final Account Balances

| Account | Initial Balance | Final Balance |
|---|---:|---:|
| Alice | 100 | 90 |
| Bob | 10 | 20 |

### Integrity Validation
- Before Tampering: True
- After Tampering: False
- Tampering Detection: Successful

### Project Files
- `solution.py` — Complete Python source code.
- `README.md` — Project documentation.

### Conclusion
This practical demonstrates how blockchain uses SHA-256 hashing and previous block references to maintain data integrity and detect unauthorized changes.

**Project Type:** Educational Blockchain Simulation
