#!/usr/bin/bash

# This is the Circular Translator installation script.
# Using the "apt" package manager.

# Install translate-shell and gcc.
sudo apt install translate-shell gcc

# Copy source code to /usr/local/src/.
sudo mkdir /usr/local/src/ctranslator
sudo cp src/trans-en.c src/trans-zh.c /usr/local/src/ctranslator/

# Install trans-en and trans-zh.
sudo gcc -Wall /usr/local/src/ctranslator/trans-en.c -o /usr/local/bin/en
sudo gcc -Wall /usr/local/src/ctranslator/trans-zh.c -o /usr/local/bin/zh

# Print infomations.
echo "
"
echo "Installation is complete."
echo "You can start Circular Translator with the commands \"en\" and \"zh\"."

