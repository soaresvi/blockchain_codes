import datetime as d
import hashlib as h
from sqlite3 import Timestamp

class Block:
    def __init__(self, index, timestamp, data, prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash

        self.hash = self.hashblock()

    def hashblock(self):
        block_encryption = h.sha256()
        block_encryption.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.prevhash))
        return block_encryption.hexdigest()
    
    @staticmethod
    def genesisblock():
        return Block(0, d.datetime.now(), "genesis block trabsaction", " ")

    @staticmethod
    def newBlock(lastblock):
        index = lastblock.index+1
        timestamp = d.datetime.now()
        hashblock = lastblock.hash
        data = "Transaction "+str(index)
        return Block(index, timestamp, data, hashblock)

blockchain = [Block.genesisblock()]
prevblock = blockchain[0]

for i in range (0,5):
    addblock = Block.newblock(prevblock)
    blockchain.append(addblock)
    prevblock =addblock

    print("Block ID {} ".format(addblock.index))
    print("Timestamp:{}".format(addblock.timestamp))
    print("Hash of the block:{}".format(addblock.hash))
    print("Previous Block Hash:{}".format(addblock.prevhash))
    print("data:{}\n".format(addblock.data))
