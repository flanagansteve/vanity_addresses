import ecdsa
from Crypto.Hash import keccak

def generate_eth_wallet():
  sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
  vk = sk.get_verifying_key()
  k = keccak.new(digest_bits=256)
  k.update(vk.to_string())
  return { 'public_address' : '0x' + k.hexdigest()[24:], 'private_key' : sk.to_string().hex() }

def get_vanity_address(vanity_str):
  returned_wallet = { 'public_address' : '', 'private_key' : '' }
  while returned_wallet['public_address'][:len(vanity_str)] != vanity_str:
    returned_wallet = generate_eth_wallet()
  return returned_wallet
