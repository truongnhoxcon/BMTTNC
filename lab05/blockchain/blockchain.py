from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        block_index = 1
        previous_block = chain[0]

        while block_index < len(chain):
            block = chain[block_index]

            # Kiểm tra hash trước có khớp không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra proof of work
            hash_operation = hashlib.sha256(str(block.proof**2 - previous_block.proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1

        return True
