client request: http://dapp.xyz/connect_app/swap
server then: locates the contract requested, verifies version is version requested
server: creates KEY, IV sends to client, 
client: stores KEY, IV in temp local storage
server: sends AES256 encrypted JSON
client: client side validates the KEY to match contract verification,  
client: client side runtime software (openAI implementation language model for web3) decrypts JSON, rebuilds the decrypted JSON
client: serves rebuilt JSON as html, css, js  (as it normally would be seen in browswer sources...etc) the serves it for display in browser
