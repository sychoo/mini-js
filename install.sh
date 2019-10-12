# install Python library for the parser and lexer
pip3 install rply

# export bin directory to system PATH variable
echo "export PATH=\"`pwd`/bin:\$PATH\"" >> ~/.zshrc

# set environment variable for bashrc
echo "export MINIJS=\"`pwd`\"" >> ~/.zshrc

source $HOME/.zshrc
