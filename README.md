**Caesar Cipher:**

The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It's simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed nuber of positions down the alphabet.

For example: if we have an offset/shift of **1**, then **A** would be replace by **B**, **B** would be replaced by **C**, and so on. Similarly, if we have an offset of **4**, then the text **ATTACKATONCE** would become **EXXEGOEXSRGI**.

The method is named after Roman leader Julius Caesar, who used it in his private correspondence.

Source: [Caesar Cipher](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)

In this project, I will write two functions named **coder** and **decoder** to encode and decipher the messages, respectively. Both functions will take two inputs which are the **message** and the **offset** number.