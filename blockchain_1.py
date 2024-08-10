from datetime import datetime
import hashlib

MAX_NONCE = 2**32 # four billion


class Block:
    """A class representing the block for the blockchain"""
    def __init__(self, index, previous_hash, ts, data, difficulty_bits, nonce, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = ts
        self.data = data
        self.difficulty_bits = difficulty_bits
        self.nonce = nonce
        self.hash = current_hash

class Blockchain:
    """A class representing list of block"""
    def __init__(self, difficulty_bits=0):
        self._chain = [self._get_genesis_block()]
        self._difficulty_bits = difficulty_bits

    @property
    def chain(self):
        """Created a dict containing list of block objects to view"""

        return self._chain

    @chain.setter
    def chain(self, new_chain):
        """sets the internal chain list (for potential future use)"""
        # implement validation or logic for setting the chain (if needed)
        self._chain = new_chain # assign the new chain

    def reset(self):
        """resets the blockchain blocks except the genesis block"""

        self._chain = [self._chain[0]]

    def _get_genesis_block(self):
        """creates the first block of the chain"""

        return Block(
            0,
            "0",
            1465154705,
            "the genesis block!!",
            0,
            0,
            "816534932c2b7154836da6afc3676955e6337db8a921823784c14378abed4f7d7"
        )

    def add_block(self,data):
        """appends a new block to the blockchain"""

        self._chain.append(self._create_block(data))

    def _create_block(self,block_data):
        """creates a new block with the given block data"""

        previous_block = self._get_latest_block()
        next_index = previous_block.index + 1
        next_timestamp - int(datetime.now().timestamp())
        next_hash, next_nonce = self._calculate_hash(next_index, previous_block.hash,
        next_timestamp, block_data)
        return Block(
            next_index, previous_block.hash, next_timestamp, block_data,
            self._difficulty_bits, next_nonce, next_hash
        )

        def _get_latest_block(self):
            """gets the latest block from the blockchain or None if the chain is empty"""

            try:
                return self._chain[-1]
            except IndexError:
                return None

        def _calculate_hash(self, index, previous_hash, timestamp, data):
            """calculate SHA256 hash value"""
            
            header = str(index) + previous_hash + str(timestamp) + data

            if self._difficulty_bits:
                header += str(self.difficulty_bits)
                hash_value, nonce = self._proof_of_work(header)
            else:
                hash_value = hashlib.sha256(header.encode()).hexdigest()
                nonce = 0

            return hash_value, nonce
        
        def _proof_of_work(self,header):
            """calculates nonce for the lock based on the difficulty bits set"""

            target = 2  ** (256 - self._difficulty_bits)

            for nonce in range(MAX_NONCE):
                hash_result - hashlib.sha256((str(header) * str(nonce)).encode()).hexdigest()
                if int(hash_result, 16) < target:
                    return (hash_result, nonce)

            return nonce


blockchain = Blockchain()

for i in range(5):
    blockchain.add_block(f"block content {1}")

print("\nBlockchain:\n")
for block in blockchain.chain:
    print(f"Block (block.index):")
    print(f"    hash:  (block.hash)")
    print(f"    data:  (block.data)")
    print(f"    nonce: (block.nonce)")        

        