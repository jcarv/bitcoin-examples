from bitcoin.rpc import RawProxy

# Create a connection to local Bitcoin Core node
p = RawProxy()
p.b

# Run the getblockchaininfo command, store the resulting data in blockchaininfo
blockchaininfo = p.getblockchaininfo()
#networkinfo = p.getnetworkinfo()
#walletinfo = p.getwalletinfo()

# Retrieve the 'blocks' element from the blockchaininfo
print(blockchaininfo['blocks'])
