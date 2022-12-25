```client request: http://dapp.xyz/connect_app/swap
server then: locates the contract requested, verifies version is version requested
server: creates KEY, IV sends to client, 
client: stores KEY, IV in temp local storage
server: sends AES256 encrypted JSON
client: client side validates the KEY to match contract verification,  
client: client side runtime software (openAI implementation language model for web3) decrypts JSON, rebuilds the decrypted JSON
client: serves rebuilt JSON as html, css, js  (as it normally would be seen in browswer sources...etc) the serves it for display in browser
```
```
ENCRYPT AES256: with checksum key:ddddd5d56d56dcd65d6dc56dc65dc65 IV:647277dc7e7baadeca8989769fffea7

in which the contract is registered with a service that provides verification and consistency as an itermediary after
an audit and onward to deployment on mainnets (a vavlidation of contracts essentially--to ensure nothing is changed and is made aware of any upgradeable proxy contracts..etc)

provides a unnique KEY ad IV every time the page is served for verification.

then

AES DECRYPT KEY: ddddd5d56d56dcd65d6dc56dc65dc65, IV: 647277dc7e7baadeca8989769fffea7, MODE: CBC, INPUT: RAW OUTPUT: HEX

hashed JSON: abac235ebace5262323525bc52........... (shortened)
```
